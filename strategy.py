import random
from base import Strategy


class RandomStrategy(Strategy):
    name = 'RandomStrategy'

    def select_squad(self, army):
        """
        Select random squad
        """
        weakest_squad = random.choice(army.squads)
        return weakest_squad


class WeakestStrategy(Strategy):
    name = 'WeakestStrategy'

    def select_squad(self, army):
        """
        Select weakest squad
        """
        weakest_squad = random.choice(army.squads)
        return weakest_squad


class StrongestStrategy(Strategy):
    name = 'StrongestStrategy'

    def select_squad(self, army):
        """
        Select strongest squad
        """
        weakest_squad = random.choice(army.squads)
        return weakest_squad
