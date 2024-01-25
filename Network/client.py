import socket
import select

IP = '127.0.0.1'
PORT = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
data_to_send = []
msg = ""
data = ""


while True:
    rlist, wlist, xlist = select.select([client_socket], [client_socket], [], 10)

    for message in data_to_send:
        if client_socket in wlist:
            client_socket.send(message.encode())
            data_to_send.remove(message)

    if client_socket in rlist:
        data = client_socket.recv(4096).decode()

    if data != "":
        if not data.startswith('-'):
            data_to_send.append(input(data))
        else:
            print(data)
        data = ""




