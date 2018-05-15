import random as rnd
from base import Unit
import lib


class Soldier(Unit):
    counter = 0

    def __init__(self, experience=0):
        self.experience = experience
        self._health = 100
        self.__class__.counter += 1
        self.name = "Soldier " + str(self.__class__.counter)

    @property
    def health(self):
        """
        Returned Soldier's health
        """
        return self._health

    @health.setter
    def health(self, value):
        if value == 0:
            del self
        self._health = value

    def damage(self):
        return round(0.05 + self.experience / 100, lib.ROUND_NUMBER)

    def attack(self):
        """
        Вероятность успеха атаки
        0.5 * (1 + health/100) * random(50 + experience, 100) / 100
        """
        rnd_koofic = rnd.randrange(50 + self.experience, 100) / 100
        return round(0.5 * (1 + self.health / 100) * rnd_koofic, lib.ROUND_NUMBER)

    def add_experience(self):
        """
        Add experience from 0 to 50(max)
        """
        if self.experience <= 50:
            self.experience += 1

    def print_composition(self, name=''):
        if name == '':
            name = self.name
        print('\t', name, self.health, self.experience)


class Vehicles(Unit):
    """
        Venicles have operators from 1 to 3. In start has 3 operators.
        If all operators was killed - vehicles killed too
    """
    counter = 0

    def __init__(self, unit_name=Soldier, count_operators=3):
        self.operators = []
        self.count_operators = count_operators
        self.__class__.counter += 1
        self.name = "Vehicle " + str(self.__class__.counter)
        unit_name().__class__.counter = 0
        for _ in range(count_operators):
            self.operators.append(unit_name())
        self._health = 100

    @property
    def health(self):
        """
        Returned health of vehicles
        """
        return self.total_health()

    @health.setter
    def health(self, value):
        if value == 0:
            del self
        self._health = value

    def total_health(self):
        """
                Returned health of vehicles and all operators
        """
        total_health = self._health + sum([operator.health
                                           for operator in self.operators])
        return total_health

    def attack(self):
        attacks_value = [operator.attack()
                         for operator in self.operators]
        return round(0.5 * (1 + self.health / 100) * lib.geo_mean(attacks_value),
                     lib.ROUND_NUMBER)

    def damage(self):
        sum_exp = sum([operator.experience / 100
                       for operator in self.operators])
        return round(0.1 + sum_exp, lib.ROUND_NUMBER)

    def print_composition(self):
        print('\t', self.name)
        for operator in self.operators:
            print('\t', '\t', operator.health, operator.experience)
