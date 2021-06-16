from Stellaris_Combat_Simulation.MACRO import WEAPON
import random


class Enemy:
    enemy_number: str
    spec: dict
    shield: float
    armor: float
    hull: float
    has_shield: bool
    has_armor: bool
    is_destroyed: bool

    def __init__(self, enemy_number: str, spec: dict = None):
        self.enemy_number = enemy_number
        if spec:
            self.spec = spec
        else:
            self.spec = {
                'shield': 2500,
                'armor': 1500,
                'hull': 3000
            }
        self.shield = spec['shield']
        self.armor = spec['armor']
        self.hull = spec['hull']
        self.has_shield = True
        self.has_armor = True
        self.is_destroyed = False

    def receive_damage(self, weapon):
        damage = random.randint(WEAPON[weapon]['damage'][0], WEAPON[weapon]['damage'][1])

        # case penetration
        if WEAPON[weapon]['buff']['shield'] == -1 and WEAPON[weapon]['buff']['armor'] == -1:
            self.hull -= damage
            if self.hull <= 0:
                self.is_destroyed = True
        # case regular
        elif self.has_shield:
            self.shield -= damage * WEAPON[weapon]['buff']['shield']
            if self.shield <= 0:
                self.has_shield = False
        elif self.has_armor:
            self.armor -= damage * WEAPON[weapon]['buff']['armor']
            if self.armor <= 0:
                self.has_armor = False
        else:
            self.hull -= damage * WEAPON[weapon]['buff']['hull']
            if self.hull <= 0:
                self.is_destroyed = True
