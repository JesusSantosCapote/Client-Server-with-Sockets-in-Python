import socket
import threading
import sys
import getopt
from logger import logger
from config import HEADER_LENGHT, DECODE_FORMAT

IP = socket.gethostbyname(socket.gethostname())
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))

def handle_client(conn: socket.socket, addr):
    logger.info(f"Connection accepted from {addr[0]}:{addr[1]}")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER_LENGHT)
        msg_length = int(msg_length)

        if msg_length == 0: 
            connected = False
        else:
            msg = conn.recv(msg_length).decode(DECODE_FORMAT)
            if len(msg) < msg_length:
                logger.error(f"An error occurred while receiving the text string. Expected string lenght: {msg_length}, received string lenght: {len(msg)}")

            logger.info(msg)

    conn.close()
    logger.info(f"Connection with {addr[0]}:{addr[1]} closed")


def start():
    server.listen()
    logger.info(f"Server is listening on {IP}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        logger.info(f"Active connections ")
    

logger.info("Server is starting...")
start()

if __name__ == "__main__":
    arg_help = "{0} -p <port:default_value=5050>".format(sys.argv[0])

    try:
        opts, args = getopt.getopt(argv[1:], "p:h", ["port=", "help"])
    except:
        logger.critical(arg_help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)

        if opt in ("-p", "--port"):
            try:
                PORT = int(arg)
            except ValueError:
                logger.critical("Invalid port value")
