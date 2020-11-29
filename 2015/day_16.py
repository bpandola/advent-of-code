def parse_input(lines):
    sues = []
    for line in lines:
        sue = {}
        attributes = line[line.index(':') + 2:].strip()
        for attr in attributes.split(','):
            attr_name, attr_value = attr.split(':')
            sue[attr_name.strip()] = int(attr_value)
        sues.append(sue)
    return sues


if __name__ == '__main__':
    puzzle_input = open('day_16.in').read().strip().split('\n')
    puzzle_input = parse_input(puzzle_input)

    criteria = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

    # Part 1
    for index, aunt in enumerate(puzzle_input, 1):
        for key, value in criteria.items():
            if value != aunt.get(key, value):
                break
        else:
            print(index)
            break

    # Part 2
    for index, aunt in enumerate(puzzle_input, 1):
        for key, value in criteria.items():
            if key in ['cats', 'trees']:
                if aunt.get(key, value + 1) <= value:
                    break
            elif key in ['pomeranians', 'goldfish']:
                if aunt.get(key, value - 1) >= value:
                    break
            else:
                if aunt.get(key, value) != value:
                    break
        else:
            print(index)
            break
