import random as rnd
from base import Strategy


class RandomStrategy(Strategy):
    def select_squad(self, army):
        """
        Select random squad
        """
        return rnd.choiсe(army.squads)
