def parse_input(filename):
    lines = open(filename).read().split('\n')
    return lines

def parse_calibration_values_v1(blursed_inputs):
    values = []
    for line in blursed_inputs:
        digits = []
        for character in line:
            if character.isdigit():
                digits.append(character)
        value = int(str(digits[0]+str(digits[-1])))
        values.append(value)

    return values

if __name__ == '__main__':
    puzzle_input = parse_input('day_01.in')
    sample_input = parse_input('day_01.in.sample_01')

    # Part 1
    assert sum(parse_calibration_values_v1(sample_input)) == 142
    print(sum(parse_calibration_values_v1(puzzle_input)))

    # Part 2