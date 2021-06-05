REFRESH_RATE = 0.01
MAXIMUM_VESSELS_AMOUNT = 201

TYPE = ['Corvette', 'Destroyer', 'Cruiser', 'Battleship', 'Titan']
WEAPON_VISIBLE_DETAILS = ['type', 'cooldown', 'accuracy', 'buff', 'damage', 'range', 'tracking']

INDENTATION = '    '
SECTION_SEPARATER = '------------------------------------------------------------------------------\n'
NOT_VALID = 'Not valid. Enter again:\n'

CORVETTE_CORES = {
    'Interceptor': ['s', 's', 's'],
    'Missile Boat': ['s', 'g'],
    'Picket Ship': ['s', 's', 'p']
}
DESTROYER_BOW = {
    'Artillery': ['l'],
    'Gunship': ['s', 's', 'm'],
    'Picket Ship': ['s', 's', 'p']
}
DESTROYER_STERN = {
    'Gunship': ['m'],
    'Interceptor': ['s', 's'],
    'Picket Ship': ['p', 'p'],
}
CRUISER_BOW = {
    'Artillery': ['l'],
    'Broadside': ['m', 'm'],
    'Torpedo': ['s', 's', 'g'],
}
CRUISER_CORE = {
    'Artillery': ['m', 'l'],
    'Broadside': ['m', 'm', 'm'],
    'Hangar': ['p', 'p', 'h'],
    'Torpedo': ['s', 's', 'g'],
}
CRUISER_STERN = {
    'Broadside': ['m'],
    'Gunship': ['s', 's'],
}
BATTLESHIP_BOW = {
    'Artillery': ['l', 'l'],
    'Broadside': ['s', 's', 'm', 'l'],
    'Hangar': ['m', 'p', 'p', 'h'],
    'Spinal Mount': ['x'],
}
BATTLESHIP_CORE = {
    'Artillery': ['l', 'l', 'l'],
    'Broadside': ['m', 'm', 'l', 'l'],
    'Carrier': ['s', 's', 'p', 'p', 'h', 'h'],
    'Hangar': ['m', 'm', 'm', 'm', 'h'],
}
BATTLESHIP_STERN = {
    'Artillery': ['l'],
    'Broadside': ['m', 'm'],
}
TITAN_BOW = {
    'titan_bow': ['t']
}
TITAN_CORE = {
    'titan_core': ['l', 'l', 'l', 'l']
}
TITAN_STERN = {
    'titan_stern': ['l', 'l']
}

CORVETTE_SECTIONS = {
    'core': CORVETTE_CORES,
}
DESTROYER_SECTIONS = {
    'bow': DESTROYER_BOW,
    'stern': DESTROYER_STERN,
}
CRUISER_SECTIONS = {
    'bow': CRUISER_BOW,
    'core': CRUISER_CORE,
    'stern': CRUISER_STERN,
}
BATTLESHIP_SECTIONS = {
    'bow': BATTLESHIP_BOW,
    'core': BATTLESHIP_CORE,
    'stern': BATTLESHIP_STERN,
}
TITAN_SECTIONS = {
    'bow': TITAN_BOW,
    'core': TITAN_CORE,
    'stern': TITAN_STERN,
}
SLOTS = {
    TYPE[0]: CORVETTE_SECTIONS,
    TYPE[1]: DESTROYER_SECTIONS,
    TYPE[2]: CRUISER_SECTIONS,
    TYPE[3]: BATTLESHIP_SECTIONS,
    TYPE[4]: TITAN_SECTIONS,
}

GAMMA_LASER_S = {
    'type': 'energy',
    'cooldown': 4.6,
    'accuracy': 0.9,
    'buff': {
        'shield': 0.5,
        'armor': 1.5,
        'hull': 1.0
    },
    'size': 's',
    'cost': 22.0,
    'power': 17.0,
    'damage': [17, 46],
    'range': 40,
    'tracking': 0.5,
    'average_damage': 6.16
}
GAMMA_LASER_M = {
    'type': 'energy',
    'cooldown': 4.6,
    'accuracy': 0.9,
    'buff': {
        'shield': 0.5,
        'armor': 1.5,
        'hull': 1.0
    },
    'size': 'm',
    'cost': 44.0,
    'power': 30.0,
    'damage': [43, 115],
    'range': 60,
    'tracking': 0.3,
    'average_damage': 15.45
}
GAMMA_LASER_L = {
    'type': 'energy',
    'cooldown': 4.6,
    'accuracy': 0.9,
    'buff': {
        'shield': 0.5,
        'armor': 1.5,
        'hull': 1.0
    },
    'size': 'l',
    'cost': 88.0,
    'power': 59.0,
    'damage': [102, 276],
    'range': 80,
    'tracking': 0.05,
    'average_damage': 36.97
}
PLASMA_CANNON_S = {
    'type': 'energy',
    'cooldown': 5.1,
    'accuracy': 0.8,
    'buff': {
        'shield': 0.25,
        'armor': 2.0,
        'hull': 1.5
    },
    'size': 's',
    'cost': 22.0,
    'power': 17.0,
    'damage': [20, 42],
    'range': 30,
    'tracking': 0.4,
    'average_damage': 4.86
}
PLASMA_CANNON_M = {
    'type': 'energy',
    'cooldown': 5.1,
    'accuracy': 0.8,
    'buff': {
        'shield': 0.25,
        'armor': 2.0,
        'hull': 1.5
    },
    'size': 'm',
    'cost': 44.0,
    'power': 30.0,
    'damage': [50, 105],
    'range': 50,
    'tracking': 0.2,
    'average_damage': 12.15
}
PLASMA_CANNON_L = {
    'type': 'energy',
    'cooldown': 5.1,
    'accuracy': 0.8,
    'buff': {
        'shield': 0.25,
        'armor': 2.0,
        'hull': 1.5
    },
    'size': 'l',
    'cost': 88.0,
    'power': 59.0,
    'damage': [120, 252],
    'range': 70,
    'tracking': 0.05,
    'average_damage': 29.17
}
TACHYON_LANCE = {
    'type': 'energy',
    'cooldown': 8.0,
    'accuracy': 0.85,
    'buff': {
        'shield': 0.5,
        'armor': 2.0,
        'hull': 1.5
    },
    'size': 'x',
    'cost': 229.0,
    'power': 250.0,
    'damage': [800, 2000],
    'range': 150,
    'tracking': 0.0,
    'average_damage': 148.75
}
CUTTING_LASER_S = {
    'type': 'energy',
    'cooldown': 4.0,
    'accuracy': 0.75,
    'buff': {
        'shield': 0.5,
        'armor': 1.25,
        'hull': 1.75
    },
    'size': 's',
    'cost': 13.0,
    'power': 7.0,
    'damage': [9, 22],
    'range': 30,
    'tracking': 0.4,
    'average_damage': 2.9
}
CUTTING_LASER_M = {
    'type': 'energy',
    'cooldown': 4.0,
    'accuracy': 0.70,
    'buff': {
        'shield': 0.5,
        'armor': 1.25,
        'hull': 1.75
    },
    'size': 'm',
    'cost': 26.0,
    'power': 13.0,
    'damage': [23, 55],
    'range': 60,
    'tracking': 0.2,
    'average_damage': 6.82
}
NEUTRON_LAUNCHERS = {
    'type': 'energy',
    'cooldown': 16.0,
    'accuracy': 0.9,
    'buff': {
        'shield': 0.5,
        'armor': 1.5,
        'hull': 1.75
    },
    'size': 'l',
    'cost': 114.0,
    'power': 90.0,
    'damage': [468, 1040],
    'range': 130,
    'tracking': 0.0,
    'average_damage': 42.41
}
MATTER_DISINTEGRATOR_S = {
    'type': 'energy',
    'cooldown': 4.5,
    'accuracy': 0.9,
    'buff': {
        'shield': 0.5,
        'armor': 1.5,
        'hull': 2.0
    },
    'size': 's',
    'cost': 29.0,
    'power': 25.0,
    'damage': [20, 49],
    'range': 60,
    'tracking': 0.6,
    'average_damage': 6.89
}
MATTER_DISINTEGRATOR_M = {
    'type': 'energy',
    'cooldown': 4.5,
    'accuracy': 0.9,
    'buff': {
        'shield': 0.5,
        'armor': 1.5,
        'hull': 2.0
    },
    'size': 'm',
    'cost': 57.0,
    'power': 50.0,
    'damage': [50, 123],
    'range': 90,
    'tracking': 0.3,
    'average_damage': 17.29
}
MATTER_DISINTEGRATOR_L = {
    'type': 'energy',
    'cooldown': 4.5,
    'accuracy': 0.9,
    'buff': {
        'shield': 0.5,
        'armor': 1.5,
        'hull': 2.0
    },
    'size': 'l',
    'cost': 114.0,
    'power': 100.0,
    'damage': [120, 294],
    'range': 120,
    'tracking': 0.05,
    'average_damage': 41.40
}
PHASED_DISRUPTOR_S = {
    'type': 'energy',
    'cooldown': 6.1,
    'accuracy': 1.0,
    'buff': {
        'shield': -1,
        'armor': -1,
        'hull': 1.0
    },
    'size': 's',
    'cost': 22.0,
    'power': 17.0,
    'damage': [1, 30],
    'range': 30,
    'tracking': 0.6,
    'average_damage': 2.54
}
PHASED_DISRUPTOR_M = {
    'type': 'energy',
    'cooldown': 6.1,
    'accuracy': 1.0,
    'buff': {
        'shield': -1,
        'armor': -1,
        'hull': 1.0
    },
    'size': 'm',
    'cost': 44.0,
    'power': 30.0,
    'damage': [1, 75],
    'range': 50,
    'tracking': 0.35,
    'average_damage': 6.22
}
CLOUD_LIGHTNING = {
    'type': 'energy',
    'cooldown': 6.0,
    'accuracy': 1.0,
    'buff': {
        'shield': -1,
        'armor': -1,
        'hull': 1.0
    },
    'size': 'l',
    'cost': 17.0,
    'power': 40.0,
    'damage': [1, 136],
    'range': 60,
    'tracking': 0.3,
    'average_damage': 11.41
}
FOCUSED_ARC_EMITTER = {
    'type': 'energy',
    'cooldown': 8.1,
    'accuracy': 1.0,
    'buff': {
        'shield': -1,
        'armor': -1,
        'hull': 1.0
    },
    'size': 'x',
    'cost': 229.0,
    'power': 250.0,
    'damage': [1, 1700],
    'range': 150,
    'tracking': 0.0,
    'average_damage': 105.00
}
ENERGY_SIPHON = {
    'type': 'energy',
    'cooldown': 4.0,
    'accuracy': 0.75,
    'buff': {
        'shield': 2.0,
        'armor': 0.25,
        'hull': 1.0
    },
    'size': 's',
    'cost': 15.0,
    'power': 10.0,
    'damage': [10, 27],
    'range': 50,
    'tracking': 0.5,
    'average_damage': 3.46
}
GAUSS_CANNON_S = {
    'type': 'kinetic',
    'cooldown': 3.45,
    'accuracy': 0.75,
    'buff': {
        'shield': 1.5,
        'armor': 0.5,
        'hull': 1.0
    },
    'size': 's',
    'cost': 22.0,
    'power': 17.0,
    'damage': [14, 46],
    'range': 50,
    'tracking': 0.5,
    'average_damage': 6.52
}
GAUSS_CANNON_M = {
    'type': 'kinetic',
    'cooldown': 3.45,
    'accuracy': 0.75,
    'buff': {
        'shield': 1.5,
        'armor': 0.5,
        'hull': 1.0
    },
    'size': 'm',
    'cost': 44.0,
    'power': 30.0,
    'damage': [35, 115],
    'range': 75,
    'tracking': 0.3,
    'average_damage': 16.30
}
GAUSS_CANNON_L = {
    'type': 'kinetic',
    'cooldown': 3.45,
    'accuracy': 0.75,
    'buff': {
        'shield': 1.5,
        'armor': 0.5,
        'hull': 1.0
    },
    'size': 'l',
    'cost': 88.0,
    'power': 59.0,
    'damage': [84, 276],
    'range': 100,
    'tracking': 0.05,
    'average_damage': 39.12
}
STORMFIRE_AUTOCANNON = {
    'type': 'kinetic',
    'cooldown': 2.3,
    'accuracy': 0.85,
    'buff': {
        'shield': 1.5,
        'armor': 0.25,
        'hull': 1.25
    },
    'size': 's',
    'cost': 22.0,
    'power': 17.0,
    'damage': [14, 27],
    'range': 30,
    'tracking': 0.75,
    'average_damage': 7.57
}
KINETIC_ARTILLERY = {
    'type': 'kinetic',
    'cooldown': 6.4,
    'accuracy': 0.75,
    'buff': {
        'shield': 2.00,
        'armor': 0.5,
        'hull': 1.25
    },
    'size': 'l',
    'cost': 114.0,
    'power': 90.0,
    'damage': [195, 585],
    'range': 120,
    'tracking': 0.0,
    'average_damage': 45.70
}
GIGA_CANNON = {
    'type': 'kinetic',
    'cooldown': 9.0,
    'accuracy': 0.75,
    'buff': {
        'shield': 1.5,
        'armor': 0.75,
        'hull': 1.25
    },
    'size': 'x',
    'cost': 229.0,
    'power': 250.0,
    'damage': [900, 2600],
    'range': 150,
    'tracking': 0.0,
    'average_damage': 145.83
}
PERDITION_BEAM = {
    'type': 'titan',
    'cooldown': 21.75,
    'accuracy': 0.85,
    'buff': {
        'shield': 0.75,
        'armor': 1.5,
        'hull': 1.25
    },
    'size': 't',
    'cost': 456.0,
    'power': 500.0,
    'damage': [5000, 10000],
    'range': 250,
    'tracking': 0.0,
    'average_damage': 293.10
}

WEAPON = {
    'gamma_laser_s': GAMMA_LASER_S,
    'gamma_laser_m': GAMMA_LASER_M,
    'gamma_laser_l': GAMMA_LASER_L,
    'plasma_cannon_s': PLASMA_CANNON_S,
    'plasma_cannon_m': PLASMA_CANNON_M,
    'plasma_cannon_l': PLASMA_CANNON_L,
    'tachyon_lance_x': TACHYON_LANCE,
    'cutting_laser_s': CUTTING_LASER_S,
    'cutting_laser_m': CUTTING_LASER_M,
    'neutron_launchers_l': NEUTRON_LAUNCHERS,
    'matter_disintegrator_s': MATTER_DISINTEGRATOR_S,
    'matter_disintegrator_m': MATTER_DISINTEGRATOR_M,
    'matter_disintegrator_l': MATTER_DISINTEGRATOR_L,
    'phased_distuptor_s': PHASED_DISRUPTOR_S,
    'phased_distuptor_m': PHASED_DISRUPTOR_M,
    'cloud_lightning_l': CLOUD_LIGHTNING,
    'focused_arc_emitter_x': FOCUSED_ARC_EMITTER,
    'energy_siphon_s': ENERGY_SIPHON,
    'gauss_cannon_s': GAUSS_CANNON_S,
    'gauss_cannon_m': GAUSS_CANNON_M,
    'gauss_cannon_l': GAUSS_CANNON_L,
    'stormfire_autocannon_s': STORMFIRE_AUTOCANNON,
    'kinetic_artillery_l': KINETIC_ARTILLERY,
    'giga_cannon_x': GIGA_CANNON,
    'perdition_beam_t': PERDITION_BEAM,
}
