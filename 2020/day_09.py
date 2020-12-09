def is_valid_xmas_number(number, preamble):
    for i in range(len(preamble)):
        for j in range(i + 1, len(preamble)):
            if preamble[i] + preamble[j] == number:
                return True
    return False


def find_secret_xmas_number(numbers, preamble_length=25):
    for i, number in enumerate(numbers):
        if i < preamble_length:
            continue
        preamble = numbers[i - preamble_length:i]
        if not is_valid_xmas_number(number, preamble):
            return number
    raise RuntimeError('Could not find secret number!')


def find_encryption_weakness(numbers, secret_number):
    start, end = 0, 1
    window_sum = 0
    while window_sum != secret_number:
        window = numbers[start:end]
        window_sum = sum(window)
        if window_sum == secret_number:
            return min(window) + max(window)
        if window_sum > secret_number:
            start += 1
        if window_sum < secret_number:
            end += 1
    raise RuntimeError('Could not find encryption weakness!')


if __name__ == '__main__':
    puzzle_input = [int(line) for line in open('day_09.in').read().split('\n')]
    sample_input = [int(line) for line in open('day_09.in.sample').read().split('\n')]

    # Part 1
    sample_secret_number = find_secret_xmas_number(sample_input, preamble_length=5)
    assert sample_secret_number == 127
    puzzle_secret_number = find_secret_xmas_number(puzzle_input, preamble_length=25)
    print(puzzle_secret_number)

    # Part 2
    assert find_encryption_weakness(sample_input, sample_secret_number) == 62
    print(find_encryption_weakness(puzzle_input, puzzle_secret_number))
