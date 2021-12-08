
def parse_input(filename):
    commands = open(filename).read().split('\n')
    commands_parsed = [
        (command.split(' ')[0], int(command.split(' ')[1]))
        for command in commands
    ]
    return commands_parsed


def calculate_position(commands):
    horizontal, depth = 0, 0
    for action, value in commands:
        if action == 'forward':
            horizontal += value
        elif action == 'down':
            depth += value
        elif action == 'up':
            depth -= value
    return horizontal * depth


def calculate_advanced_position(commands):
    horizontal, depth, aim = 0, 0, 0
    for action, value in commands:
        if action == 'forward':
            horizontal += value
            depth += (aim * value)
        elif action == 'down':
            aim += value
        elif action == 'up':
            aim -= value
    return horizontal * depth


if __name__ == '__main__':
    puzzle_input = parse_input('day_02.in')
    sample_input = parse_input('day_02.in.sample_01')

    # Part 1
    assert calculate_position(sample_input) == 150
    print(calculate_position(puzzle_input))

    # Part 2
    assert calculate_advanced_position(sample_input) == 900
    print(calculate_advanced_position(puzzle_input))
