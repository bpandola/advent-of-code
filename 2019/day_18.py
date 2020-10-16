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
    poi = {'ROOT': fill_area_with_oxygen(translated, start_coords)}
    for key, coords in keys.items():
        poi[key] = fill_area_with_oxygen(translated, coords)
    for key, coords in doors.items():
        poi[key] = fill_area_with_oxygen(translated, coords)
    return translated, poi, start_coords, keys, doors


class Graph:
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        #self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        #self.weights[(to_node, from_node)] = weight


def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return None
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

def poi_manips(poi, keys, doors):
    key_to_key = {}
    graph = Graph()
    for node, adjacent_nodes in poi.items():
        for adjacent_node, distance in adjacent_nodes:
            graph.add_edge(node, adjacent_node, distance)

    for key_start in list(keys) + ['ROOT']:
        for key_end in keys:
            if key_start == key_end:
                continue
            path = dijsktra(graph, key_start, key_end)
            key_to_key[(key_start, key_end)] = path


    return graph


def poi_to_route(poi):
    num_keys = len([key for key in poi.keys() if key in string.ascii_lowercase])


    routes = [[('ROOT',0)]]

    key_routes = []
    while routes:
        routes_copy = routes[:]
        routes = []
        for route in routes_copy:
            start = route[-1]
            moves = poi[start[0]]  #get_viable_moves(start)
            # If there were no moves, we hit a dead end.
            for move in moves:
                node = move[0]
                if len(route) > 1 and node == route[-2][0]:
                    if list([node for node, _ in route]).count(route[-1][0]) > 1:
                        continue  # no backtracking unless we're standing on a key/door for first time

                    # if node in string.ascii_lowercase and route[-1][0] in string.ascii_uppercase:
                    #     continue  # no backtracking from a door to a previous key
                    # elif node in string.ascii_uppercase and route[-1][0] in string.ascii_lowercase:
                    #     if list([node for node, _ in route]).count(route[-1][0]) > 1:
                    #         continue  # no backtracking from a key if we've already picked it up.
                elif node in string.ascii_lowercase:
                    keys_acquired = set([key for key, _ in route if key in string.ascii_lowercase])
                    keys_acquired.add(node)
                    route_keys = len(keys_acquired)
                    if route_keys == num_keys:
                        key_routes.append(route + [move])
                        continue
                elif node in string.ascii_uppercase:
                    if node.lower() not in [key for key, _ in route]:
                        continue
                routes.append(route + [move])

    return key_routes


def fill_area_with_oxygen(area_map, start_coords):
    area = area_map.copy()
    step = 1
    spread_points = [start_coords]
    area[start_coords] = '#'
    poi = []
    while spread_points:
        spread_points_new = []
        for x, y in spread_points:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                data = area[(x + dx ,y + dy)]
                if data == '.':
                    spread_points_new.append((x + dx, y + dy))
                    area[(x + dx, y + dy)] = '#'
                elif data in string.ascii_letters:
                    poi.append((data, step))
                    area[(x + dx, y + dy)] = '#'

        spread_points = spread_points_new
        step += 1

    return poi


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

def dfs_shortest_path(data):
    translated, start_coords, doors, keys = translate_input(data)
    path = [start_coords]
    viable_paths = dfs(translated, doors, keys, path)

    shortest = min([len(p) for p in viable_paths])

    return shortest - 1


def find_shortest_path(data):
    translated, poi, start_coords, keys, doors = translate_input(data)
    poi = poi_manips(poi, keys, doors)
    key_routes = poi_to_route(poi)
    shortest = min([sum([step[1] for step in route]) for route in key_routes])
    return shortest



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
    #assert find_shortest_path(sample_0) == 4
    #assert find_shortest_path(sample_1) == 86
    #assert find_shortest_path(sample_2) == 132
    assert find_shortest_path(sample_3) == 136
    assert find_shortest_path(sample_4) == 81

    print(find_shortest_path(puzzle_input))
