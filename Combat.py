from Stellaris_Combat_Simulation.Fleet import *
from Stellaris_Combat_Simulation.Enemy import *
from Stellaris_Combat_Simulation.Log import *


class Combat:
    fleet: Fleet
    enemy: Enemy
    duration: float
    has_end: bool

    def __init__(self, fleet: Fleet, enemy: Enemy):
        self.fleet = fleet
        self.enemy = enemy
        self.duration = 0
        self.has_end = False

    def fire(self):
        pass

    def update_status(self, duration: float) -> CombatStatusLog:
        pass


    def start(self) -> CombatResultLog:
        pass

class DummyCombat(Combat):
    def __init__(self, fleet: Fleet, dummy_enemy: Dummy):
        super().__init__(fleet, dummy_enemy)

    def fire(self):
        for weapon in self.fleet.get_all_weapons():
            if weapon.get_status():
                weapon.fire()
                self.enemy.receive_damage(weapon)


    def update_status(self, duration: float) -> CombatStatusLog:
        pass


# TBD
class FleetsCombat(Combat):
    def __init__(self, fleet_offense: Fleet, fleet_defense: Fleet):
        super().__init__(fleet_offense, fleet_defense)

    def fire(self):
        pass

    def update_status(self, duration: float) -> CombatStatusLog:
        fleet_offense_status = self.fleet.get_status()
        fleet_defense_status = self.enemy.get_status()
        if fleet_offense_status['is_destroyed'] or fleet_defense_status['is_destroyed']:
            self.has_end = True
        pass