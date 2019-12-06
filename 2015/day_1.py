

def follow_directions(directions, starting_floor=0):
    floor_on = starting_floor
    entered_basement_index = 0
    for index, direction in enumerate(directions):
        if direction == '(':
            floor_on += 1
        elif direction == ')':
            floor_on -= 1
        if floor_on == -1 and not entered_basement_index:
            entered_basement_index = index + 1
    return floor_on, entered_basement_index


def get_floor_on(directions, starting_floor=0):
    floor_on, _ = follow_directions(directions, starting_floor)
    return floor_on


def get_entered_basement_index(directions, starting_floor=0):
    _, entered_basement_index = follow_directions(directions, starting_floor)
    return entered_basement_index


if __name__ == '__main__':
    puzzle_input = open('day_1.in').read()
    # Part 1
    assert get_floor_on('(())') == get_floor_on('()()') == 0
    assert get_floor_on('(((') == get_floor_on('(()(()(') == 3
    assert get_floor_on('))(((((') == 3
    assert get_floor_on('())') == get_floor_on('))(') == -1
    assert get_floor_on(')))') == get_floor_on(')())())') == -3

    print get_floor_on(puzzle_input)

    # Part 2
    assert get_entered_basement_index(')') == 1
    assert get_entered_basement_index('()())') == 5

    print get_entered_basement_index(puzzle_input)
