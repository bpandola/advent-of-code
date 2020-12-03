from functools import reduce


def trees_hit(slope, area):
    dx, dy = slope
    col, row = 0, 0
    hits = 0
    while row < len(area):
        col += dx
        row += dy
        if row < len(area) and area[row][col % len(area[row])] == '#':
            hits += 1
    return hits


if __name__ == '__main__':
    puzzle_input = [line for line in open('day_03.in').read().split('\n')]

    sample_input = [
        '..##.......',
        '#...#...#..',
        '.#....#..#.',
        '..#.#...#.#',
        '.#...##..#.',
        '..#.##.....',
        '.#.#.#....#',
        '.#........#',
        '#.##...#...',
        '#...##....#',
        '.#..#...#.#',
    ]

    # Part 1
    assert trees_hit((3, 1), sample_input) == 7
    print(trees_hit((3, 1), puzzle_input))

    # Part 2
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    assert reduce((lambda x, y: x * y), list(map(lambda s: trees_hit(s, sample_input), slopes))) == 336
    print(reduce((lambda x, y: x * y), list(map(lambda s: trees_hit(s, puzzle_input), slopes))))
