import socket
import re
from logger import logger
import argparse
from config import FORMAT, HEADER_LENGHT
import sys
from chains_generator import RandomChainsGenerator
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 6060
SERVER_ADDR = ()

class Client:
    def __init__(self, client_port):
        self.port = client_port

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.client_socket.connect((host, port))
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()
    
    def send(self, msg: str):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_lenght = str(msg_length).encode(FORMAT)
        send_lenght += b' ' * (HEADER_LENGHT - len(send_lenght))
        self.client_socket.send(send_lenght)
        self.client_socket.send(message)
        
    def receive(self):
        connected = True
        while connected:
            msg_length = self.client_socket.recv(HEADER_LENGHT)
            if not msg_length:
                connected = False
            else:
                msg_length = int(msg_length)
                msg = self.client_socket.recv(msg_length).decode(FORMAT)
                if len(msg) < msg_length:
                    logger.error(f"An error occurred while receiving the text string. Expected string lenght: {msg_length}, received string lenght: {len(msg)}")

                logger.info(msg)

        self.client_socket.close()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=int, metavar='', help='<port:default_value=5054>')
    parser.add_argument('-s', type=str, metavar='', help='<server_ip:server_port>')
    args = parser.parse_args()

    server_ip, server_port = args.s.split(':')
    server_port = int(server_port)

    client = Client(args.p)
    client.connect(server_ip, server_port)

    gen = RandomChainsGenerator(20)
    gen.generate_chains()
    for chain in gen.generated_chains:
        client.send(chain)
