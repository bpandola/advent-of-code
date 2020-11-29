from collections import defaultdict
from itertools import chain, combinations


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


if __name__ == '__main__':
    puzzle_input = [int(i) for i in open('day_17.in').read().strip().split('\n')]

    # Part 1
    valid_combos = []
    for combination in powerset(puzzle_input):
        if sum(combination) == 150:
            valid_combos.append(combination)

    print(len(valid_combos))

    # Part 2
    transformed = defaultdict(list)
    for combo in valid_combos:
        transformed[len(combo)] += [combo]
    min_key = min(list(transformed.keys()))
    print(len(transformed[min_key]))
