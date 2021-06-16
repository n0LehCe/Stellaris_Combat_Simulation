from Stellaris_Combat_Simulation.Section import *
from Stellaris_Combat_Simulation.MACRO import *


class Vessel:
    type: int
    vessel_number: int
    sections: dict

    def __init__(self, type, vessel_number):
        self.type = type
        self.vessel_number = vessel_number
        self.sections = dict()

    def get_compatible_sections(self):
        return list(self.sections.keys())

    def get_section(self, type):
        return self.sections[type]

    def get_available_sections(self):
        pass

    def modify_vessel_section(self, section_name: str, new_section: str):
        self.sections[section_name].change_section(self.type, section_name, new_section)

    def modify_vessel_weapon(self, section_name: str, slot_index: int, weapon_name: str):
        self.sections[section_name].modify_slots(slot_index, weapon_name)

    def __str__(self):
        vessel_str = '{} #{} with'.format(TYPE[int(self.type)], self.vessel_number)
        for key in self.sections.keys():
            vessel_str += '\n' + INDENTATION + key + ': ' + self.sections[key].__str__()
        return vessel_str


class Corvette(Vessel):
    def __init__(self, type, vessel_number):
        core = Section()
        super().__init__(type, vessel_number)
        self.sections['core'] = core


class Destroyer(Vessel):
    def __init__(self, type, vessel_number):
        bow, stern = Section(), Section()
        super().__init__(type, vessel_number)
        self.sections['bow'] = bow
        self.sections['stern'] = stern


class Cruiser(Vessel):
    def __init__(self, type, vessel_number):
        bow, core, stern = Section(), Section(), Section()
        super().__init__(type, vessel_number)
        self.sections['bow'] = bow
        self.sections['core'] = core
        self.sections['stern'] = stern


class Battleship(Vessel):
    def __init__(self, type, vessel_number):
        bow, core, stern = Section(), Section(), Section()
        super().__init__(type, vessel_number)
        self.sections['bow'] = bow
        self.sections['core'] = core
        self.sections['stern'] = stern


class Titan(Vessel):
    def __init__(self, type, vessel_number):
        bow, core, stern = Section(), Section(), Section()
        super().__init__(type, vessel_number)
        self.sections['bow'] = bow
        self.sections['core'] = core
        self.sections['stern'] = stern
