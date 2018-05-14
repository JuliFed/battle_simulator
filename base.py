import random
from abc import ABCMeta, abstractmethod


class Unit:
    health = 100
    recharge = random.randrange(100, 2000)


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def select_squad(self, army):
        pass
