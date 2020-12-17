

def parse_input(filename):
    lines = open(filename).read().split('\n')
    translated = {}
    for y, line in enumerate(lines):
        for x, data in enumerate(lines[y]):
            translated[(x, y, 0)] = data
    return translated


dirs = [
    (-1, -1, 0), (0, -1, 0), (1, -1, 0), (-1, 1, 0), (0, 1, 0), (1, 1, 0), (-1, 0, 0), (1, 0, 0),

    (-1, -1, 1), (0, -1, 1), (1, -1, 1), (-1, 1, 1), (0, 1, 1), (1, 1, 1), (-1, 0, 1), (1, 0, 1), (0, 0, 1),

    (-1, -1, -1), (0, -1, -1), (1, -1, -1), (-1, 1, -1), (0, 1, -1), (1, 1, -1), (-1, 0, -1), (1, 0, -1), (0, 0, -1)

]


def num_adjacent_occupied(coords, area):
    occupied = 0
    x, y, z = coords
    for dx, dy, dz in dirs:
        try:
            if area[(x + dx, y + dy, z + dz)] == '#':
                occupied += 1
        except KeyError:
            pass  # Out of bounds.
    return occupied


def num_visibly_occupied(coords, area):
    occupied = 0
    x, y, z = coords
    for dx, dy in dirs:
        px, py = x, y
        while True:
            px += dx
            py += dy
            try:
                if area[(px, py)] == 'L':
                    break
                if area[(px, py)] == '#':
                    occupied += 1
                    break
            except KeyError:
                pass  # Out of bounds.
    return occupied


def run_simulation(area_map):
    area = area_map.copy()
    for i in range(6):
        area_new = area.copy()
        c_min = min(area.keys())
        c_max = max(area.keys())
        # for x in range(c_min[0]-5, c_max[0]+5,1):
        #     for y in range(c_min[1] - 5, c_max[1] + 5,1):
        #         for z in range(c_min[2] - 5, c_max[2] + 5, 1):
        for x in range(-10, 25, 1):
            for y in range(-10, 25, 1):
                for z in range(-10, 25, 1):
                    coords  = x, y, z
                    neighbors = num_adjacent_occupied(coords, area)
                    if coords not in area:
                        area[coords] = '.'
                    try:
                        if area[coords] == '#':
                            if neighbors not in [2,3]:
                                area_new[coords] = '.'
                        elif area[coords] == '.' and neighbors == 3:
                            area_new[coords] = '#'
                    except KeyError:
                        pass
        area = area_new.copy()
    return list(area.values()).count('#')


if __name__ == '__main__':
    puzzle_input = parse_input('day_17.in')
    sample_input = parse_input('day_17.in.sample')

    # Part 1
    print(run_simulation(sample_input))
    print(run_simulation(puzzle_input))

    # Part 2
    # assert run_simulation(sample_input, 5, num_visibly_occupied) == 26
    # print(run_simulation(puzzle_input, 5, num_visibly_occupied))
