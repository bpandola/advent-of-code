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




def dfs(graph, doors, keys, path, viable_routes=None):
    viable_routes = viable_routes or []
    def get_viable_moves(steps):
        moves = []
        possible_moves = []
        px, py = steps[-1]
        if graph[(px - 1, py)] != '#':
            possible_moves.append((px - 1, py))
        if graph[(px + 1, py)] != '#':
            possible_moves.append((px + 1, py))
        if graph[(px, py - 1)] != '#':
            possible_moves.append((px, py - 1))
        if graph[(px, py + 1)] != '#':
            possible_moves.append((px, py + 1))
        for move in possible_moves:
            if len(steps) > 1 and move == steps[-2]:
                if graph[steps[-1]] in string.ascii_lowercase:
                    if steps.count(steps[-1]) == 1:
                        # continue  # no backtracking unless we're standing on a key/door for first time
                        if set(keys.values()) - set(steps):
                            moves.append(move)
            elif graph[move] in string.ascii_uppercase:
                key = str(graph[move]).lower()
                key_pos = keys[key]
                if key_pos in steps:
                    moves.append(move)
            else:
                # Free spot or key
                moves.append(move)
        return moves

    moves = get_viable_moves(path)
    while len(moves) == 1:
        path += moves
        moves = get_viable_moves(path)
    # moves = []
    shortest = min([len(p) for p in viable_routes]) if viable_routes else 65536
    if len(path) > shortest:
        moves = [] # get_viable_moves(path)
    new_path = None
    if not moves:
        if not set(keys.values()) - set(path):

            if shortest >= len(path):
                viable_routes.append(path)
    for move in moves:
        # print(move)
        new_path = path[:] + [move]
        viable_routes = dfs(graph, doors, keys, new_path, viable_routes)

    return viable_routes

def find_shortest_path(data):
    translated, start_coords, doors, keys = translate_input(data)
    path = [start_coords]
    viable_paths = dfs(translated, doors, keys, path)

    shortest = min([len(p) for p in viable_paths])

    return shortest - 1


def dfs_shortest_path(data):
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

    sample_0 = [
        '######',
        '#bA@a#',
        '######',
    ]
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
    assert find_shortest_path(sample_0) == 4
    assert find_shortest_path(sample_1) == 86
    assert find_shortest_path(sample_2) == 132
    #assert find_shortest_path(sample_3) == 136
    assert find_shortest_path(sample_4) == 81

    #print(find_shortest_path(puzzle_input))
