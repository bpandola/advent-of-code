
dirs = ['e', 'w', 'se', 'sw', 'nw', 'ne']
deltas = {
        'e': (1, -1, 0),
        'w': (-1,  1, 0),
        'se': (0, -1, 1),
        'sw': (-1, 0, 1),
        'ne': (1, 0, -1),
        'nw': (0, 1, -1)
    }
def lay_floor(instructions):

    tiles = {}

    for cmd in instructions:
        parsed_cmd = []
        acc = 0
        while acc < len(cmd):
            for d in dirs:
                if cmd[acc:].startswith(d):
                    parsed_cmd.append(d)
                    acc += len(d)
        x, y,  z = 0, 0, 0
        for move in parsed_cmd:
            dx, dy, dz = deltas[move]
            x += dx
            y += dy
            z += dz
        coords = (x, y, z)
        if coords in tiles:
            tiles[coords] = 'black' if tiles[coords] == 'white' else 'white'
        else:
            tiles[coords] = 'black'

    return tiles

def get_coords_to_check(d):
    to_check = set()
    for coords, color in d.items():
        if color != 'black':
            continue
        to_check.add(coords)
        for adj_coords in get_adjacent_coords(coords):
            to_check.add(adj_coords)
    return to_check

def get_adjacent_coords(coords):
    adj = set()
    for d in dirs:
        x, y, z = coords
        dx, dy, dz = deltas[d]
        x += dx
        y+=dy
        z+=dz
        adj.add((x,y,z))
    return adj


def adjacent_counts(pos, floor):
    count_white = 0
    for d in dirs:
        x, y, z = pos
        dx, dy, dz = deltas[d]
        x += dx
        y+=dy
        z+=dz
        try:
            c = floor[(x,y, z)]
        except KeyError:
            c = 'white'
        count_white += 1 if c == 'white' else 0
    return count_white, 6 - count_white

def run_simulation(tiles, num_days):
    floor = tiles.copy()




    for i in range(num_days):
        floor_new = floor.copy()

        for coords in get_coords_to_check(floor):
            white,black =adjacent_counts(coords, floor)
            try:
                color = floor[coords]
            except  KeyError:
                color ='white'
            if color == 'white' and black == 2:
                floor_new[coords] = 'black'
            else:
                if black == 0 or black > 2:
                    floor_new[coords] = 'white'
        floor = floor_new.copy()
        print(len([color for color in floor.values() if color == 'black']))
    return floor









if __name__ == '__main__':
    puzzle_input = open('day_24.in').read().split('\n')
    sample_input = open('day_24.in.sample').read().split('\n')

    # Part 1
    sample_floor = lay_floor(sample_input)
    assert len([color for color in sample_floor.values() if color == 'black']) == 10

    puzzle_floor = lay_floor(puzzle_input)
    print(len([color for color in puzzle_floor.values() if color == 'black']))

    # Part 2
    sample_floor = run_simulation(sample_floor, 100)
    assert len([color for color in sample_floor.values() if color == 'black']) == 2208

    puzzle_floor = run_simulation(puzzle_floor, 100)
    print(len([color for color in puzzle_floor.values() if color == 'black']))
