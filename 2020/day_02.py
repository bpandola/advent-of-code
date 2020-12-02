from collections import namedtuple

Password = namedtuple('Password', 'characters char low high')


def parse_input(lines):
    passwords = []
    for line in lines:
        policy, password = line.split(': ')
        policy_range, letter = policy.split(' ')
        min_range, max_range = policy_range.split('-')
        passwords.append(
            Password(
                characters=password,
                char=letter,
                high=int(max_range.strip()),
                low=int(min_range.strip())
            )
        )
    return passwords


def predicate_part_1(password):
    return password.low <= password.characters.count(password.char) <= password.high


def predicate_part_2(password):
    char_in_position_low = password.characters[password.low - 1] == password.char
    char_in_position_high = password.characters[password.high - 1] == password.char
    return int(char_in_position_low) ^ int(char_in_position_high)


def valid_passwords(passwords, predicate):
    return list(filter(predicate, passwords))


if __name__ == '__main__':
    puzzle_input = [i for i in open('day_02.in').read().split('\n')]
    sample_input = [
        '1-3 a: abcde',
        '1-3 b: cdefg',
        '2-9 c: ccccccccc',
    ]
    puzzle_passwords = parse_input(puzzle_input)
    sample_passwords = parse_input(sample_input)

    # Part 1
    assert len(valid_passwords(sample_passwords, predicate_part_1)) == 2
    print(len(valid_passwords(puzzle_passwords, predicate_part_1)))

    # Part 2
    assert len(valid_passwords(sample_passwords, predicate_part_2)) == 1
    print(len(valid_passwords(puzzle_passwords, predicate_part_2)))
