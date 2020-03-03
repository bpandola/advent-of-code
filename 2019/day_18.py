from collections import defaultdict
import string

def translate_input(data):
    # Translate into a more convenient data structure.
    # defaultdict[(x, y)] = data; default is '.'
    translated = defaultdict(lambda: '.')
    start_coords = (0, 0)
    doors = {}
    keys = {}
    for y, line in enumerate(data):
        for x, c in enumerate(data[y]):
            if c == '@':
                start_coords = (x, y)
            elif c == '#':
                translated[(x, y)] = c
            elif c in string.ascii_letters:
                translated[(x, y)] = c
                if c in string.ascii_uppercase:
                    doors[c] = (x, y)
                elif c in string.ascii_lowercase:
                    keys[c] = (x, y)
    return translated, start_coords, doors, keys


def get_viable_routes(area, pos, keys, routes=None):

    x, y = pos
    routes = routes or [[(x,y)]]
    def get_viable_moves(p):
        moves = []
        px, py = p
        if area[(px-1, py)] != '#':
            moves.append((px-1, py))
        if area[(px+1, py)] != '#':
            moves.append((px+1, py))
        if area[(px, py-1)] != '#':
            moves.append((px, py-1))
        if area[(px, py+1)] != '#':
            moves.append((px, py+1))
        return moves
    key_routes = []
    while routes:
        print(len(routes))
        routes_copy = routes[:]
        routes = []
        for route in routes_copy:
            start = route[-1]
            moves = get_viable_moves(start)
            # If there were no moves, we hit a dead end.
            for move in moves:
                if len(route) > 1 and move == route[-2]:
                    if area[route[-1]] in string.ascii_lowercase:
                        if route.count(route[-1]) == 1:
                            #continue  # no backtracking unless we're standing on a key/door for first time
                            routes.append(route + [move])
                elif area[move] in string.ascii_lowercase:
                    if move in route:
                        routes.append(route + [move])
                        continue
                    key_routes.append(route + [move])
                elif area[move] in string.ascii_uppercase:
                    key = str(area[move]).lower()
                    key_pos = keys[key]
                    if key_pos not in route:
                        continue
                    routes.append(route + [move])
                elif area[move] == '.':
                    routes.append(route + [move])
    return key_routes


def find_shortest_path(data):
    translated, start_coords, doors, keys = translate_input(data)
    paths = []
    key_routes = get_viable_routes(translated, start_coords, keys)
    while key_routes:
        paths = key_routes
        key_routes = get_viable_routes(translated, start_coords, keys, key_routes)
    shortest = min([len(p) for p in paths])
    return shortest - 1





if __name__ == '__main__':
    puzzle_input = [line for line in open('day_18.in').read().split('\n')]

    for line in puzzle_input:
        print(line)

    sample_1 = [
        '########################',
        '#f.D.E.e.C.b.A.@.a.B.c.#',
        '######################.#',
        '#d.....................#',
        '########################',
    ]
    sample_2 = [
        '########################',
        '#...............b.C.D.f#',
        '#.######################',
        '#.....@.a.B.c.d.A.e.F.g#',
        '########################',
    ]
    sample_3 = [
        '#################',
        '#i.G..c...e..H.p#',
        '########.########',
        '#j.A..b...f..D.o#',
        '########@########',
        '#k.E..a...g..B.n#',
        '########.########',
        '#l.F..d...h..C.m#',
        '#################',
    ]
    sample_4 = [
        '########################',
        '#@..............ac.GI.b#',
        '###d#e#f################',
        '###A#B#C################',
        '###g#h#i################',
        '########################',
    ]
    # Part 1

    assert find_shortest_path(sample_1) == 86
    assert find_shortest_path(sample_2) == 132
    assert find_shortest_path(sample_3) == 136
    assert find_shortest_path(sample_4) == 81

    print(find_shortest_path(puzzle_input))
