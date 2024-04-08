import socket
import select
from Vulnerabilities.XSS import good_XSS

MAX_MSG_LENGTH = 1024
SERVER_PORT = 5555
SERVER_IP = "0.0.0.0"
print("Setting up server...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()
print("Listening for clients...")
client_sockets = []
msg_to_send = []

users = {"itay": "pass123"}
logged_in = {}
sockets_entered_users = {} # list of sockets and the usernames entered to the login

while True:
    rlist, wlist, xlist = select.select([server_socket] + client_sockets, client_sockets, [])
    for current_socket in rlist:
        if current_socket is server_socket:
            connection, client_address = current_socket.accept()
            print("New client joined!", client_address)
            client_sockets.append(connection)
            msg_to_send.append(("=Welcome to Xploit Hub!=\nEnter Username: ", connection))
        else:
            data = current_socket.recv(MAX_MSG_LENGTH).decode()
            if data == "":
                print("Connection closed", )
                client_sockets.remove(current_socket)
                current_socket.close()

            if current_socket not in logged_in.keys():
                if current_socket not in sockets_entered_users.keys():
                    sockets_entered_users[current_socket] = data
                    msg_to_send.append(("Enter Password: ", current_socket))
                elif sockets_entered_users[current_socket] in users.keys() and data == users[sockets_entered_users[current_socket]]:
                    logged_in[current_socket] = sockets_entered_users[current_socket]
                    msg_to_send.append(("You are in!\nEnter the URL to check for XSS vulnerabilities: ", current_socket))
                else:
                    msg_to_send.append(("Wrong username or password, please try again.\nEnter Username: ", current_socket))
                    del sockets_entered_users[current_socket]

            else:
                XSS = good_XSS.scan_xss(data)
                if len(XSS) == 0:
                    msg_to_send.append((f"Congrats, no XSS detected on {data}!", current_socket))
                else:
                    msg_to_send.append((f"-[!] XSS Detected on {data}", current_socket))
                    for vul in XSS:
                        msg_to_send.append(("-" + vul, current_socket))

                msg_to_send.append(("----", current_socket))
                msg_to_send.append(("Enter another URL to check, or hit enter to exit: ", current_socket))

    for msg in msg_to_send:
        data, receiver = msg
        if receiver in wlist:
            receiver.send(data.encode())
            msg_to_send.remove(msg)


