def calculate_fuel_for_mass(mass):
    return mass // 3 - 2


def calculate_fuel_for_fuel(fuel_mass):
    fuel_needed = 0
    fuel_for_fuel = calculate_fuel_for_mass(fuel_mass)
    while fuel_for_fuel > 0:
        fuel_needed += fuel_for_fuel
        fuel_for_fuel = calculate_fuel_for_mass(fuel_for_fuel)
    return fuel_needed


def calculate_fuel_required(mass):
    fuel_for_mass = calculate_fuel_for_mass(mass)
    fuel_for_fuel = calculate_fuel_for_fuel(fuel_for_mass)
    return fuel_for_mass + fuel_for_fuel


if __name__ == '__main__':
    puzzle_input = [int(i) for i in open('day_1.in').read().split('\n')]

    # Part 1
    assert calculate_fuel_for_mass(12) == 2
    assert calculate_fuel_for_mass(14) == 2
    assert calculate_fuel_for_mass(1969) == 654
    assert calculate_fuel_for_mass(100756) == 33583

    print sum([calculate_fuel_for_mass(m) for m in puzzle_input])

    # Part 2
    assert calculate_fuel_required(14) == 2
    assert calculate_fuel_required(1969) == 966
    assert calculate_fuel_required(100756) == 50346

    print sum([calculate_fuel_required(m) for m in puzzle_input])
