import pickle
import socket
import threading
from datetime import datetime

import select
import Commands as cmds
from database import Database
import Constants.Errors as errors

import Constants.Vulnerabilities as vuln
import validators
from selenium import webdriver

import Vulnerabilities.XSS.XSS_Scanner as XSS
import Vulnerabilities.SQL.SQL_Inj_Scanner as SQL_INJ
import Vulnerabilities.Command_Injection.payloads
import Vulnerabilities.Command_Injection.Cmd_Inj_Scanner
import Vulnerabilities
import Vulnerabilities.scan_page as SCAN_PAGE
from Vulnerabilities import get_cookies
import re


MAX_MSG_LENGTH = 1024
SERVER_PORT = 5559
SERVER_IP = "0.0.0.0"
print("Setting up server...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()
print("Listening for clients...")
client_sockets = []
msg_to_send = []

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

logged_in_users = {}  # dictionary list of clients that are logged in. client is key and email is value


# Scan function for multithreading for all clients
def client_scan(client_url, vuln_list, client_socket, cookies_str=None):
    cookies = None
    print("started")

    # Check if the URL exists
    if not validators.url(client_url):
        msg_to_send.append((client_socket, [cmds.NEW_SCAN_CMD, False, errors.INVALID_URL]))

    else:
        # =Set up the headless browser driver=
        # Use Selenium to interact with the webpage
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)  # Replace with your preferred browser driver
        driver.get(client_url)

        # Load an actual cookies dictionary for the cookies string received
        if cookies_str != "":
            try:
                cookies = get_cookies.load_cookies_from_string(cookies_str)
            except:
                msg_to_send.append((client_socket, [cmds.NEW_SCAN_CMD, False, errors.BAD_COOKIES]))
                return


        try:
            forms_inputs, forms_details = SCAN_PAGE.get_all_inputs(client_url, cookies)

            if cookies is not None:
                # Add each cookie to the WebDriver
                for name, value in cookies.items():
                    cookie = {'name': name, 'value': value}
                    driver.add_cookie(cookie)

                # Refresh the page to apply the cookies
                driver.refresh()
        except Exception as e:
            print(e)
            msg_to_send.append((client_socket, [cmds.NEW_SCAN_CMD, False, errors.BAD_COOKIES]))
            return

        try:
            for vuln_request in vuln_list:
                # make sure that the web driver is on the right page given by the client
                driver.get(client_url)

                # Reset the scan message, add the appropriate command and add true for no errors
                scan_msg = [cmds.NEW_SCAN_CMD, True]


                # XSS vulnerability scan
                if vuln_request == vuln.XSS:
                    # Add the type of vulnerability to the scan message
                    scan_msg.append(vuln.XSS)

                    vuln_found, forms_index = Vulnerabilities.XSS.XSS_Scanner.scan_xss(forms_inputs, client_url, driver)

                    # Add to the scan message weather an XSS vulnerability has been found on the URL
                    scan_msg.append(vuln_found)

                    # Add every vulnerable form detail to the scan message using it's given index
                    for form_index in forms_index:
                        scan_msg.append(forms_details[form_index])

                    # Add the scan message to be sent back to the client
                    msg_to_send.append((client_socket, scan_msg))


                # SQL Injection vulnerability scan
                elif vuln_request == vuln.SQL_INJECTION:
                    # Add the type of vulnerability to the scan message
                    scan_msg.append(vuln.SQL_INJECTION)

                    vuln_found, forms_index = Vulnerabilities.SQL.SQL_Inj_Scanner.scan_sql(forms_inputs, client_url, driver)

                    # Add to the scan message weather an SQL Injection vulnerability has been found on the URL
                    scan_msg.append(vuln_found)

                    # Add every vulnerable form detail to the scan message using it's given index
                    for form_index in forms_index:
                        scan_msg.append(forms_details[form_index])

                    # Add the scan message to be sent back to the client
                    msg_to_send.append((client_socket, scan_msg))


                # Command Injection vulnerability scan
                elif vuln_request == vuln.CMD_INJECTION:
                    # Add the type of vulnerability to the scan message
                    scan_msg.append(vuln.CMD_INJECTION)

                    vuln_found, forms_index = Vulnerabilities.Command_Injection.Cmd_Inj_Scanner.scan_cmd_injection(forms_inputs, client_url, driver)
                    # Add to the scan message weather a Command Injection vulnerability has been found on the URL
                    scan_msg.append(vuln_found)

                    # Add every vulnerable form detail to the scan message using it's given index
                    for form_index in forms_index:
                        scan_msg.append(forms_details[form_index])

                    # Add the scan message to be sent back to the client
                    msg_to_send.append((client_socket, scan_msg))

        except Exception as e:
            print(e)

        driver.quit()


# Create a new database instance
db = Database()

while True:
    rlist, wlist, xlist = select.select([server_socket] + client_sockets, client_sockets, [])
    for current_socket in rlist:
        if current_socket is server_socket:
            connection, client_address = current_socket.accept()
            print("New client joined!", client_address)
            client_sockets.append(connection)
        else:
            try:
                data_recv = current_socket.recv(MAX_MSG_LENGTH)
                data = pickle.loads(data_recv)
                print(data)
                cmd = data.pop(0)

                if cmd == cmds.SIGN_IN_CMD:
                    email, passw = data
                    msg = ''

                    result = db.check_sign_in(email, passw)

                    if result:
                        logged_in_users[current_socket] = email  # Add the current socket as logged in with their email
                        msg = db.get_username(email)  # The message back to the client is the user's username
                    else:
                        msg = errors.SIGN_IN_INCORRECT

                    msg_to_send.append((current_socket, [cmds.SIGN_IN_CMD, result, msg]))

                elif cmd == cmds.SIGN_UP_CMD:
                    email, username, passw, confirm_passw = data
                    msg = ''

                    # Validate the email address
                    if not re.fullmatch(regex, email):
                        msg_to_send.append((current_socket, [cmds.SIGN_UP_CMD, False, errors.INVALID_EMAIL]))

                    else:
                        if passw == confirm_passw:
                            result = db.check_email_exists(email)  # Check if the email is already an existing user
                            if not result:
                                db.add_new_user(email=email, passw=passw, username=username)  # Create new user
                                logged_in_users[current_socket] = email  # Add the current socket as logged in with their email
                            else:
                                msg = errors.EMAIL_EXISTS

                            # Send the appropriate msg to the client
                            msg_to_send.append((current_socket, [cmds.SIGN_UP_CMD, not result, msg]))
                        else:
                            # The password and the confirm-password don't match
                            msg = errors.PASSW_DONT_MATCH
                            msg_to_send.append((current_socket, [cmds.SIGN_UP_CMD, False, msg]))

                elif cmd == cmds.NEW_SCAN_CMD:
                    url = data.pop(0)
                    client_cookies = data.pop(0)

                    scan = threading.Thread(target=client_scan, args=(url, data, current_socket, client_cookies))
                    scan.start()

                elif cmd == cmds.SAVE_SCAN_CMD:
                    try:
                        scan_id = data.pop(0)  # Get the scan id from the first item in data and remove it from data
                        email = logged_in_users[current_socket]  # Get the client's email from the logged in dictionary

                        # Make sure the scan has not already been saved by making sure the scan id doesn't exist
                        if not db.check_scan_id_exists(email, scan_id):
                            result = data[0]  # What's left in data would be only the scan's result for save

                            # Get the current date and time
                            current_datetime = datetime.now()
                            # Convert the datetime object to a string in a desired format
                            date_time = current_datetime.strftime("%Y-%m-%d %H:%M")

                            # Save the given sacn result to the database
                            db.add_new_scan_save(email, scan_id, date_time, result)

                            msg_to_send.append((current_socket, [cmds.SAVE_SCAN_CMD, True, "Saved!"]))

                        else:
                            msg_to_send.append((current_socket, [cmds.SAVE_SCAN_CMD, False, errors.SCAN_ALREADY_SAVED]))

                    except Exception as e:
                        print(e)
                        msg_to_send.append((current_socket, [cmds.SAVE_SCAN_CMD, False, errors.ERROR_SAVING_SCAN]))

                elif cmd == cmds.GET_ALL_SAVED_DATES_CMD:
                    try:
                        email = logged_in_users[current_socket]  # Get the client's email from the logged in dictionary

                        dates = db.get_all_saved_dates(email)
                        msg_to_send.append((current_socket, [cmds.GET_ALL_SAVED_DATES_CMD, True] + dates))

                    except Exception as e:
                        print(e)
                        msg_to_send.append((current_socket, [cmds.GET_ALL_SAVED_DATES_CMD, False, errors.ERROR_FETCHING_DATES]))

                elif cmd == cmds.GET_SAVED_SCAN_CMD:
                    try:
                        email = logged_in_users[current_socket]  # Get the client's email from the logged in dictionary
                        date_time = data[0]

                        result = db.get_history_save(email, date_time)

                        msg_to_send.append((current_socket, [cmds.GET_SAVED_SCAN_CMD, True, result]))

                    except Exception as e:
                        print(e)
                        msg_to_send.append((current_socket, [cmds.GET_SAVED_SCAN_CMD, False, errors.ERROR_FETCHING_SCAN]))


            except ConnectionResetError:
                # Handle connection reset by client
                print(f"Connection reset by {current_socket}")
                client_sockets.remove(current_socket)

                if current_socket in logged_in_users.keys():
                    del logged_in_users[current_socket]



    for msg in msg_to_send:
        receiver, data = msg
        if receiver in wlist:
            receiver.send(pickle.dumps(data))
            msg_to_send.remove(msg)

