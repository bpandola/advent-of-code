import sys
dirs = ['e', 'w', 'se', 'sw', 'nw', 'ne']
deltas = {
        'e': (2, 0),
        'w': (-2, 0),
        'se': (1, 2),
        'sw': (-1, 2),
        'ne': (1, -2),
        'nw': (-1, -2)
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
        x, y = 0, 0
        for move in parsed_cmd:
            dx, dy = deltas[move]
            x += dx
            y += dy
        if (x, y) in tiles:
            tiles[(x, y)] = 'black' if tiles[(x, y)] == 'white' else 'white'
        else:
            tiles[(x, y)] = 'black'

    return tiles

def get_min_max(d):
    min_x, max_x = sys.maxsize, -sys.maxsize
    min_y, max_y = sys.maxsize, -sys.maxsize
    for coords, color in d.items():
        if color != 'black':
            continue
        x, y = coords
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        min_y = min(x, min_y)
        max_y = max(x, max_y)
    return min_x -2, min_y -1, max_x + 2, max_y+2


def run_simulation(tiles, num_days):
    floor = tiles.copy()

    def adjacent_counts(coords):
        count_white = 0
        for d in dirs:
            x, y = coords
            dx, dy = deltas[d]
            x += dx
            y+=dy
            try:
                color = floor[(x,y)]
            except KeyError:
                color = 'white'
            count_white += 1 if color == 'white' else 0
        return count_white, 6 - count_white


    for i in range(num_days):
        floor_new = floor.copy()
        min_x, min_y, max_x, max_y = get_min_max(floor)
        for x in range(min_x, max_x+1):
            for y in range(min_y, max_y+1):
                coords = (x,y)
                white,black =adjacent_counts(coords)
                try:
                    color = floor[(x,y)]
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

    # dirs = ['e', 'w', 'se', 'sw',  'nw', 'ne']
    # deltas = {
    #     'e': (2,0),
    #     'w': (-2,0),
    #     'se': (1,2),
    #     'sw': (-1,2),
    #     'ne': (1, -2),
    #     'nw': (-1, -2)
    # }
    # tiles = {}
    #
    # for cmd in puzzle_input:
    #     parsed_cmd = []
    #     acc = 0
    #     while acc < len(cmd):
    #         for d in dirs:
    #             if cmd[acc:].startswith(d):
    #                 parsed_cmd.append(d)
    #                 acc += len(d)
    #     x, y = 0, 0
    #     for move in parsed_cmd:
    #         dx, dy = deltas[move]
    #         x+=dx
    #         y+=dy
    #     if (x,y) in tiles:
    #         tiles[(x,y)] = 'black' if tiles[(x,y)] == 'white' else 'white'
    #     else:
    #         tiles[(x,y)] = 'black'
    #
    # print(len([v for v in tiles.values() if v == 'black']))
