import random
from abc import ABCMeta, abstractmethod


class Unit(metaclass=ABCMeta):
    @property
    @abstractmethod
    def health(self):
        pass

    @abstractmethod
    def attacking(self):
        pass

    @abstractmethod
    def defending(self):
        pass
    # recharge = random.randrange(100, 2000)


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def select_squad(self, army):
        pass
