import pickle
import socket
import threading

import select
import Commands as cmds
import database as db
import Constants.Errors as errors

import Constants.Vulnerabilities as vuln
import validators
from selenium import webdriver

import Vulnerabilities.XSS.XSS_selenium as XSS
import Vulnerabilities.SQL.SQL_selenium as SQL_INJ
import Vulnerabilities.Command_Injection.payloads
import Vulnerabilities.Command_Injection.command_injection
import Vulnerabilities
import Vulnerabilities.scan_page as SCAN_PAGE
from Vulnerabilities import get_cookies

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
        #options.add_argument("--headless")
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
        except:
            msg_to_send.append((client_socket, [cmds.NEW_SCAN_CMD, False, errors.BAD_COOKIES]))
            return

        for vuln_request in vuln_list:
            # make sure that the web driver is on the right page given by the client
            driver.get(client_url)

            # Reset the scan message, add the appropriate command and add true for no errors
            scan_msg = [cmds.NEW_SCAN_CMD, True]


            # XSS vulnerability scan
            if vuln_request == vuln.XSS:
                # Add the type of vulnerability to the scan message
                scan_msg.append(vuln.XSS)

                vuln_found, forms_index = Vulnerabilities.XSS.XSS_selenium.scan_xss(forms_inputs, client_url, driver)

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

                vuln_found, forms_index = Vulnerabilities.SQL.SQL_selenium.scan_sql(forms_inputs, client_url, driver)

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

                vuln_found, forms_index = Vulnerabilities.Command_Injection.command_injection.scan_cmd_injection(forms_inputs, client_url, driver)
                # Add to the scan message weather a Command Injection vulnerability has been found on the URL
                scan_msg.append(vuln_found)

                # Add every vulnerable form detail to the scan message using it's given index
                for form_index in forms_index:
                    scan_msg.append(forms_details[form_index])

                # Add the scan message to be sent back to the client
                msg_to_send.append((client_socket, scan_msg))





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
                cmd = data[0]
                data.pop(0)

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

