DX = {'<': -1, '^': 0, '>': 1, 'v': 0}
DY = {'<': 0, '^': 1, '>': 0, 'v': -1}


def calculate_houses_visited(directions):
    x, y = 0, 0
    locations = [(x, y)]
    for d in directions:
        x += DX[d]
        y += DY[d]
        locations.append((x, y))
    return locations


def calculate_houses_visited_with_robot(directions):
    x_santa, y_santa, x_robot, y_robot = 0, 0, 0, 0
    locations = [(x_santa, y_santa), (x_robot, y_robot)]
    santa_turn = 1
    for d in directions:
        if santa_turn:
            x_santa += DX[d]
            y_santa += DY[d]
            locations.append((x_santa, y_santa))
        else:
            x_robot += DX[d]
            y_robot += DY[d]
            locations.append((x_robot, y_robot))
        santa_turn ^= 1
    return locations


if __name__ == '__main__':
    puzzle_input = open('day_3.in').read()

    # Part 1
    assert len(set(calculate_houses_visited('>'))) == 2
    assert len(set(calculate_houses_visited('^>v<'))) == 4
    assert len(set(calculate_houses_visited('^v^v^v^v^v'))) == 2

    print len(set(calculate_houses_visited(puzzle_input)))

    # Part 2
    assert len(set(calculate_houses_visited_with_robot('^v'))) == 3
    assert len(set(calculate_houses_visited_with_robot('^>v<'))) == 3
    assert len(set(calculate_houses_visited_with_robot('^v^v^v^v^v'))) == 11

    print len(set(calculate_houses_visited_with_robot(puzzle_input)))
