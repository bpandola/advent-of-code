def is_nice_v1(word):
    # Contains at least three vowels.
    num_vowels = 0
    for s in word:
        if s in 'aeiou':
            num_vowels += 1
    if num_vowels <= 2:
        return False
    # Contains at least one letter that appears twice in a row.
    num_repeated = 0
    for a in 'abcdefghijklmnopqrstuvwxyz':
        if a + a in word:
            num_repeated += 1
    if not num_repeated:
        return False
    # Does not contain verboten strings.
    for bad in ['ab', 'cd', 'pq', 'xy']:
        if bad in word:
            return False
    return True


def is_nice_v2(word):
    # Contains a pair of any two letters without overlap.
    for i in range(len(word) - 1):
        search = word[i:i + 2]
        if search in word[0:i] or search in word[i + 2:]:
            break
    else:
        return False
    # Contains at least one letter that repeats with one letter between them.
    for i in range(len(word) - 2):
        if word[i] == word[i + 2]:
            break
    else:
        return False
    return True


if __name__ == '__main__':
    puzzle_input = open('day_05.in').read().split('\n')

    # Part 1
    assert is_nice_v1('ugknbfddgicrmopn') is True
    assert is_nice_v1('aaa') is True
    assert is_nice_v1('jchzalrnumimnmhp') is False
    assert is_nice_v1('haegwjzuvuyypxyu') is False
    assert is_nice_v1('dvszwmarrgswjxmb') is False

    print(sum([int(is_nice_v1(word)) for word in puzzle_input]))

    # Part 2
    assert is_nice_v2('aaa') is False
    assert is_nice_v2('qjhvhtzxzqqjkmpb') is True
    assert is_nice_v2('xxyxx') is True
    assert is_nice_v2('uurcxstgmygtbstg') is False
    assert is_nice_v2('ieodomkazucvgmuy') is False

    print(sum([int(is_nice_v2(word)) for word in puzzle_input]))
