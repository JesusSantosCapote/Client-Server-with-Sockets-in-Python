import socket
import threading
import sys
import argparse
from logger import logger
from config import HEADER_LENGHT, FORMAT


class Server:
    def __init__(self, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._ip = socket.gethostbyname(socket.gethostname())
        self._port = port
        self.server_socket.bind((self._ip, self._port))


    def _handle_client(self, conn: socket.socket, addr):
        logger.info(f"Connection accepted from {addr[0]}:{addr[1]}")

        connected = True
        while connected:
            msg_length = conn.recv(HEADER_LENGHT)
            if not msg_length:
                connected = False
            else:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if len(msg) < msg_length:
                    logger.error(f"An error occurred while receiving the text string. Expected string lenght: {msg_length}, received string lenght: {len(msg)}")

                logger.info(msg)

        conn.close()
        logger.info(f"Connection with {addr[0]}:{addr[1]} closed")


    def start(self):
        self.server_socket.listen()
        logger.info(f"Server is listening on {self._ip}:{self._port}")
        while True:
            conn, addr = self.server_socket.accept()
            thread = threading.Thread(target=self._handle_client, args=(conn, addr))
            thread.start()
            logger.info(f"Active Connections: {threading.active_count() - 1}")

    
    def send(msg):
        pass
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=int, metavar='', help='<port:default_value=5050>')
    args = parser.parse_args()

    port = 5050

    if args.p:
        port = args.p

    server = Server(port)

    logger.info("Server is starting...")
    server.start()
