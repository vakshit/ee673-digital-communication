import socket
import netifaces
import threading


def get_local_ip(interface="wlp4s0"):
    try:
        local_ip = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]["addr"]
        return local_ip
    except Exception as e:
        print("Error:", e)
        return None


class ChatServer:
    def __init__(self, client, port=12000) -> None:
        self.client = client
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = (get_local_ip(), port)
        self.server_socket.bind(self.server_address)
        print(
            f"UDP server is listening on {self.server_address[0]}:{self.server_address[1]}"
        )

    def listen(self):
        while True:
            data, client_address = self.server_socket.recvfrom(2048)
            print(f"{client_address[0]}:{client_address[1]} => {data.decode()}")

    def send(self):
        while True:
            print("Enter message to send: ")
            message = input()
            self.server_socket.sendto(message.encode(), self.client)


if __name__ == "__main__":
    client_ip = input("Enter client IP: ")
    client_port = int(input("Enter client port: "))
    chatapp = ChatServer((client_ip, client_port), 12000)
    threading.Thread(target=chatapp.listen).start()
    threading.Thread(target=chatapp.send).start()
