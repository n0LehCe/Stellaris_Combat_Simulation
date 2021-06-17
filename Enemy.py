from Stellaris_Combat_Simulation.MACRO import WEAPON
import random


class Enemy:
    enemy_number: str
    spec: dict
    shield: float
    armor: float
    hull: float
    evasion: float
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
                'hull': 3000,
                'evasion': 0.3
            }
        self.shield = spec['shield']
        self.armor = spec['armor']
        self.hull = spec['hull']
        self.evasion = spec['evasion']
        self.has_shield = True
        self.has_armor = True
        self.is_destroyed = False

    def receive_damage(self, weapon):
        # case evasion
        if weapon['tracking'] > self.evasion:
            accuracy = weapon['accuracy']
        else:
            accuracy = weapon['accuracy'] - (self.evasion - weapon['tracking'])
        hit = random.randint(1, 100)
        if hit >= accuracy * 100:
            return

        damage = random.randint(weapon['damage'][0], weapon['damage'][1])

        # case penetration
        if weapon['buff']['shield'] == -1 and weapon['buff']['armor'] == -1:
            self.hull -= damage
            if self.hull <= 0:
                self.is_destroyed = True

        # case regular
        elif self.has_shield:
            self.shield -= damage * weapon['buff']['shield']
            if self.shield <= 0:
                self.has_shield = False
                damage = abs(self.shield)
                self.shield = 0
                self.armor -= damage * weapon['buff']['armor']
                if self.armor <= 0:
                    self.has_armor = False
                    damage = abs(self.armor)
                    self.armor = 0
                    self.hull -= damage * weapon['buff']['hull']
                    if self.hull <= 0:
                        self.is_destroyed = True
        elif self.has_armor:
            self.armor -= damage * weapon['buff']['armor']
            if self.armor <= 0:
                self.has_armor = False
                damage = abs(self.armor)
                self.armor = 0
                self.hull -= damage * weapon['buff']['hull']
                if self.hull <= 0:
                    self.is_destroyed = True
        else:
            self.hull -= damage * weapon['buff']['hull']
            if self.hull <= 0:
                self.is_destroyed = True