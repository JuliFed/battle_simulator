"""
Main module for start battle simulator
"""
import configparser
import json
import pyclbr
import random

from divisions import Army


class EventLogToFile:
    def __init__(self, file='battle_log.txt'):
        self.f = open(file, 'w')

    def __del__(self):
        self.f.close()
        del self.f

    def add_strings_in_log(self, strs):
        self.f.write(strs)


class Game:
    def __init__(self, file_log, console_print=0, create_from='json'):
        self.game_over = False
        self.round_counter = 1
        self.armies = []
        self.file_log = file_log
        self.win = []
        self.console_print = console_print
        self.rules = {}
        if create_from == 'json':
            try:
                self.create_armies_from_json()
            except FileNotFoundError:
                self.create_random_armies()
        elif create_from == 'random_armies':
            self.create_random_armies()
        else:
            raise AttributeError

    def get_config_battle(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        options = config.options("Rules")
        for option in options:
            self.rules[option] = config.get("Rules", option)

    def create_random_armies(self):
        self.get_config_battle()
        unit_types = pyclbr.readmodule('unit')
        base_types = pyclbr.readmodule('base')
        for base in base_types:
            unit_types.pop(base, 'None')
        unit_types = tuple(unit_types.keys())
        count_arm = random.randrange( int(self.rules['armies']), int(self.rules['armies']) * 2)
        # print('COUNT_ARMIES', count_arm)
        for number_arm in range(count_arm):
            army = []
            name = 'Army ' + str(number_arm+1)
            strategy = random.choice(self.rules['strategies'].split('|'))
            count_squads = random.randrange( int(self.rules['squads']), int(self.rules['squads']) * 2)
            for number_squad in range(count_squads):
                squad = {}
                for unit_type in unit_types:
                    squad[unit_type] = random.randrange(int(self.rules['minunits']), int(self.rules['maxunits']))
                army.append(squad)
            arm = Army(name, strategy, army)
            self.armies.append(arm)

    def create_armies_from_json(self):
        """
        Read json file "input_data.json" for creating armies
        """
        try:
            json_data = open('input_data.json').read()
        except FileNotFoundError:
            raise
        data = json.loads(json_data)
        for army in data:
            arm = Army(army['name'], army['strategy'], army['squads'])
            self.armies.append(arm)

    def fight(self):
        while not self.game_over:
            members = random.sample(self.armies, 2)
            member1 = members[0]
            member2 = members[1]

            self.file_log.add_strings_in_log('Round ' + str(self.round_counter) + '\n')
            if self.console_print:
                print('Round ' + str(self.round_counter) + '\n')

            result = member1.attack_enemy(member2)

            self.file_log.add_strings_in_log(result)
            if self.console_print:
                print(result)
            self.game_over_state()
            if self.game_over:
                break

            result = member2.attack_enemy(member1)
            if self.console_print:
                print(result)
            self.file_log.add_strings_in_log(result)

            self.file_log.add_strings_in_log('\n')
            self.round_counter += 1
            self.game_over_state()

    def game_over_state(self):
        for member in self.armies:
            if not member.alive:
                self.armies.remove(member)
        if len(self.armies) < 2:
            self.game_over = True
            self.win = self.armies
            if self.console_print:
                print('GameOver')


def main():
    """
    Main function to start simulator
    """
    file_log = EventLogToFile('battle.txt')
    game = Game(file_log, 1, 'json')
    game.fight()
    del file_log

    for arm in game.armies:
        army_composition = arm.print_composition()
        game.file_log.add_strings_in_log(army_composition)
        if game.console_print:
            print(army_composition)


if __name__ == '__main__':
    main()
