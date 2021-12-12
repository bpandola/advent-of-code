def parse_input(filename):
    lines = [s for s in open(filename).read().split('\n')]
    patterns = []
    output = []
    for line in lines:
        temp = line.strip().split(' | ')
        patterns.append(temp[0].split(' '))
        output.append(temp[1].split(' '))
    return patterns, output


def count_unique_digits(data):
    unique_segments = [2, 4, 3, 7]  # Numbers 1,4,7,8
    _, output = data
    ans = len(
        [
            s for o in output for s in o
            if len(s) in unique_segments
        ]
    )
    return ans


def decode(digit_patterns):
    digit_to_pattern = {}
    # First pass for unique patterns.
    for pattern in digit_patterns:
        if len(pattern) == 2:
            digit_to_pattern[1] = pattern
        elif len(pattern) == 3:
            digit_to_pattern[7] = pattern
        elif len(pattern) == 4:
            digit_to_pattern[4] = pattern
        elif len(pattern) == 7:
            digit_to_pattern[8] = pattern
    # Figure out the patterns with 6 segments.
    digit_to_pattern[6] = next(
        p for p in digit_patterns if len(p) == 6 and not set(digit_to_pattern[1]).issubset(set(p)))
    digit_to_pattern[9] = next(
        p for p in digit_patterns if len(p) == 6 and set(digit_to_pattern[4]).issubset(set(p)))
    digit_to_pattern[0] = next(
        p for p in digit_patterns if len(p) == 6 and p not in [digit_to_pattern[6], digit_to_pattern[9]])
    # Figure out the patterns with 5 segments.
    digit_to_pattern[3] = next(
        p for p in digit_patterns if len(p) == 5 and set(digit_to_pattern[1]).issubset(set(p)))
    digit_to_pattern[5] = next(
        p for p in digit_patterns if
        len(p) == 5 and set(p).issubset(set(digit_to_pattern[9])) and p != digit_to_pattern[3])
    digit_to_pattern[2] = next(
        p for p in digit_patterns if len(p) == 5 and p not in [digit_to_pattern[3], digit_to_pattern[5]])
    # Now invert the dictionary, so we can look the digits up by their pattern.
    # Have to use frozenset because pattern might be 'abc' and output pattern might be 'bca'.
    pattern_to_digit = {
        frozenset(v): k for k, v in digit_to_pattern.items()
    }
    return pattern_to_digit


def sum_output_values(data):
    patterns, output = data
    total = 0
    for i in range(len(patterns)):
        patterns_to_digits = decode(patterns[i])
        number = ''
        for p in output[i]:
            number += str(patterns_to_digits[frozenset(p)])
        total += int(number)
    return total


if __name__ == '__main__':
    puzzle_input = parse_input('day_08.in')
    sample_input = parse_input('day_08.in.sample_01')

    # Part 1
    assert count_unique_digits(sample_input) == 26
    print(count_unique_digits(puzzle_input))

    # Part 2
    assert sum_output_values(sample_input) == 61229
    print(sum_output_values(puzzle_input))
