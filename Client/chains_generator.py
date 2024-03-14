import rstr
import abc
from abc import abstractmethod
import random
import string


class ChainGenerator(metaclass = abc.ABCMeta):
    def __init__(self, chains_qty = 1000000):
        self.chains_qty = chains_qty
        self.generated_chains = []

    @abstractmethod
    def generate_chains():
        pass


class RandomChainsGenerator(ChainGenerator):
    def __init__(self, chains_qty = 1000000):
        ChainGenerator.__init__(self, chains_qty)

    def _getRandomChar(self):
        return random.choice(string.ascii_letters + string.digits)

    def generate_chains(self):
        for i in range(self.chains_qty):
            chain = []
            white_spaces = random.randint(3, 5)
            chain_lenght = random.randint(50, 100)

            for j in range(chain_lenght):
                chain.append(self._getRandomChar())

            for k in range(white_spaces):
                while True:
                    index_to_change = random.randint(1, chain_lenght-2)
                    if chain[index_to_change] != ' ' and chain[index_to_change - 1] != ' ' and chain[index_to_change + 1] != ' ':
                        chain[index_to_change] = ' '
                        break

            chain = ''.join(chain)
            self.generated_chains.append(chain)
            
            