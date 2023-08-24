import cv2
import socket
import pickle
import struct
import threading

FRAME_RATE = 30


class VideoServer:
    def __init__(self, ip, port, max_clients):
        self.max_clients: int = max_clients
        self.server_socket: socket.socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )
        host_ip: str = ip
        self.socket_address: tuple = (host_ip, port)

        # bind the TCP socket to the host ip and port
        self.server_socket.bind(self.socket_address)

        # lock to update data
        self.data_lock: threading.Lock = threading.Lock()
        self.payload: bytes = None

    def capture(self):
        self.cap = cv2.VideoCapture(0)
        while True:
            _, frame = self.cap.read()
            frame = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))
            data = pickle.dumps(frame)
            message_size = struct.pack("L", len(data))
            self.data_lock.acquire()
            self.payload = message_size + data
            self.data_lock.release()

    def listen(self):
        while True:
            client, addr = self.server_socket.accept()
            print(f"✅ {addr[0]}:{addr[1]}")
            threading.Thread(
                target=self.send,
                args=(
                    client,
                    addr,
                ),
            ).start()

    def send(self, client: socket.socket, addr: tuple):
        while True:
            try:
                client.sendall(self.payload)
            except (ConnectionResetError, BrokenPipeError):
                client.close()
                print(f"❌ Client {addr[0]}:{addr[1]} disconnected")
                break

    def start(self):
        self.server_socket.listen(self.max_clients)
        print(f"📢 {self.socket_address[0]}:{self.socket_address[1]} [LISTENING]")
        threading.Thread(target=self.capture).start()
        self.listen()


if __name__ == "__main__":
    video_server = VideoServer("localhost", 12000, 10)
    video_server.start()
