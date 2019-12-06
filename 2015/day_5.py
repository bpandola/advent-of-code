

def is_string_nice(string):
    # Contains at least three vowels.
    num_vowels = 0
    for s in string:
        if s in 'aeiou':
            num_vowels += 1
    if num_vowels <= 2:
        return False
    # Contains at least one letter that appears twice in a row.
    num_repeated = 0
    for a in 'abcdefghijklmnopqrstuvwxyz':
        if a+a in string:
            num_repeated += 1
    if not num_repeated:
        return False
    # Does not contain verboten strings.
    for bad in ['ab', 'cd', 'pq', 'xy']:
        if bad in string:
            return False
    return True


def is_string_nice_v2(string):
    # Contains a pair of any two letters without overlap.
    for i in range(len(string) - 1):
        search = string[i:i+2]
        if search in string[0:i] or search in string[i+2:]:
            break
    else:
        return False
    # Contains at least one letter that repeats with one letter between them.
    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            break
    else:
        return False
    return True


if __name__ == '__main__':
    puzzle_input = open('day_5.in').read().split('\n')

    # Part 1
    assert is_string_nice('ugknbfddgicrmopn') is True
    assert is_string_nice('aaa') is True
    assert is_string_nice('jchzalrnumimnmhp') is False
    assert is_string_nice('haegwjzuvuyypxyu') is False
    assert is_string_nice('dvszwmarrgswjxmb') is False

    print sum([int(is_string_nice(word)) for word in puzzle_input])

    # Part 2
    assert is_string_nice_v2('aaa') is False
    assert is_string_nice_v2('qjhvhtzxzqqjkmpb') is True
    assert is_string_nice_v2('xxyxx') is True
    assert is_string_nice_v2('uurcxstgmygtbstg') is False
    assert is_string_nice_v2('ieodomkazucvgmuy') is False

    print sum([int(is_string_nice_v2(word)) for word in puzzle_input])
