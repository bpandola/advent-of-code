def parse_input(filename):
    keys = open(filename).read().split('\n')
    return int(keys[0]), int(keys[1])


def transform(subject_number, value=1, loop_size=1):
    transformed = value
    for _ in range(loop_size):
        transformed *= subject_number
        transformed = transformed % 20201227
    return transformed


def calc_loop_size(public_key, subject_number):
    loop_size = 0
    value = 1
    while value != public_key:
        value = transform(subject_number, value, loop_size=1)
        loop_size += 1
    return loop_size


def calc_encryption_key(public_keys):
    card_pk, door_pk = public_keys
    card_loop_size = calc_loop_size(card_pk, 7)
    door_loop_size = calc_loop_size(door_pk, 7)
    card_encryption = transform(door_pk, loop_size=card_loop_size)
    door_encryption = transform(card_pk, loop_size=door_loop_size)
    assert card_encryption == door_encryption
    return card_encryption


if __name__ == '__main__':
    puzzle_input = parse_input('day_25.in')
    sample_input = parse_input('day_25.in.sample')

    assert calc_loop_size(sample_input[0], 7) == 8
    assert calc_loop_size(sample_input[1], 7) == 11
    assert calc_encryption_key(sample_input) == 14897079

    print(calc_encryption_key(puzzle_input))
