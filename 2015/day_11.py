import string


def is_valid_password(password):
    # Passwords may not contain the letters i, o, or l, as these letters
    # can be mistaken for other characters and are therefore confusing.
    for invalid_character in ['i', 'o', 'l']:
        if invalid_character in password:
            return False
    # Passwords must include one increasing straight of at least three
    # letters, like abc, bcd, cde, and so on, up to xyz. They cannot
    # skip letters; abd doesn't count.
    for i in range(len(password) - 2):
        if password[i:i + 3] in string.ascii_lowercase:
            break
    else:
        return False
    # Passwords must contain at least two different, non-overlapping
    # pairs of letters, like aa, bb, or zz.
    pair_count = 0
    last_pair_index = -1
    for i in range(1, len(password)):
        if password[i] == password[i - 1] and i - 1 != last_pair_index:
            pair_count += 1
            last_pair_index = i
        if pair_count >= 2:
            break
    else:
        return False
    return True


def increment_password(password):
    password_incremented = [c for c in password]
    next_character = string.ascii_lowercase + 'a'
    index = len(password) - 1
    while index:
        next_character_index = string.ascii_lowercase.index(password[index]) + 1
        incremented_character = next_character[next_character_index]
        password_incremented[index] = incremented_character
        if password_incremented[index] != 'a':
            break
        index -= 1
    return ''.join(password_incremented)


def rotate_password(password, display=False):
    new_password = password
    while True:
        new_password = increment_password(new_password)
        if display:
            print(f'\r{new_password}', end='')
        if is_valid_password(new_password):
            break
    if display:
        print(f'\r{new_password}', end='\n')
    return new_password


if __name__ == '__main__':
    puzzle_input = open('day_11.in').read().strip()

    # Part 1
    assert (is_valid_password('hijklmmn')) is False
    assert (is_valid_password('abbceffg')) is False
    assert (is_valid_password('abbcegjk')) is False

    # assert rotate_password('abcdefgh') == 'abcdffaa'
    # assert rotate_password('ghijklmn') == 'ghjaabcc'

    rotated_password = rotate_password(puzzle_input, display=True)

    # Part 2
    rotate_password(rotated_password, display=True)
