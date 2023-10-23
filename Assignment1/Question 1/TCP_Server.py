import socket


class TCP_Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ("localhost", 8080)

    def start(self):
        self.server_socket.bind(self.server_address)
        self.server_socket.listen(1)
        print(
            f"TCP server is listening at {self.server_address[0]}:{self.server_address[1]}..."
        )

    def listen(self):
        self.start()
        while True:
            client_socket, client_address = self.server_socket.accept()

            while True:
                data = client_socket.recv(2048)
                if not data:
                    break
                client_socket.send(data.upper())
            client_socket.close()


if __name__ == "__main__":
    server = TCP_Server()
    server.listen()
