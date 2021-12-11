def parse_input(filename):
    crab_positions = [int(n) for n in open(filename).read().split(',')]
    return crab_positions


def run_simulation(positions, constant_fuel=True):
    def calculate_fuel(source, dest):
        dist = abs(source - dest)
        if constant_fuel:
            return dist
        total_fuel = 0
        for i in range(1, dist + 1):
            total_fuel += i
        return total_fuel

    pos_min = min(positions)
    pos_max = max(positions)
    lowest_fuel = 100000000
    for pos in range(pos_min, pos_max + 1):
        fuel = 0
        for crab in positions:
            fuel += calculate_fuel(crab, pos)
            if fuel > lowest_fuel:
                break
        if fuel < lowest_fuel:
            lowest_fuel = fuel
    return lowest_fuel


if __name__ == '__main__':
    puzzle_input = parse_input('day_07.in')
    sample_input = parse_input('day_07.in.sample_01')

    # Part 1
    assert run_simulation(sample_input) == 37
    print(run_simulation(puzzle_input))

    # Part 2
    assert run_simulation(sample_input, constant_fuel=False) == 168
    print(run_simulation(puzzle_input, constant_fuel=False))
