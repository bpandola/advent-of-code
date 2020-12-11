def parse_input(filename):
    lines = open(filename).read().split('\n')
    translated = {}
    for y, line in enumerate(lines):
        for x, data in enumerate(lines[y]):
            translated[(x, y)] = data
    return translated


dirs = [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0)]


def num_adjacent_occupied(coords, area):
    occupied = 0
    x, y = coords
    for dx, dy in dirs:
        try:
            if area[(x + dx, y + dy)] == '#':
                occupied += 1
        except KeyError:
            pass  # Out of bounds.
    return occupied


def num_visibly_occupied(coords, area):
    occupied = 0
    x, y = coords
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
                break  # Out of bounds.
    return occupied


def run_simulation(area_map, occupied_threshold, num_occupied):
    area = area_map.copy()
    while True:
        area_new = area.copy()
        for coords in list(area.keys()):
            if area[coords] == 'L' and num_occupied(coords, area) == 0:
                area_new[coords] = '#'
            elif area[coords] == '#' and num_occupied(coords, area) >= occupied_threshold:
                area_new[coords] = 'L'
        if area_new == area:
            break
        area = area_new.copy()
    return list(area.values()).count('#')


if __name__ == '__main__':
    puzzle_input = parse_input('day_11.in')
    sample_input = parse_input('day_11.in.sample')

    # Part 1
    assert run_simulation(sample_input, 4, num_adjacent_occupied) == 37
    print(run_simulation(puzzle_input, 4, num_adjacent_occupied))

    # Part 2
    assert run_simulation(sample_input, 5, num_visibly_occupied) == 26
    print(run_simulation(puzzle_input, 5, num_visibly_occupied))
