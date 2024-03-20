import logging
from config import LOG_FILE
import sys

formatter = logging.Formatter('%(asctime)s~%(levelname)s~%(message)s~module:%(module)s\n')

file_handler = logging.FileHandler(LOG_FILE, 'w')
file_handler.setFormatter(formatter)

logger = logging.getLogger('logger')
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

