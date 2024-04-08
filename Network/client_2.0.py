import socket
import select


class Client:

    def __init__(self):
        self.IP = "127.0.0.1"
        self.PORT = 5555
        self.MAX_MSG_LENGTH = 4096

        self.msg = ""
        self.data = ""

        self.client_sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.IP, self.PORT))

