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

    def modify_vessel_slots(self, section_name: str, weapon_index: int):
        pass

    def __str__(self):
        vessel_str = '{} #{} with'.format(TYPE[int(self.type)], self.vessel_number)
        for key in self.sections.keys():
            vessel_str += '\n' + INDENTATION + key + ': ' + self.sections[key].__str__()
        return vessel_str


class Corvette(Vessel):
    core: Section

    def __init__(self, type, vessel_number):
        self.core = Section()
        super().__init__(type, vessel_number)
        self.sections['core'] = self.core


class Destroyer(Vessel):
    bow: Section
    stern: Section

    def __init__(self, type, vessel_number):
        self.bow, self.stern = Section(), Section()
        super().__init__(type, vessel_number)
        self.sections['bow'] = self.bow
        self.sections['stern'] = self.stern


class Cruiser(Vessel):
    bow: Section
    core: Section
    stern: Section

    def __init__(self, type, vessel_number):
        self.bow, self.core, self.stern = Section(), Section(), Section()
        super().__init__(type, vessel_number)
        self.sections['bow'] = self.bow
        self.sections['core'] = self.core
        self.sections['stern'] = self.stern


class Battleship(Vessel):
    bow: Section
    core: Section
    stern: Section

    def __init__(self, type, vessel_number):
        self.bow, self.core, self.stern = Section(), Section(), Section()
        super().__init__(type, vessel_number)
        self.sections['bow'] = self.bow
        self.sections['core'] = self.core
        self.sections['stern'] = self.stern


class Titan(Vessel):
    bow: Section
    core: Section
    stern: Section

    def __init__(self, type, vessel_number):
        self.bow, self.core, self.stern = Section(), Section(), Section()
        super().__init__(type, vessel_number)
        self.sections['bow'] = self.bow
        self.sections['core'] = self.core
        self.sections['stern'] = self.stern
