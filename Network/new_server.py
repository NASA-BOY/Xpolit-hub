import pickle
import socket
import select
import Commands as cmds
import database as db
import Constants.Errors as errors

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

users = {"itay": "pass123"}

logged_in_users = {}  # List of clients that are signed in and their email

while True:
    rlist, wlist, xlist = select.select([server_socket] + client_sockets, client_sockets, [])
    for current_socket in rlist:
        if current_socket is server_socket:
            connection, client_address = current_socket.accept()
            print("New client joined!", client_address)
            client_sockets.append(connection)
        else:
            data_recv = current_socket.recv(MAX_MSG_LENGTH)
            data = pickle.loads(data_recv)
            print(data)
            cmd = data[0]
            data.pop(0)

            if cmd == "01":
                email, passw = data
                msg = ''

                result = db.check_sign_in(email, passw)

                if not result:
                    msg = errors.SIGN_IN_INCORRECT

                msg_to_send.append((current_socket, [cmds.SIGN_IN_CMD, result, msg]))

            elif cmd == "02":
                email, username, passw, confirm_passw = data
                msg = ''

                if passw == confirm_passw:
                    result = db.check_email_exists(email)  # Check if the email is already an existing user
                    if not result:
                        db.add_new_user(email=email, passw=passw, username=username)  # Create new user
                    else:
                        msg = errors.EMAIL_EXISTS

                    # Send the appropriate msg to the client
                    msg_to_send.append((current_socket, [cmds.SIGN_UP_CMD, not result, msg]))
                else:
                    # The passwords and the confirm password don't match
                    msg = errors.PASSW_DONT_MATCH
                    msg_to_send.append((current_socket, [cmds.SIGN_UP_CMD, False, msg]))



    for msg in msg_to_send:
        receiver, data = msg
        if receiver in wlist:
            receiver.send(pickle.dumps(data))
            msg_to_send.remove(msg)

