import cv2
import socket
import pickle
import struct
import signal


class VideoClient:
    def __init__(self, host_ip, host_port):
        self.socket_addr = (host_ip, host_port)
        self.make_connection()

    def make_connection(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.socket_addr)

    def start(self):
        data = b""
        payload_size = struct.calcsize("L")
        while True:
            while len(data) < payload_size:
                data += self.client_socket.recv(2048)
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("L", packed_msg_size)[0]
            while len(data) < msg_size:
                data += self.client_socket.recv(2048)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)
            cv2.imshow("Live Stream", frame)
            cv2.waitKey(1)

    def __del__(self):
        self.client_socket.close()


def signal_handler(signal, frame):
    print("\n Closing connection and exiting...")
    video_client.client_socket.close()
    exit(0)


if __name__ == "__main__":
    video_client = VideoClient("localhost", 12000)
    signal.signal(signal.SIGINT, signal_handler)
    video_client.start()
