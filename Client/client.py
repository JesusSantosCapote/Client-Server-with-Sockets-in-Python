import socket
import re
from logger import logger
from config import FORMAT, HEADER_LENGHT

IP = socket.gethostbyname(socket.gethostname())
PORT = 6060
SERVER_ADDR = ()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(SERVER_ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_lenght = str(msg_length).encode(FORMAT)
    send_lenght = b' ' * (HEADER_LENGHT - len(send_lenght))
    client.send(send_lenght)
    client.send(message)


if __name__ == "__main__":
    arg_help = "{0} -p <port:default_value=5050> -s <server_ip:server_port>".format(sys.argv[0])

    try:
        opts, args = getopt.getopt(argv[1:], "p:h:s", ["port=", "help", "server="])
    except:
        logger.critical(arg_help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            logger.info(arg_help)  # print the help message
            sys.exit(2)

        if opt in ("-p", "--port"):
            try:
                PORT = int(arg)
            except ValueError:
                logger.critical("Invalid port value")

        if opt in ("-s", "--server"):
            # Regular expression for match IP:Port address
            address_re = re.compile("[0-9]{3}.[0-9]{3}.[0-9]{3}.[0-9]{3}:[0-9]{5}")

            if not address_re.match(arg):
                logger.critical("Value of server argument dont match with an IP:Port address")
                logger.info(arg_help)
                sys.exit(2)

            server_ip, server_port = str(arg).split(':')
            server_port = int(server_port)
            SERVER_ADDR = (server_ip, server_port)

    if not SERVER_ADDR:
        logger.critical("You need to enter a server address")
        sys.exit(2)
