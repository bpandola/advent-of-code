def parse_input(filename, dimensions):
    lines = open(filename).read().split('\n')
    translated = {}
    for y, line in enumerate(lines):
        for x, data in enumerate(lines[y]):
            coords = [x, y] + [0] * (dimensions - 2)
            translated[tuple(coords)] = data
    return translated


def get_neighbor_deltas(dimensions):
    dirs = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                for w in [0] if dimensions == 3 else range(-1, 2):
                    if any([n for n in (x, y, z, w) if n != 0]):
                        coords = [x, y, z, w]
                        dirs.append(tuple(coords[:dimensions]))
    return dirs


def num_adjacent_occupied(coords, area, deltas):
    occupied = 0
    for delta in deltas:
        translated = []
        for i in range(len(coords)):
            translated.append(coords[i] + delta[i])

        try:
            if area[tuple(translated)] == '#':
                occupied += 1
        except KeyError:
            pass  # Out of bounds.
    return occupied


def run_simulation(area_map, num_steps=6, dimensions=3):
    deltas = get_neighbor_deltas(dimensions)
    area = area_map.copy()
    start, stop = -1, max(max(list(area.keys()))) + 2
    for i in range(num_steps):
        area_new = area.copy()
        for x in range(start, stop):
            for y in range(start, stop):
                for z in range(start, stop):
                    for w in [0] if dimensions == 3 else range(start, stop):
                        coords = tuple([x, y, z, w][:dimensions])
                        num_neighbors = num_adjacent_occupied(coords, area, deltas)
                        if coords not in area:
                            area[coords] = '.'
                        try:
                            if area[coords] == '#':
                                if num_neighbors not in [2, 3]:
                                    area_new[coords] = '.'
                            elif area[coords] == '.' and num_neighbors == 3:
                                area_new[coords] = '#'
                                if start in coords:
                                    start -= 1
                                if stop - 1 in coords:
                                    stop += 1
                        except KeyError:
                            pass
        area = area_new.copy()
    return list(area.values()).count('#')


if __name__ == '__main__':
    print('Be patient.  This is gonna take a couple minutes...')

    # Part 1
    assert run_simulation(parse_input('day_17.in.sample', 3)) == 112
    print(run_simulation(parse_input('day_17.in', 3)))

    # Part 1
    assert run_simulation(parse_input('day_17.in.sample', 4), dimensions=4) == 848
    print(run_simulation(parse_input('day_17.in', 4), dimensions=4))
