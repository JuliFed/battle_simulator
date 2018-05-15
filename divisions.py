import unit
import lib
from strategy import RandomStrategy


class Squad:
    """
    Class for Squad
    Squad has different units
    """

    counter = 0

    def __init__(self, squad):
        self.units = []
        self.__class__.counter += 1
        self.name = "Squad " + str(self.__class__.counter)
        for unit_name in squad:
            self.add_units(squad[unit_name], unit_name)

    def add_units(self, count_units, unit_type):
        getattr(unit, unit_type)().__class__.counter = 0
        for _ in range(count_units):
            self.units.append(getattr(unit, unit_type)())

    def attack(self):
        total_attack = [one_unit.attack()
                        for one_unit in self.units]
        return round(lib.geo_mean(total_attack), lib.ROUND_NUMBER)

    def damage(self):
        total_damage = 0
        for one_unit in self.units:
            total_damage += one_unit.damage()
        return round(total_damage, lib.ROUND_NUMBER)

    def total_health(self):
        total_health = 0
        for one_unit in self.units:
            total_health += one_unit.health
        return total_health

    def print_composition(self, flag=0):
        print(self.name, "Health", self.total_health(), "Damage", self.damage())
        if flag == 1:
            for one_unit in self.units:
                one_unit.print_composition()


class Army:
    """
    Class for army
    Army has squads, strategy
    """

    def __init__(self, name, strategy, squads):
        self.squads = []
        if strategy == 'random':
            self.strategy = RandomStrategy()
        self.name = name
        for squad in squads:
            self.add_squad(Squad(squad))

    def add_squad(self, squad):
        self.squads.append(squad)

    def total_damage(self):
        pass

    def print_composition(self):
        print('##############################')
        print(self.name)
        print('##############################')
        for squad in self.squads:
            squad.print_composition()

    def attack_enemy(self, enemy):
        squad_for_attack = self.strategy.get_squad(enemy)
        pass
