import socket


class TCP_Client:
    def __init__(self):
        # create client socket and connect to server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ("localhost", 8080)

    def start(self):
        self.client_socket.connect(self.server_address)

        # send message to server and receive response
        self.client_socket.send(input("Enter message: ").encode())
        response = self.client_socket.recv(2048)
        print(f"Response: {response.decode()}")

        # close connection after transaction
        self.client_socket.close()


if __name__ == "__main__":
    client = TCP_Client()
    client.start()
