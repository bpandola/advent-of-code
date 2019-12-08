def build_graph(data):
    graph = {}
    for orbit in data:
        left, right = orbit.split(')')
        graph[left] = graph.get(left, [])
        graph[left].append(right)
    return graph


def num_orbits(graph, key):
    count = 0
    for mass, satellites in graph.items():
        if key in satellites:
            count += 1
            count += num_orbits(graph, mass)
    return count


def get_all_objects(graph):
    objs = []
    for mass, satellites in graph.items():
        objs.append(mass)
        objs.extend(satellites)
    return set(objs)


def count_orbits(graph):
    count = 0
    objs = get_all_objects(graph)
    for o in objs:
        count += num_orbits(graph, o)
    return count


def get_mass(graph, satellite):
    for mass, satellites in graph.items():
        if satellite in satellites:
            return mass
    return None


def find_shortest_path(graph, start, end, path=None):
    path = (path if path else []) + [start]
    if start == end:
        return path
    shortest = None
    nodes = graph.get(start, []) + [get_mass(graph, start)]
    for node in nodes:
        if node not in path:
            new_path = find_shortest_path(graph, node, end, path)
            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path
    return shortest


def count_orbital_transfers(graph, o1, o2):
    path = find_shortest_path(graph, o1, o2)
    return len(path) - 3  # Subtract o1 and o2 and then off by one...


if __name__ == '__main__':
    puzzle_input = open('day_6.in').read().split('\n')

    # Part 1
    sample = [
        'COM)B',
        'B)C',
        'C)D',
        'D)E',
        'E)F',
        'B)G',
        'G)H',
        'D)I',
        'E)J',
        'J)K',
        'K)L',
    ]
    sample_graph = build_graph(sample)
    assert num_orbits(sample_graph, 'D') == 3
    assert num_orbits(sample_graph, 'L') == 7
    assert num_orbits(sample_graph, 'COM') == 0
    assert count_orbits(build_graph(sample)) == 42

    print(count_orbits(build_graph(puzzle_input)))

    # Part 2
    sample = [
        'COM)B',
        'B)C',
        'C)D',
        'D)E',
        'E)F',
        'B)G',
        'G)H',
        'D)I',
        'E)J',
        'J)K',
        'K)L',
        'K)YOU',
        'I)SAN',
    ]
    assert count_orbital_transfers(build_graph(sample), 'YOU', 'SAN') == 4

    print(count_orbital_transfers(build_graph(puzzle_input), 'YOU', 'SAN'))
