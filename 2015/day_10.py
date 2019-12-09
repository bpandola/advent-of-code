def look_and_say(digits):
    digits = str(digits)
    output = ''
    digit = digits[0]
    count = 1
    for c in digits[1:]:
        if c == digit:
            count += 1
        else:
            output += str(count) + digit
            count = 1
            digit = c
    output += str(count) + digit
    return output


if __name__ == '__main__':
    puzzle_input = open('day_10.in').read().strip()

    # Part 1
    assert look_and_say(1) == '11'
    assert look_and_say(11) == '21'
    assert look_and_say(21) == '1211'
    assert look_and_say(1211) == '111221'
    assert look_and_say(111221) == '312211'

    result = puzzle_input
    for i in range(40):
        result = look_and_say(result)
    print(len(result))

    # Part 2
    result = puzzle_input
    for i in range(50):
        result = look_and_say(result)
    print(len(str(result)))
