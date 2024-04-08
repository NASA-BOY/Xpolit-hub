import socket
import select


class Client:

    def __init__(self):
        self.IP = "127.0.0.1"
        self.PORT = 5555
        self.MAX_MSG_LENGTH = 4096

        self.data_to_send = []

        self.client_sockt = None
        self.connected = False

    def connect(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.IP, self.PORT))
            self.connected = True
            print("Connected to server.")
        except Exception as e:
            print(f"Connection failed: {e}")
            self.connected = False

    def send_data(self, data):
        try:
            self.client_socket.send(data.encode())
        except Exception as e:
            print(f"Error sending message: {e}")

    def receive_data(self):
        try:
            rlist, _, _ = select.select([self.client_socket], [self.client_socket], [], 10)
            if self.client_socket in rlist:
                data = self.client_socket.recv(4096).decode()
                return data

        except Exception as e:
            print(f"Error receiving message: {e}")

    def disconnect(self):
        if self.connected:
            self.client_socket.close()
            self.connected = False

