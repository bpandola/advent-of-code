import hashlib


def print_password_progress(password, pad_digits=0, end=None):
    _end = '' if end is None else end
    _padding = ''.join(['_' for _ in range(pad_digits - len(password))])
    print('\r' + password + _padding, end=_end)


def get_first_door_password(secret, prefix, num_digits, display_progress=False):
    password = ''
    i = 1
    while len(password) != num_digits:
        result = hashlib.md5((secret + str(i)).encode()).hexdigest()
        if result.startswith(prefix):
            password += str(result)[5:6]
            if display_progress:
                print_password_progress(password, num_digits)
        i += 1
    if display_progress:
        print_password_progress(password, end='\n')
    return password


def get_second_door_password(secret, prefix, num_digits, display_progress=False):
    password = ['_' for _ in range(num_digits)]
    i = 1
    while '_' in password:
        result = hashlib.md5((secret + str(i)).encode()).hexdigest()
        if result.startswith(prefix):
            try:
                index = int(str(result)[5:6])
                if index < num_digits and password[index] == '_':
                    password[index] = str(result)[6:7]
            except ValueError:
                pass
            if display_progress:
                print_password_progress(''.join(password))
        i += 1
    if display_progress:
        print_password_progress(''.join(password), end='\n')
    return ''.join(password)


if __name__ == '__main__':
    puzzle_input = open('day_05.in').read().strip()

    # Part 1
    assert get_first_door_password('abc', '00000', 8) == '18f47a30'

    get_first_door_password(puzzle_input, '00000', 8, display_progress=True)

    # Part 2
    assert get_second_door_password('abc', '00000', 8) == '05ace8e3'

    get_second_door_password(puzzle_input, '00000', 8, display_progress=True)
