import socket


class UDP_Server:
    def __init__(self, server_address: tuple) -> None:
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = server_address

    def start(self):
        self.server_socket.bind(self.server_address)
        print(
            f"UDP server is listening at {self.server_address[0]}:{self.server_address[1]}..."
        )

    def listen(self):
        self.start()
        while True:
            data, client_address = self.server_socket.recvfrom(2048)
            self.server_socket.sendto(data.upper(), client_address)


if __name__ == "__main__":
    server = UDP_Server(("localhost", 8080))
    server.listen()
