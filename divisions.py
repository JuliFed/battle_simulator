import unit
import lib
import strategy


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
        self.score = 0
        self.alive = True
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

    def died_units(self):
        for one_unit in self.units:
            if one_unit.health <= 0:
                self.units.remove(one_unit)
        if len(self.units) == 0:
            self.alive = False

    def total_health(self):
        total_health = 0
        for one_unit in self.units:
            total_health += one_unit.health
        return round(total_health, lib.ROUND_NUMBER)

    def print_composition(self, flag=0):
        result = self.name + " Health=" + str(self.total_health()) + " Damage=" + str(self.damage()) + '\n'
        if flag == 1:
            for one_unit in self.units:
                result += one_unit.print_composition()
        return result

    def lost(self, damage):
        count_units = len(self.units)
        for one_unit in self.units:
            one_unit.lost(round(damage/count_units, lib.ROUND_NUMBER))
        self.died_units()
        if self.total_health() <= 0:
            self.alive = False

    def win(self, damage):
        self.score += damage*100
        for one_unit in self.units:
            one_unit.win()


class Army:
    """
    Class for army
    Army has squads, strategy
    """

    def __init__(self, name, strategy_name, squads):
        self.alive = True
        self.squads = []
        self.name = name
        try:
            self.strategy = getattr(strategy, strategy_name)()
        except AttributeError:
            print('Can not create army with strategy ' + strategy_name)
            print('Army was created with RandomStrategy by default')
            self.strategy = strategy.RandomStrategy()

        Squad({}).__class__.counter = 0
        for squad in squads:
            self.add_squad(Squad(squad))

    @property
    def score(self):
        score = 0
        for squad in self.squads:
            score += squad.score
        return score

    def add_squad(self, squad):
        self.squads.append(squad)

    def died_squad(self):
        for squad in self.squads:
            if not squad.alive:
                self.squads.remove(squad)
        if len(self.squads) == 0:
            self.alive = False

    def total_health(self):
        total_health = 0
        for squad in self.squads:
            total_health += squad.total_health()
        if total_health <= 0:
            self.alive = False
        return round(total_health, lib.ROUND_NUMBER)

    def print_composition(self, flag=0):
        result = '______________'
        result += self.name + ' (' + self.strategy.name + ')'
        result += '______________' + '\n'
        for squad in self.squads:
            result += squad.print_composition(flag)
        return result

    def attack_enemy(self, enemy):
        result = self.name + ' (Health=' + str(self.total_health()) + ') VS '+enemy.name + ' (Health=' + str(enemy.total_health()) + ')\n'
        for attacking_squad in self.squads:
            if len(enemy.squads) == 0:
                enemy.died_squad()
                break

            defending_squad = self.strategy.select_squad(enemy)
            attacking_squad_probability = attacking_squad.attack()
            defending_squad_probability = defending_squad.attack()
            result += '\t' + attacking_squad.name + ' VS ' + defending_squad.name + ' => '
            if attacking_squad_probability > defending_squad_probability:
                damage = attacking_squad.damage()
                defending_squad.lost(damage)
                attacking_squad.win(damage)
                result += ' Round Win (' + str(attacking_squad_probability) + '/' + str(defending_squad_probability) + '),'
                result += ' Damage = ' + str(damage)+ ', Health=' + str(attacking_squad.total_health())
                result += ', Enemy Health=' + str(defending_squad.total_health()) + '\n'
                enemy.died_squad()
            else:
                result += ' Round Lost (' + str(attacking_squad_probability) + '/' + str(defending_squad_probability)
                result += ', Health=' + str(attacking_squad.total_health())
                result += ', Enemy Health=' + str(defending_squad.total_health()) + ')\n'

        return result
