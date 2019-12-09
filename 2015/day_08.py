def calculate_string_length(code):
    length_literal = len(code)
    length_memory = length_literal
    if code[0] == '"' and code[-1] == '"':
        length_memory -= 2
    i = 0
    while True:
        if code[i] == '\\' and code[i + 1] == '\\':
            length_memory -= 1
            i += 2
        elif code[i] == '\\' and code[i + 1] == '"':
            length_memory -= 1
            i += 2
        elif code[i] == '\\' and code[i + 1] == 'x':
            length_memory -= 3
            i += 2
        else:
            i += 1
        if i > length_literal - 2:
            break
    return length_literal, length_memory


def encode_string_length(code):
    length_literal = len(code)
    encoded = ''
    i = 0
    while True:
        if code[i] == '"':
            encoded += '\\"'
        elif code[i] == '\\':
            encoded += '\\\\'
        else:
            encoded += code[i]
        i += 1
        if i >= length_literal:
            break
    encoded = '"' + encoded + '"'
    return length_literal, len(encoded)


if __name__ == '__main__':
    puzzle_input = open('day_08.in').read().strip().split('\n')

    # Part 1
    assert calculate_string_length('"\\\\\\\\"') == (6, 2)
    test_fixture = {
        '""': (2, 0),
        '"abc"': (5, 3),
        '"aaa\\"aaa"': (10, 7),
        '"\\x27"': (6, 1),
    }
    for input_, output in test_fixture.items():
        assert calculate_string_length(input_) == output
    assert sum([lit - mem for (lit, mem) in [calculate_string_length(code) for code in test_fixture.keys()]]) == 12

    print(sum([lit - mem for (lit, mem) in [calculate_string_length(code) for code in puzzle_input]]))

    # Part 2
    assert encode_string_length('"\\\\\\\\"') == (6, 14)
    test_fixture = {
        '""': (2, 6),
        '"abc"': (5, 9),
        '"aaa\\"aaa"': (10, 16),
        '"\\x27"': (6, 11),
    }
    for input_, output in test_fixture.items():
        assert encode_string_length(input_) == output
    assert sum([enc - lit for (lit, enc) in [encode_string_length(code) for code in test_fixture.keys()]]) == 19

    print(sum([enc - lit for (lit, enc) in [encode_string_length(code) for code in puzzle_input]]))
