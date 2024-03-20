import re
from logger import logger

def calculate_weighing_measure(chain:str):
    double_A_rule = re.compile("(aa)|(aA)|(Aa)|(AA)")

    if double_A_rule.search(chain):
        logger.info(f"Double ‘a’ rule detected >> {chain}")
        return 1000

    white_spaces = 0
    digits = 0
    letters = 0

    for char in chain:
        if char.isspace():
            white_spaces += 1
        elif char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
        else:
            logger.critical(f"Chain {chain} contains elements that is not alphanumeric or white space. The chain measure will be 0")
            return 0

    return (letters * 1.5 + digits * 2) / white_spaces


