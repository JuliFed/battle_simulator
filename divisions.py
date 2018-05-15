import unit
import lib

class Squad:
    """
    Class for Squad
    Squad has different units
    """
    def __init__(self, squad):
        self.count_units = 0
        self.units = []
        for unit_name in squad:
            self.add_units(squad[unit_name], unit_name)

    def add_units(self, count_units, unit_type):
        for _ in range(count_units):
            self.units.append(getattr(unit, unit_type)())
        self.count_units += count_units
        print(self.units)

    def attack(self):
        total_attack = [one.attack()
                for one in self.units]
        print(total_attack)
        return lib.geo_mean(total_attack)

    def damage(self):
        total_damage = 0
        for unit in self.units:
            total_damage += unit.damage
        return total_damage

    def total_health(self):
        total_health = 0
        for unit in self.units:
            total_health += unit.health
        return total_health


class Army:
    """
    Class for army
    Army has squads, strategy

    """
    def __init__(self, strategy, squads):
        self.squads = []
        self.strategy = strategy
        for squad in squads:
            self.add_squad(Squad(squad))

    def add_squad(self, squad):
        self.squads.append(squad)

    def total_damage(self):
        pass

