"""
Main module for start battle simulator
"""
import json, pyclbr, configparser
import random as rnd
from divisions import Army


def get_config_battle():
    rules = {}
    config = configparser.ConfigParser()
    config.read("config.ini")
    options = config.options("Rules")
    for option in options:
        rules[option] = config.get("Rules", option)
    return rules


def create_random_armies():
    rules = get_config_battle()
    unit_types = pyclbr.readmodule('unit')
    base_types = pyclbr.readmodule('base')
    for base in base_types:
        unit_types.pop(base, 'None')
    unit_types = tuple(unit_types.keys())
    list_armies = []
    for _ in range(rnd.randrange(int(rules['armies']),int(rules['armies']*2))):
        army = []
        strategy = rules['strategies'].split('|')
        for _ in range(rnd.randrange(int(rules['squads']),int(rules['squads']*2))):
            squad = {}
            for unit_type in unit_types:

                squad[unit_type] = rnd.randrange(int(rules['minunits']), int(rules['maxunits']))
            army.append(squad)
        arm = Army(strategy, army)
        list_armies.append(arm)
    return list_armies


def create_armies_from_json():
    """
    Read json file "input_data.json" for creating armies
    """
    json_data = open('input_data.json').read()
    data = json.loads(json_data)
    list_armies = []
    for army in data:
        arm = Army(army['strategy'], army['squads'])
        list_armies.append(arm)
    return list_armies


def main():
    """
    Main function to start simulator
    """
    list_armies = create_armies_from_json()
    #list_armies = create_random_armies()

    print(list_armies[0].squads[0].attack())
    print(list_armies[0].squads[0].damage())





if __name__ == '__main__':
    main()
