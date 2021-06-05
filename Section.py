from Stellaris_Combat_Simulation.Slot import *
from Stellaris_Combat_Simulation.MACRO import *


class Section():
    name: str
    slots: list

    def __init__(self):
        self.name = 'no section'
        self.slots = []

    def change_section(self, type: int, section_name: str, new_section: str):
        self.name = new_section
        for slot_type in SLOTS[TYPE[type]][section_name][new_section]:
            self.slots.append(Slot(slot_type))

    @staticmethod
    def get_available_sections(type: int, section_name: str):
        return SLOTS[TYPE[type]][section_name]

    def get_slots(self):
        return self.slots

    def modify_slots(self):
        pass

    def __str__(self):
        slot_str = self.name
        if len(self.slots) != 0:
            slot_str += '\n' + INDENTATION * 2
        for slot in self.slots:
            slot_str += str(slot) + '  '
        return slot_str
