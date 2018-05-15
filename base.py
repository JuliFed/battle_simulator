"""
Base classes for units and strateries
"""

from abc import ABCMeta, abstractmethod


class Unit(metaclass=ABCMeta):
    """
        Abstract base class for units
    """
    @property
    @abstractmethod
    def health(self):
        """
        Abstract property for unit's health
        """
        pass

    @abstractmethod
    def attack(self):
        """
        Abstract method for attack
        """
        pass

    @abstractmethod
    def damage(self):
        """
        Abstract method for defending
        """
        pass
    # recharge = random.randrange(100, 2000)


class Strategy(metaclass=ABCMeta):
    """
    Abstract class for strategies
    """
    @abstractmethod
    def select_squad(self, army):
        """
        Method to choice squad with self strategy fight
        """
        pass
