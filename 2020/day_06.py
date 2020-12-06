from string import ascii_lowercase

if __name__ == '__main__':
    puzzle_input = [line.split('\n') for line in open('day_06.in').read().split('\n\n')]

    # Part 1
    total = 0
    for group in puzzle_input:
        yeses = set()
        for person in group:
            for answer in person:
                yeses.add(answer)
        total += len(yeses)
    print(total)

    # Part 2
    total = 0
    for group in puzzle_input:
        for c in ascii_lowercase:
            if all([c in person for person in group]):
                total += 1
    print(total)
