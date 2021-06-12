from Stellaris_Combat_Simulation.Vessel import *
from Stellaris_Combat_Simulation.MACRO import *
from json import JSONEncoder


class Fleet:
    fleet_size: int
    fleet_number: str
    quantities: dict
    vessels: dict
    corvettes: list
    destroyers: list
    cruisers: list
    battleships: list
    titans: list

    def __init__(self, fleet_number):
        self.fleet_number = fleet_number
        self.fleet_size = 0
        self.corvettes = list()
        self.destroyers = list()
        self.cruisers = list()
        self.battleships = list()
        self.titans = list()
        self.vessels = {TYPE[0]: self.corvettes, TYPE[1]: self.destroyers, TYPE[2]: self.cruisers,
                        TYPE[3]: self.battleships, TYPE[4]: self.titans}

    def add_vessel(self, type: int, amount: int):
        if type == 0:
            self.corvettes.extend([Corvette(type, i) for i in range(amount)])
        elif type == 1:
            self.destroyers.extend([Destroyer(type, i) for i in range(amount)])
        elif type == 2:
            self.cruisers.extend([Cruiser(type, i) for i in range(amount)])
        elif type == 3:
            self.battleships.extend([Battleship(type, i) for i in range(amount)])
        else:
            self.titans.extend([Titan(type, i) for i in range(amount)])
        self.fleet_size += amount

    def get_fleet_number(self):
        return self.fleet_number

    def get_size(self):
        return self.fleet_size

    def get_quantity(self, type: int):
        return len(self.vessels[TYPE[type]])

    def get_vessel(self, type: int):
        return self.vessels[TYPE[type]][0]

    def get_vessels(self):
        return self.vessels

    def modify_vessels_section(self, type: int, section_name: str, new_section: str):
        for vessel in self.vessels[TYPE[type]]:
            vessel.modify_vessel_section(section_name, new_section)

    def modify_vessels_slots(self, type: int, section_name: str, slot_index: int, weapon_index: int):
        for vessel in self.vessels[TYPE[type]]:
            vessel.modify_vessel_slots(section_name, weapon_index)

    def __str__(self):
        vessels_str = 'Fleet: {}\nSize: {}\nVessels: \n'.format(self.fleet_number, self.fleet_size)
        for type in TYPE:
            vessels_str += INDENTATION + '{} {}\n'.format(len(self.vessels[type]), type)
        return vessels_str[:-1]

    def details(self):
        vessels_str = 'Fleet: {}\nSize: {}\nVessels: \n'.format(self.fleet_number, self.fleet_size)
        for key in self.vessels.keys():
            if len(self.vessels[key]) > 0:
                vessels_str += INDENTATION + self.vessels[key][0].__str__() + '\n'
        return vessels_str[:-1]


class FleetEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
