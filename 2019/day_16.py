def fft_pattern(digit_index, number_length):
    base_pattern = [0, 1, 0, -1]
    pattern_index = 0
    repeat = digit_index + 1
    index = 0
    while True:
        for _ in range(repeat):
            if index > number_length:
                return
            yield base_pattern[pattern_index]
            index += 1
        pattern_index += 1
        pattern_index &= 3


def fft(numbers):
    new_number = ''
    number_length = len(numbers)
    for j in range(number_length):
        pat = fft_pattern(j, number_length)
        next(pat)  # Burn the first one...
        value = 0
        for n in str(numbers):
            pattern = next(pat)
            if pattern < 0:
                value -= int(n)
            elif pattern > 0:
                value += int(n)
        new_number += str(value)[-1]
    return new_number


def calculate(number, phases, display=False):
    new_number = str(number)
    for i in range(phases):
        new_number = fft(new_number)
        if display:
            print(f'\r{new_number[:8]}', end='')
    if display:
        print(f'\r{new_number[:8]}', end='\n')
    return new_number[:8]


def calculate_special_case(number, phases, display=False):
    # This assumes that our input falls in the range where
    # a whole bunch of zeroes run up against a whole bunch
    # of ones.  Basically, the pattern for our first digit
    # is all ones and the last digit is all zeroes except
    # for a final one.  So we can basically sum up all the
    # numbers and then just subtract each position as we
    # go to get our output.
    new_number = str(number)
    for i in range(phases):
        s = sum([int(c) for c in new_number])
        out = ''
        for j in range(len(new_number)):
            out += str(s)[-1]
            s -= int(new_number[j])
        new_number = out
        if display:
            print(f'\r{new_number[:8]}', end='')
    if display:
        print(f'\r{new_number[:8]}', end='\n')
    return new_number[:8]


if __name__ == '__main__':
    puzzle_input = open('day_16.in').read().strip()

    # Part 1
    test_inputs = {
        '80871224585914546619083218645595': '24176176',
        '19617804207202209144916044189917': '73745418',
        '69317163492948606335995924319873': '52432133',
    }
    for test_input, test_output in test_inputs.items():
        assert calculate(test_input, 100) == test_output

    calculate(puzzle_input, 100, display=True)

    # Part 2
    test_inputs = {
        '03036732577212944063491565474664': '84462026',
        '02935109699940807407585447034323': '78725270',
        '03081770884921959731165446850517': '53553731',
    }
    for test_input, test_output in test_inputs.items():
        test_input = test_input[:] * 10000
        offset = int(test_input[:7])
        test_input = test_input[offset:]
        assert calculate_special_case(test_input, 100) == test_output

    puzzle_input = puzzle_input[:] * 10000
    offset = int(puzzle_input[:7])
    puzzle_input = puzzle_input[offset:]
    calculate_special_case(puzzle_input, 100, display=True)
