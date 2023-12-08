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
        value = int(str(digits[0]) + str(digits[-1]))
        values.append(value)
    return values


def parse_calibration_values_v2(blursed_inputs):
    word_to_num = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    values = []
    for line in blursed_inputs:
        digits = []
        # Find first digit
        for index, character in enumerate(line):
            if character.isdigit():
                digits.append(character)
                break
            for word in word_to_num:
                found_word = False
                if line[index:].find(word) == 0:
                    digits.append(word_to_num[word])
                    found_word = True
                if found_word:
                    break
            if digits:
                break
        # Find second digit
        line_reversed = reversed(line)
        for index, character in enumerate(line_reversed):
            if character.isdigit():
                digits.append(character)
                break
            for word in word_to_num:
                found_word = False
                if line[-(index + 1):].find(word) == 0:
                    digits.append(word_to_num[word])
                    found_word = True
                if found_word:
                    break
            if len(digits) == 2:
                break
        value = int(str(digits[0]) + str(digits[1]))
        values.append(value)
    return values


if __name__ == '__main__':
    puzzle_input = parse_input('day_01.in')

    # Part 1
    sample_input = parse_input('day_01.in.sample_01')
    assert sum(parse_calibration_values_v1(sample_input)) == 142
    print(sum(parse_calibration_values_v1(puzzle_input)))

    # Part 2
    sample_input = parse_input('day_01.in.sample_02')
    assert sum(parse_calibration_values_v2(sample_input)) == 281
    print(sum(parse_calibration_values_v2(puzzle_input)))
