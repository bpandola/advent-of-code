def build_graph(data):
    nodes = []
    edges = {}
    for d in data:
        a, _, b, __, dist = d.split()
        nodes.append(a)
        nodes.append(b)
        edges[(a, b)] = edges[(b, a)] = int(dist)
    return list(set(nodes)), edges


def generate_permutations(data):
    if len(data) == 0:
        return []
    if len(data) == 1:
        return [data]
    permutations = []
    for i in range(len(data)):
        m = data[i]
        remaining = data[:i] + data[i + 1:]
        for p in generate_permutations(remaining):
            permutations.append([m] + p)
    return permutations


def generate_paths(nodes, edges):
    paths = {}
    for combination in generate_permutations(nodes):
        distance = 0
        path = ''
        for index, dest in enumerate(combination):
            if index == 0:
                path += dest
            else:
                path += ' -> ' + dest
                distance += edges[(combination[index - 1], dest)]
        paths[path] = distance
    return paths


if __name__ == '__main__':
    puzzle_input = open('day_9.in').read().strip().split('\n')

    # Part 1
    sample_data = [
        'London to Dublin = 464',
        'London to Belfast = 518',
        'Dublin to Belfast = 141',
    ]
    graph = build_graph(sample_data)
    routes = generate_paths(graph[0], graph[1])
    print([(k, v) for k, v in routes.items() if v == min(routes.values())])
    assert min(routes.values()) == 605

    graph = build_graph(puzzle_input)
    routes = generate_paths(graph[0], graph[1])

    print([(k, v) for k, v in routes.items() if v == min(routes.values())])

    # Part 2
    print([(k, v) for k, v in routes.items() if v == max(routes.values())])
