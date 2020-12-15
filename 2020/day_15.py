from itertools import islice


# Modified Van Eck Sequence with Starting Numbers
def van_eck(starting_numbers):
    seen = {}
    for i in range(len(starting_numbers) - 1):
        yield starting_numbers[i]
        seen[starting_numbers[i]] = i
    n, seen, val = len(starting_numbers) - 1, seen, starting_numbers[-1]
    while True:
        yield val
        last = {val: n}
        val = n - seen.get(val, n)
        seen.update(last)
        n += 1


if __name__ == '__main__':
    puzzle_input = list(map(int, open('day_15.in').read().split(',')))

    # Part 1
    assert list(islice(van_eck([1, 3, 2]), 2020))[-1] == 1
    assert list(islice(van_eck([2, 1, 3]), 2020))[-1] == 10
    assert list(islice(van_eck([1, 2, 3]), 2020))[-1] == 27
    assert list(islice(van_eck([2, 3, 1]), 2020))[-1] == 78
    assert list(islice(van_eck([3, 2, 1]), 2020))[-1] == 438
    assert list(islice(van_eck([3, 1, 2]), 2020))[-1] == 1836
    print(list(islice(van_eck(puzzle_input), 2020))[-1])

    # Part 2
    print(list(islice(van_eck(puzzle_input), 30000000))[-1])
