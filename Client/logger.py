import logging
from config import LOG_FILE
import sys

formatter = logging.Formatter('%(asctime)s~%(levelname)s~%(message)s~module:%(module)s\n')

prompt_handler = logging.StreamHandler(sys.stdout)
prompt_handler.setFormatter(formatter)

file_handler = logging.FileHandler(LOG_FILE, 'w')
file_handler.setFormatter(formatter)

logger = logging.getLogger('logger')
logger.addHandler(prompt_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

