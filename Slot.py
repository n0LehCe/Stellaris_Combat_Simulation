from Stellaris_Combat_Simulation.Weapon import *


class Slot():
    type: str
    weapon: Weapon

    def __init__(self, type: str):
        self.type = type
        self.weapon = None

    def get_available_weapons(self):
        available_weapons = {}
        for key in WEAPON.keys():
            if key[-1] == self.type:
                available_weapons[key] = WEAPON[key]
        return available_weapons

    def arm(self, weapon: str):
        self.weapon = Weapon(weapon)

    def __str__(self):
        return '{}: {}'.format(self.type, self.weapon)
