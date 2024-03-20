import socket
from logger import logger
import argparse
from config import FORMAT, HEADER_LENGHT, CHAINS_FILE
from chains_generator import RandomChainsGenerator
import threading
import time

class Client:
    def __init__(self):
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
        

class ChainsClient(Client):
    def __init__(self, number_of_chains, chains_generator_instance):
        Client.__init__(self)

        self.number_of_chains = number_of_chains
        self.start_time = time.time()
        logger.info("Generating chains")
        chains_generator_instance.generate_chains(self.number_of_chains)
        self.chains_to_send = chains_generator_instance.generated_chains
        logger.info("Chains generated succefully")
        logger.info("Exporting chains to file")
        self._generate_chains_file()
        self.end_time = 0


    def _generate_chains_file(self):
        with open(CHAINS_FILE, 'w') as file:
            for chain in self.chains_to_send:
                file.write(chain)
                file.write('\n')


    def process_chains(self):
        for chain in self.chains_to_send:
            self.send(chain)
            msg_length = self.client_socket.recv(HEADER_LENGHT)
            msg_length = int(msg_length)
            msg = self.client_socket.recv(msg_length).decode(FORMAT)
            if len(msg) < msg_length:
                logger.error(f"An error occurred while receiving the text string. Expected string lenght: {msg_length}, received string lenght: {len(msg)}")

            logger.info(f"Chain: {chain}")
            logger.info(f"Measure: {msg}")
        
        self.end_time = time.time()
        logger.info(f"Process completed in {self.end_time - self.start_time} seconds.")
        self.client_socket.close()
        

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=str, metavar='', help='<server_ip:server_port>')
    parser.add_argument('-c', type=int, metavar='', help='<number of chains of the chain.txt file>')
    args = parser.parse_args()

    server_ip, server_port = args.s.split(':')
    server_port = int(server_port)
    chain_number = args.c

    if not args.c:
        chain_number = 1000000

    client = ChainsClient(chain_number, RandomChainsGenerator())
    client.connect(server_ip, server_port)
    client.process_chains()