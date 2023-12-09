def parse_input(filename):
    instructions, nodes_data = open(filename).read().split('\n\n')
    nodes = {}
    for node in nodes_data.split('\n'):
        name = node[0:3]
        left = node[7:10]
        right = node[12:15]
        nodes[name] = [left, right]
    return instructions, nodes


def calculate_steps(instructions, nodes, start='AAA', terminator='ZZZ'):
    ip, steps = 0, 0
    node = nodes[start]
    while True:
        steps += 1
        direction = instructions[ip]
        next_node_index = 0 if direction == 'L' else 1
        next_node = node[next_node_index]
        if next_node.endswith(terminator):
            break
        node = nodes[next_node]
        ip += 1
        if ip == len(instructions):
            ip = 0
    return steps


def calculate_simultaneous_steps(instructions, nodes):
    from math import lcm

    steps = []
    starting_nodes = [node for node in nodes if node.endswith('A')]
    for starting_node in starting_nodes:
        steps.append(
            calculate_steps(instructions, nodes, start=starting_node, terminator='Z')
        )
    return lcm(*steps)


if __name__ == '__main__':
    puzzle_input = parse_input('day_08.in')

    # Part 1
    sample_input = parse_input('day_08.in.sample_01')
    assert calculate_steps(sample_input[0], sample_input[1]) == 6
    print(calculate_steps(puzzle_input[0], puzzle_input[1]))

    # Part 2
    sample_input = parse_input('day_08.in.sample_02')
    assert calculate_simultaneous_steps(sample_input[0], sample_input[1]) == 6
    print(calculate_simultaneous_steps(puzzle_input[0], puzzle_input[1]))
