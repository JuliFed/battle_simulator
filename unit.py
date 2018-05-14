import random
from base import Unit

try:
    import numpy as np
except ImportError:
    print("Can't import numpy")


ROUND_NUMBER = 2


def geo_mean(iterable):
    a = np.array(iterable)
    return a.prod() ** (1.0 / len(a))


class Soldier(Unit):

    def __init__(self, experience=0):
        self.experience = experience

    @property
    def health(self):
        return self.health

    """ 
        Вероятность успеха атаки
    """

    def attack(self):
        # 0.5 * (1 + health/100) * random(50 + experience, 100) / 100
        return round(0.5 * (1 + self.health / 100) * random.randrange(50 + self.experience, 100) / 100, ROUND_NUMBER)

    """
        Сумма нанесенного урона
    """

    def damage(self):
        # 0.05 + experience / 100
        return round(0.05 + self.experience / 100, ROUND_NUMBER)

    def add_experience(self):
        if self.experience <= 50:
            self.experience += 1

    def attacking(self):
        pass

    def defending(self):
        pass


class Vehicles(Unit):
    """

    """
    @property
    def health(self):
        return self.health

    def __init__(self, unit_name=Soldier, count_operators=3):
        self.operators = []
        self.count_operators = count_operators
        for i in range(count_operators):
            self.operators.append(unit_name())
        self.health = 100
        self.recharge = random.randrange(1000, 2000)

    def total_health(self):
        total_health = self.health
        for unit in self.operators:
            total_health += unit.health

        return round(total_health / (self.count_operators + 1), ROUND_NUMBER)

    def attack(self):
        attacks_value = [i.attack
                         for i in self.operators
                         ]
        return round(0.5 * (1 + self.health / 100) * geo_mean(attacks_value), ROUND_NUMBER)

    def operators_experience(self):
        sum_exp = 0
        for i in self.operators:
            sum_exp += i.experience / 100
        return sum_exp

    def damage(self):
        return round(0.1 + self.operators_experience(), ROUND_NUMBER)

    def attacking(self):
        pass

    def defending(self):
        pass


class Squads:
    def __init__(self):
        self.count_units = 0
        self.units = []

    def add_units(self,count_units, *unit_type):
        for i in range(count_units):
            self.units.append(*unit_type)
        self.count_units += count_units

    def damage(self):
        total_damage = 0
        for unit in self.units:
            total_damage += unit.damage
        return total_damage


class Army:
    def __init__(self, strategy):
        self.squads = []
        self.strategy = strategy

    def add_squad(self, sq):
        self.squads.append(sq)

