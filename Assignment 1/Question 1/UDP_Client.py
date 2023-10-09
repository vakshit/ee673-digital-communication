import socket


class UDP_Client:
    def __init__(self, server_address: tuple) -> None:
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = server_address

    def send(self, message: str):
        self.client_socket.sendto(message.encode(), self.server_address)
        response, _ = self.client_socket.recvfrom(2048)
        print(f"Received response: {response.decode()}")
        self.client_socket.close()


if __name__ == "__main__":
    client = UDP_Client(("localhost", 8080))
    client.send(input("Enter message: "))
