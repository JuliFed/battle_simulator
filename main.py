"""
Main module for start battle simulator
"""

import json
from unit import Army, Squad


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
    print(list_armies)


if __name__ == '__main__':
    main()
