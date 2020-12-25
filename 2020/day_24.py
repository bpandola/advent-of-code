DIRS = ['e', 'w', 'se', 'sw', 'nw', 'ne']
DIRS_TO_DELTAS = {
    'e': (1, -1, 0),
    'w': (-1, 1, 0),
    'se': (0, -1, 1),
    'sw': (-1, 0, 1),
    'ne': (1, 0, -1),
    'nw': (0, 1, -1),
}


def lay_floor(instructions):
    tiles = {}
    for cmd in instructions:
        parsed_cmd = []
        acc = 0
        while acc < len(cmd):
            for d in DIRS:
                if cmd[acc:].startswith(d):
                    parsed_cmd.append(d)
                    acc += len(d)
        x, y, z = 0, 0, 0
        for move in parsed_cmd:
            dx, dy, dz = DIRS_TO_DELTAS[move]
            x += dx
            y += dy
            z += dz
        coords = (x, y, z)
        if coords in tiles:
            tiles[coords] = True if not tiles[coords] else False
        else:
            tiles[coords] = True
    return tiles


def get_adjacent_coords(coords):
    adj = set()
    for d in DIRS:
        x, y, z = coords
        dx, dy, dz = DIRS_TO_DELTAS[d]
        x += dx
        y += dy
        z += dz
        adj.add((x, y, z))
    return adj


def get_coords_to_check(floor):
    coords_to_check = set()
    for coords, color in floor.items():
        if not color:
            continue
        coords_to_check.add(coords)
        for coords_adj in get_adjacent_coords(coords):
            coords_to_check.add(coords_adj)
    return coords_to_check


def adjacent_counts(floor, coords):
    color_count = 0
    for coords_adj in get_adjacent_coords(coords):
        try:
            c = floor[coords_adj]
        except KeyError:
            c = False
        color_count += 1 if c else 0
    return color_count, 6 - color_count


def run_simulation(tiles, num_days):
    floor = tiles.copy()
    for i in range(num_days):
        floor_new = floor.copy()
        for coords in get_coords_to_check(floor):
            num_black, num_white = adjacent_counts(floor, coords)
            try:
                color = floor[coords]
            except KeyError:
                color = False
            if not color and num_black == 2:
                floor_new[coords] = True
            else:
                if num_black == 0 or num_black > 2:
                    floor_new[coords] = False
        floor = floor_new.copy()
    return floor


if __name__ == '__main__':
    puzzle_input = open('day_24.in').read().split('\n')
    sample_input = open('day_24.in.sample').read().split('\n')

    # Part 1
    sample_floor = lay_floor(sample_input)
    assert list(sample_floor.values()).count(True) == 10

    puzzle_floor = lay_floor(puzzle_input)
    print(list(puzzle_floor.values()).count(True))

    # Part 2
    sample_floor = run_simulation(sample_floor, 100)
    assert list(sample_floor.values()).count(True) == 2208

    puzzle_floor = run_simulation(puzzle_floor, 100)
    print(list(puzzle_floor.values()).count(True))
