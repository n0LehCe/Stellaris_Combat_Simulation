from Stellaris_Combat_Simulation.Vessel import *
from Stellaris_Combat_Simulation.MACRO import *
from json import JSONEncoder


class Fleet:
    fleet_size: int
    fleet_number: str
    vessels: dict
    corvettes: list
    destroyers: list
    cruisers: list
    battleships: list
    titans: list

    def __init__(self, fleet_number: str = None, vessels_json: dict = None):
        self.fleet_size = 0
        self.corvettes = list()
        self.destroyers = list()
        self.cruisers = list()
        self.battleships = list()
        self.titans = list()

        if fleet_number:
            self.fleet_number = fleet_number

        if vessels_json:
            self.fleet_number = vessels_json['fleet_number']
            self.fleet_size = vessels_json['fleet_size']
            if vessels_json[TYPE_PLURALS[0]]:
                self.corvettes.extend([Corvette(i, vessels_json[TYPE_PLURALS[0]][0]['sections']) for i in
                                       range(len(list(vessels_json[TYPE_PLURALS[0]])))])
            if vessels_json[TYPE_PLURALS[1]]:
                self.destroyers.extend([Destroyer(i, vessels_json[TYPE_PLURALS[1]][0]['sections']) for i in
                                        range(len(list(vessels_json[TYPE_PLURALS[1]])))])
            if vessels_json[TYPE_PLURALS[2]]:
                self.cruisers.extend([Cruiser(i, vessels_json[TYPE_PLURALS[2]][0]['sections']) for i in
                                      range(len(list(vessels_json[TYPE_PLURALS[2]])))])
            if vessels_json[TYPE_PLURALS[3]]:
                self.battleships.extend([Battleship(i, vessels_json[TYPE_PLURALS[3]][0]['sections']) for i in
                                         range(len(list(vessels_json[TYPE_PLURALS[3]])))])
            if vessels_json[TYPE_PLURALS[4]]:
                self.titans.extend([Titan(i, vessels_json[TYPE_PLURALS[4]][0]['sections']) for i in
                                    range(len(list(vessels_json[TYPE_PLURALS[4]])))])
        self.vessels = {TYPE[0]: self.corvettes, TYPE[1]: self.destroyers, TYPE[2]: self.cruisers,
                        TYPE[3]: self.battleships, TYPE[4]: self.titans}

    def add_vessel(self, type: int, amount: int):
        if 0 == type:
            self.corvettes.extend([Corvette(i) for i in range(amount)])
        elif 1 == type:
            self.destroyers.extend([Destroyer(i) for i in range(amount)])
        elif 2 == type:
            self.cruisers.extend([Cruiser(i) for i in range(amount)])
        elif 3 == type:
            self.battleships.extend([Battleship(i) for i in range(amount)])
        elif 4 == type:
            self.titans.extend([Titan(i) for i in range(amount)])
        self.fleet_size += amount

    def get_fleet_number(self):
        return self.fleet_number

    def get_size(self):
        return self.fleet_size

    def get_quantity(self, type: int):
        return len(self.vessels[TYPE[type]])

    def get_vessel(self, type: int):
        return self.vessels[TYPE[type]][0]

    def get_vessels(self, type: int):
        return self.vessels[TYPE[type]]

    def get_all_vessels(self):
        return self.corvettes + self.destroyers + self.cruisers + self.battleships + self.titans

    def get_status(self):
        pass

    def get_all_weapons(self):
        weapons = list()
        for vessel in self.get_all_vessels():
            weapons.extend(vessel.get_all_weapons())
        return weapons


    def modify_vessels_section(self, type: int, section_name: str, new_section: str):
        for vessel in self.vessels[TYPE[type]]:
            vessel.modify_vessel_section(section_name, new_section)

    def modify_vessels_slots(self, type: int, section_name: str, slot_index: int, weapon_name: str):
        for vessel in self.vessels[TYPE[type]]:
            vessel.modify_vessel_weapon(section_name, slot_index, weapon_name)

    def __str__(self):
        vessels_str = 'Fleet: {}\nSize: {}\nVessels: \n'.format(self.fleet_number, self.fleet_size)
        for type in TYPE:
            vessels_str += INDENTATION + '{} {}\n'.format(len(self.vessels[type]), type)
        return vessels_str[:-1]

    def details(self):
        vessels_str = 'Fleet: {}\nSize: {}\nVessels: \n'.format(self.fleet_number, self.fleet_size)
        for key in self.vessels.keys():
            if len(self.vessels[key]) > 0:
                vessels_str += INDENTATION + str(self.vessels[key][0]) + '\n'
        return vessels_str[:-1]


class FleetEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
