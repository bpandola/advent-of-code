import hashlib


def calculate_lowest_hash_input_to_get_prefix(secret, prefix):
    i = 1
    while True:
        result = hashlib.md5((secret + str(i)).encode()).hexdigest()
        if result.startswith(prefix):
            break
        i += 1
    return i


if __name__ == '__main__':
    puzzle_input = open('day_04.in').read()

    # Part 1
    assert calculate_lowest_hash_input_to_get_prefix('abcdef', '00000') == 609043
    assert calculate_lowest_hash_input_to_get_prefix('pqrstuv', '00000') == 1048970

    print(calculate_lowest_hash_input_to_get_prefix(puzzle_input, '00000'))

    # Part 2
    print(calculate_lowest_hash_input_to_get_prefix(puzzle_input, '000000'))
