DIRECTION_FROM_TURN = {
    'N': {'L': 'W', 'R': 'E'},
    'S': {'L': 'E', 'R': 'W'},
    'W': {'L': 'S', 'R': 'N'},
    'E': {'L': 'N', 'R': 'S'},
}
DX = {'N': 0, 'S': 0, 'W': -1, 'E': 1}
DY = {'N': -1, 'S': 1, 'W': 0, 'E': 0}


def generate_path(instructions):
    direction = 'N'
    x, y = 0, 0
    path = [(x, y)]
    for i in instructions:
        turn = i[0]
        move = int(i[1:])
        direction = DIRECTION_FROM_TURN[direction].get(turn)
        for m in range(move):
            x += DX[direction]
            y += DY[direction]
            path.append((x, y))
    return path


def calculate_manhattan_distance(xy):
    x, y = xy
    return abs(x) + abs(y)


def find_easter_bunny_hq(path):
    intersections = {}
    for intersection in path:
        if intersection in intersections:
            return intersection
        intersections[intersection] = True


if __name__ == '__main__':
    puzzle_input = [str(i).strip() for i in open('day_01.in').read().split(',')]

    # Part 1
    assert calculate_manhattan_distance(generate_path(['R2', 'L3'])[-1]) == 5
    assert calculate_manhattan_distance(generate_path(['R2', 'R2', 'R2'])[-1]) == 2
    assert calculate_manhattan_distance(generate_path(['R5', 'L5', 'R5', 'R3'])[-1]) == 12

    steps = generate_path(puzzle_input)
    print(calculate_manhattan_distance(steps[-1]))

    # Part 2
    assert calculate_manhattan_distance(find_easter_bunny_hq(generate_path(['R8', 'R4', 'R4', 'R8']))) == 4

    print(calculate_manhattan_distance(find_easter_bunny_hq(steps)))
