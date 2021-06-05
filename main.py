from Stellaris_Combat_Simulation.Fleet import *


def load_vessels_types(type_str: str):
    for x in TYPE:
        type_str += '#' + str(TYPE.index(x) + 1) + INDENTATION + x + '\n'
    return type_str


def initialize_fleet(quantities: list, fleet: Fleet):
    for type in range(len(quantities)):
        fleet.add_vessel(type, int(quantities[type]))
    return fleet


def main_get_quantities():
    test_mode = input('#1: mixed vessels fleet\n'
                      '#2: single type vessels fleet\n'
                      '#3. single vessel\n')
    while test_mode not in ['1', '2', '3']:
        test_mode = input(NOT_VALID)

    quantities = [0, 0, 0, 0, 0]
    print(SECTION_SEPARATER[:-1])
    if test_mode == '1':
        quantities = [x for x in input('Enter quantities(*,**,***,****,@):\n').split(' ')]
        while len(quantities) != 5 or ([quantities[i].isdigit() for i in range(5)].__contains__(False)):
            quantities = [x for x in input(NOT_VALID).split(' ')]
    elif test_mode == '2':
        type_str = 'Enter type:\n'
        type_str = load_vessels_types(type_str)
        type = input(type_str)
        while type not in list(map(str, list(range(1, 6)))):
            type = input(NOT_VALID)
        quantity = input(SECTION_SEPARATER + 'Enter quantity:\n')
        while quantity not in range(1, MAXIMUM_VESSELS_AMOUNT):
            quantity = input(NOT_VALID)
        quantities[int(type) - 1] = quantity
    else:
        type_str = 'Enter type:\n'
        type_str = load_vessels_types(type_str)
        type = input(type_str)
        while type not in list(map(str, list(range(1, 6)))):
            type = input(NOT_VALID)
        quantities[int(type) - 1] = 1
    return quantities


def arm_fleet(fleet: Fleet):
    print(SECTION_SEPARATER[:-1])
    print(fleet)
    available_type = [i+1 for i in [0, 1, 2, 3, 4] if fleet.get_quantity(i) != 0]

    editting_fleet_status = True
    while (editting_fleet_status):
        type_str = 'Enter type of vessels you would like to arm(1-Corvette,...,5-Titan)("done" if you have done editting this vessel):\n'
        type_str = load_vessels_types(type_str)
        type = input(type_str)
        while type not in list(map(str, available_type)):
            if type == 'done':
                editting_fleet_status = False
                break
            type = input(NOT_VALID)
        if not editting_fleet_status:
            break
        type = int(type) - 1

        editting_vessel_status = True
        while (editting_vessel_status):
            vessel = fleet.get_vessel(type)
            print(SECTION_SEPARATER[:-1])
            print(vessel)
            section_type = input(
                'Enter the section type you would like to arm("done" if you have done editting this vessel)\n')
            while section_type not in vessel.get_compatible_sections():
                if section_type == 'done':
                    editting_vessel_status = False
                    break
                section_type = input(NOT_VALID)
            if not editting_vessel_status:
                break

            section = vessel.get_section(section_type)
            print(SECTION_SEPARATER + '{}: {}'.format(section_type, section))
            available_sections_str = 'available sections:\n'
            available_sections = section.get_available_sections(type, section_type)
            for key in available_sections:
                available_sections_str += '#' + str(
                    list(available_sections.keys()).index(key) + 1) + INDENTATION + key + ':'
                for x in available_sections[key]:
                    available_sections_str += ' ' + str(x)
                available_sections_str += '\n'
            section_index = input('Enter the section you would like to install:\n' + available_sections_str)
            while section_index not in list(map(str, list(range(1, len(available_sections) + 1)))):
                section_index = input(NOT_VALID)
            section_index = int(section_index) - 1

            vessel.modify_vessel_section(section_type, list(available_sections.keys())[section_index])
            print(SECTION_SEPARATER[:-1])
            print(vessel)
            for slot in section.get_slots():
                available_weapon_str = 'Available weapons for ' + str(slot) + ':\n#0' + INDENTATION + 'None'
                available_weapons = slot.get_available_weapons()
                for key in available_weapons.keys():
                    available_weapon_str += '\n#' + str(
                        list(available_weapons.keys()).index(key) + 1) + INDENTATION + key + ':'
                    for weapon_detail_key in WEAPON_VISIBLE_DETAILS:
                        available_weapon_str += '  ' + weapon_detail_key + ': ' + str(
                            available_weapons[key][weapon_detail_key])
                available_weapon_str += '\nWhich weapon would you like to arm to this slot\n'
                selected_weapon_index = input(available_weapon_str)
                while selected_weapon_index not in list(map(str, range(0, len(available_weapons.keys()) + 1))):
                    selected_weapon_index = input(NOT_VALID)
                if int(selected_weapon_index) > 0:
                    slot.arm(list(available_weapons.keys())[int(selected_weapon_index) - 1])
                print(SECTION_SEPARATER[:-1])
            print(vessel)
    print(fleet.details())

def main():
    fleet = Fleet('test_fleet_000')
    initialize_fleet(main_get_quantities(), fleet)
    arm_fleet(fleet)


if __name__ == '__main__':
    main()
