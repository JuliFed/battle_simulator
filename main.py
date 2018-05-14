import json
from unit import *


def create_armies_from_json():
    json_data = open('input_data.json').read()
    data = json.loads(json_data)
    list_armies = []
    for army in data:
        arm = Army(army['strategy'])
        for squad in army['squads']:
            s = Squads()
            for prop in squad:
                s.add_units(squad[prop], prop)
            arm.add_squad(s)
        list_armies.append(arm)

    return list_armies


def main():
    list_armies = create_armies_from_json()



if __name__ == '__main__':
    main()
