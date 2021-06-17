from Stellaris_Combat_Simulation.Section import *
from Stellaris_Combat_Simulation.MACRO import *


class Vessel:
    type: int
    vessel_number: int
    sections: dict

    def __init__(self, type: int, vessel_number: int, sections_json: dict = None):
        self.type = type
        self.vessel_number = vessel_number
        self.sections = dict()
        if sections_json:
            for key, value in sections_json.items():
                self.sections[key] = Section(slots_json=value)

    def get_compatible_sections(self):
        return list(self.sections.keys())

    def get_section(self, type):
        return self.sections[type]

    def get_available_sections(self):
        pass

    def get_all_weapons(self):
        weapons = list()
        for section in self.sections.values():
            weapons.extend(section.get_all_weapons())
        return weapons

    def modify_vessel_section(self, section_name: str, new_section: str):
        self.sections[section_name].change_section(self.type, section_name, new_section)

    def modify_vessel_weapon(self, section_name: str, slot_index: int, weapon_name: str):
        self.sections[section_name].modify_slots(slot_index, weapon_name)

    def __str__(self):
        vessel_str = '{} #{} with'.format(TYPE[int(self.type)], self.vessel_number)
        for key in self.sections.keys():
            vessel_str += '\n' + INDENTATION + key + ': ' + str(self.sections[key])
        return vessel_str


class Corvette(Vessel):
    def __init__(self, vessel_number, sections_json: dict = None):
        super().__init__(0, vessel_number, sections_json)
        if not sections_json:
            self.sections['core'] = Section()


class Destroyer(Vessel):
    def __init__(self, vessel_number, sections_json: dict = None):
        super().__init__(1, vessel_number, sections_json)
        if not sections_json:
            self.sections['bow'], self.sections['stern'] = Section(), Section()


class Cruiser(Vessel):
    def __init__(self, vessel_number, sections_json: dict = None):
        super().__init__(2, vessel_number, sections_json)
        if not sections_json:
            self.sections['bow'], self.sections['core'], self.sections['stern'] = Section(), Section(), Section()


class Battleship(Vessel):
    def __init__(self, vessel_number, sections_json: dict = None):
        super().__init__(3, vessel_number, sections_json)
        if not sections_json:
            self.sections['bow'], self.sections['core'], self.sections['stern'] = Section(), Section(), Section()


class Titan(Vessel):
    def __init__(self, vessel_number, sections_json: dict = None):
        super().__init__(4, vessel_number, sections_json)
        if not sections_json:
            self.sections['bow'], self.sections['core'], self.sections['stern'] = Section(), Section(), Section()
