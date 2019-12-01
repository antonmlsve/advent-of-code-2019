def get_fuel_from_mass(mass):
    return int(mass / 3) - 2

def get_fuel_from_mass_exclude_fuel_mass(mass_list):
    total_fuel = 0
    for mass in mass_list:
        total_fuel += get_fuel_from_mass(mass)
    return total_fuel

def get_field_from_mass_include_fuel(mass_list):
    total_fuel = 0
    for mass in mass_list:
        total_fuel += get_fuel_for_fuel(0, mass)
    return total_fuel

def get_fuel_for_fuel(module_fuel_for_fuel, mass):
        fuel = get_fuel_from_mass(mass)
        if fuel > 0:
            module_fuel_for_fuel += fuel + get_fuel_for_fuel(module_fuel_for_fuel, fuel)
        return module_fuel_for_fuel

if __name__ == "__main__":
    input_file = open("data/input.txt", "r")
    module_masses_str = input_file.read().split('\n')
    module_masses = list(map(int, module_masses_str))

    total_fuel_task1 = get_fuel_from_mass_exclude_fuel_mass(module_masses)
    print('Total fuel spent excluding mass for fuel itself: ' + str(total_fuel_task1))

    total_fuel_task2 = get_field_from_mass_include_fuel(module_masses)
    print('Total fuel spent including mass for fuel itself: ' + str(total_fuel_task2))
