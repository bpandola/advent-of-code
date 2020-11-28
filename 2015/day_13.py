from collections import defaultdict


def build_graph(data):
    nodes = []
    edges = defaultdict(int)
    for line in data.split('\n'):
        line = line.strip()
        tokens = line.split(' ')
        left = tokens[0]
        sign = tokens[2]
        units = int(tokens[3])
        right = tokens[10][:-1]
        nodes.append(left)
        nodes.append(right)
        value = units * (-1 if sign == 'lose' else 1)
        edges[(left, right)] += value
        edges[(right, left)] += value
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


def generate_seating(nodes, edges):
    order = ''
    max_value = 0
    for combination in generate_permutations(nodes):
        combination.append(combination[0])  # Complete circle around table
        value = 0
        seating_order = ''
        for index, name in enumerate(combination):
            if index == 0:
                seating_order += name
            else:
                seating_order += ' -> ' + name
                value += edges[(combination[index - 1], name)]
        if value > max_value:
            order = seating_order
            max_value = value
    return order, max_value


if __name__ == '__main__':
    puzzle_input = open('day_13.in').read().strip()

    # Part 1
    sample_input = """Alice would gain 54 happiness units by sitting next to Bob.
        Alice would lose 79 happiness units by sitting next to Carol.
        Alice would lose 2 happiness units by sitting next to David.
        Bob would gain 83 happiness units by sitting next to Alice.
        Bob would lose 7 happiness units by sitting next to Carol.
        Bob would lose 63 happiness units by sitting next to David.
        Carol would lose 62 happiness units by sitting next to Alice.
        Carol would gain 60 happiness units by sitting next to Bob.
        Carol would gain 55 happiness units by sitting next to David.
        David would gain 46 happiness units by sitting next to Alice.
        David would lose 7 happiness units by sitting next to Bob.
        David would gain 41 happiness units by sitting next to Carol."""
    attendees, happiness = build_graph(sample_input)
    _, max_happiness = generate_seating(attendees, happiness)
    assert max_happiness == 330

    attendees, happiness = build_graph(puzzle_input)
    seating, max_happiness = generate_seating(attendees, happiness)

    print(seating, max_happiness)

    # Part 2
    for name in attendees:
        happiness[('Me', name)] = happiness[(name, 'Me')] = 0
    attendees.append('Me')

    seating, max_happiness = generate_seating(attendees, happiness)

    print(seating, max_happiness)
