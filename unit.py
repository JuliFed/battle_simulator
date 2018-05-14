import random as rnd
try:
    import numpy as np
except ImportError:
    print("Can't import numpy")
from base import Unit

ROUND_NUMBER = 2


def geo_mean(num_list):
    """
    Function for geometric average from list
    """
    np_array = np.array(num_list)
    return np_array.prod() ** (1.0 / len(np_array))


class Soldier(Unit):
    def __init__(self, experience=0):
        self.experience = experience

    @property
    def health(self):
        """
        Returned Soldier's health
        """
        return self.health

    def attack(self):
        """
        Вероятность успеха атаки
        0.5 * (1 + health/100) * random(50 + experience, 100) / 100
        """
        rnd_koofic = rnd.randrange(50 + self.experience, 100) / 100
        return round(0.5 * (1 + self.health/100) * rnd_koofic, ROUND_NUMBER)

    def add_experience(self):
        """
        Add experience from 0 to 50(max)
        """
        if self.experience <= 50:
            self.experience += 1

    def attacking(self):
        pass

    def defending(self):
        pass


class Vehicles(Unit):
    """
        Venicles have operators from 1 to 3. In start has 3 operators.
        If all operators was killed - vehicles killed too
    """

    @property
    def health(self):
        """
        Returned health of vehicles
        """
        return self.health

    def __init__(self, unit_name=Soldier, count_operators=3):
        self.operators = []
        self.count_operators = count_operators
        for _ in range(count_operators):
            self.operators.append(unit_name())
        self.health = 100
        # self.recharge = random.randrange(1000, 2000)

    def total_health(self):
        """
                Returned health of vehicles and all operators
        """
        total_health = self.health
        for unit in self.operators:
            total_health += unit.health

        return round(total_health / (self.count_operators + 1), ROUND_NUMBER)

    def attack(self):
        attacks_value = [i.attack
                         for i in self.operators]
        return round(0.5 * (1 + self.health / 100) * geo_mean(attacks_value),
                     ROUND_NUMBER)

    def operators_experience(self):
        sum_exp = 0
        for operator in self.operators:
            sum_exp += operator.experience / 100
        return sum_exp

    def damage(self):
        return round(0.1 + self.operators_experience(), ROUND_NUMBER)

    def attacking(self):
        pass

    def defending(self):
        pass


class Squad:
    """
    Class for Squad
    Squad has different units
    """
    def __init__(self):
        self.count_units = 0
        self.units = []

    def add_units(self, count_units, *unit_type):
        for _ in range(count_units):
            self.units.append(*unit_type)
        self.count_units += count_units

    def attack(self):
        # TODO
        pass

    def damage(self):
        total_damage = 0
        for unit in self.units:
            total_damage += unit.damage
        return total_damage


class Army:
    """
    Class for army
    Army has squads, strategy

    """
    def __init__(self, strategy):
        self.squads = []
        self.strategy = strategy

    def add_squad(self, squad):
        self.squads.append(squad)

    def total_damage(self):
        pass
