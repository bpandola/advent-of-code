def build_direction_map(keypad_layout):
    coord_to_key = {}
    key_to_coord = {}
    y = 0
    for row in keypad_layout:
        x = 0
        for key in row:
            if key != ' ':
                coord_to_key[(x, y)] = key
                key_to_coord[key] = (x, y)
            x += 1
        y += 1
    direction_map = {}
    for key, location in key_to_coord.items():
        x, y = location
        direction_map[key] = {
            'L': coord_to_key.get((x - 1, y), key),
            'R': coord_to_key.get((x + 1, y), key),
            'U': coord_to_key.get((x, y - 1), key),
            'D': coord_to_key.get((x, y + 1), key),
        }
    return direction_map


def get_bathroom_code(instructions, keypad_layout, starting_key):
    direction_map = build_direction_map(keypad_layout)
    current_key = starting_key
    bathroom_code = ''
    for sequence in instructions:
        for direction in sequence:
            current_key = direction_map[current_key][direction]
        bathroom_code += current_key
    return bathroom_code


if __name__ == '__main__':
    puzzle_input = [str(i).strip() for i in open('day_02.in').read().split('\n')]

    sample_input = [
        'ULL',
        'RRDDD',
        'LURDL',
        'UUUUD',
    ]

    # Part 1
    keypad_1 = [
        '123',
        '456',
        '789',
    ]
    assert get_bathroom_code(sample_input, keypad_1, '5') == '1985'

    print(get_bathroom_code(puzzle_input, keypad_1, '5'))

    # Part 2
    keypad_2 = [
        '  1  ',
        ' 234 ',
        '56789',
        ' ABC ',
        '  D  ',
    ]
    assert get_bathroom_code(sample_input, keypad_2, '5') == '5DB3'

    print(get_bathroom_code(puzzle_input, keypad_2, '5'))
