def decipher_repetition_code(messages, fn):
    code_map = {k: {} for k in range(len(messages[0]))}
    for message in messages:
        for index, character in enumerate(message):
            code_map[index][character] = code_map[index].get(character, 0) + 1
    decoded_message = ''
    for index in code_map:
        decoded_message += fn(code_map[index], key=code_map[index].get)
    return decoded_message


if __name__ == '__main__':
    puzzle_input = open('day_06.in').read().split('\n')

    sample_input = [
        'eedadn',
        'drvtee',
        'eandsr',
        'raavrd',
        'atevrs',
        'tsrnev',
        'sdttsa',
        'rasrtv',
        'nssdts',
        'ntnada',
        'svetve',
        'tesnvt',
        'vntsnd',
        'vrdear',
        'dvrsen',
        'enarar',
    ]

    # Part 1
    assert decipher_repetition_code(sample_input, max) == 'easter'

    print(decipher_repetition_code(puzzle_input, max))

    # Part 2
    assert decipher_repetition_code(sample_input, min) == 'advent'

    print(decipher_repetition_code(puzzle_input, min))
