import socket
import sys

def send_for_prediction(image_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(('localhost', 12345))
        sock.sendall(image_path.encode('utf-8'))
        result = sock.recv(1024).decode('utf-8')
        print(result)

if __name__ == "__main__":
    image_path = sys.argv[1]
    send_for_prediction(image_path)

