def never_decreases(password):
    p = [int(i) for i in str(password)]
    for n in range(len(p) - 1):
        if p[n] > p[n + 1]:
            return False
    return True


def adjacent_digits(password):
    p = [int(i) for i in str(password)]
    adjacent = False
    for n in range(len(p) - 1):
        if p[n] == p[n + 1]:
            adjacent = True
    return adjacent


def contains_double(password):
    dub_dict = {}
    for s in str(password):
        dub_dict[s] = dub_dict.get(s, 0) + 1
    for key, value in dub_dict.items():
        if value == 2:
            return True
    return False


def is_valid_password_v1(password):
    if not never_decreases(password):
        return False
    if not adjacent_digits(password):
        return False
    return True


def is_valid_password_v2(password):
    if not never_decreases(password):
        return False
    if not adjacent_digits(password):
        return False
    if not contains_double(password):
        return False
    return True


def find_valid_passwords(rng, f=is_valid_password_v1):
    valid_passwords = []
    for i in range(rng[0], rng[1] + 1):
        if f(i):
            valid_passwords.append(i)
    return valid_passwords


if __name__ == '__main__':
    puzzle_input = (246515, 739105)

    # Part 1
    assert is_valid_password_v1(111111) is True
    assert is_valid_password_v1(223450) is False
    assert is_valid_password_v1(123789) is False

    print(len(find_valid_passwords(puzzle_input)))

    # Part 2
    assert is_valid_password_v2(112233) is True
    assert is_valid_password_v2(123444) is False
    assert is_valid_password_v2(111122) is True

    print(len(find_valid_passwords(puzzle_input, is_valid_password_v2)))
