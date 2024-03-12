import socket
import re
from logger import logger
import argparse
from config import FORMAT, HEADER_LENGHT
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT = 6060
SERVER_ADDR = ()

class Client:
    def __init__(self, client_port):
        self.port = client_port

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.client_socket.connect((host, port))
    
    def send(self, msg: str):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_lenght = str(msg_length).encode(FORMAT)
        send_lenght += b' ' * (HEADER_LENGHT - len(send_lenght))
        self.client_socket.send(send_lenght)
        self.client_socket.send(message)
        


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=int, metavar='', help='<port:default_value=5054>')
    parser.add_argument('-s', type=str, metavar='', help='<server_ip:server_port>')
    args = parser.parse_args()

    server_ip, server_port = args.s.split(':')
    server_port = int(server_port)

    client = Client(args.p)
    client.connect(server_ip, server_port)
    client.send("hellow server mdf de nuevo")
