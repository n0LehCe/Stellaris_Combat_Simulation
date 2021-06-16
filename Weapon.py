from Stellaris_Combat_Simulation.MACRO import *


class Weapon:
    name: str
    type: str
    cooldown: float
    accuracy: float
    buff: dict
    size: str
    cost: float
    power: float
    damage: list
    range: float
    tracking: float
    average_damage: float
    status: float

    def __init__(self, name: str = None, weapon_specs_json: dict = None):
        if name:
            self.name = name
            self.type = WEAPON[name]['type']
            self.cooldown = WEAPON[name]['cooldown']
            self.accuracy = WEAPON[name]['accuracy']
            self.buff = WEAPON[name]['buff']
            self.size = WEAPON[name]['size']
            self.cost = WEAPON[name]['cost']
            self.power = WEAPON[name]['power']
            self.damage = WEAPON[name]['damage']
            self.range = WEAPON[name]['range']
            self.tracking = WEAPON[name]['tracking']
            self.average_damage = WEAPON[name]['average_damage']
            self.status = 0

        if weapon_specs_json:
            self.name = weapon_specs_json['name']
            self.type = weapon_specs_json['type']
            self.cooldown = weapon_specs_json['cooldown']
            self.accuracy = weapon_specs_json['accuracy']
            self.buff = weapon_specs_json['buff']
            self.size = weapon_specs_json['size']
            self.cost = weapon_specs_json['cost']
            self.power = weapon_specs_json['power']
            self.damage = weapon_specs_json['damage']
            self.range = weapon_specs_json['range']
            self.tracking = weapon_specs_json['tracking']
            self.average_damage = weapon_specs_json['average_damage']
            self.status = weapon_specs_json['status']

    def update_status(self):
        self.status += REFRESH_RATE
        if self.status >= 0:
            self.status = 0

    def get_status(self):
        return self.status == 0

    def fire(self):
        self.status = -self.cooldown

    def __str__(self):
        return self.name
