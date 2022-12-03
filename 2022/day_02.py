def parse_input(filename):
    lines = open(filename).read().split('\n')
    games = [tuple(line.split(' ')) for line in lines]
    return games


DECODE_SHAPE = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}

DECODE_OUTCOME = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

SHAPE_SCORE = {
    'A': 1,
    'B': 2,
    'C': 3,
}

SCORING = {
    'A': {'A': 3, 'B': 0, 'C': 6},
    'B': {'A': 6, 'B': 3, 'C': 0},
    'C': {'A': 0, 'B': 6, 'C': 3},
}


def decode_choice(key, opponent_choice):
    for shape in SCORING:
        for k, v in SCORING[shape].items():
            if k == opponent_choice and v == DECODE_OUTCOME[key]:
                return shape


def calculate_score(rounds, ultra_top_secret_strategy=False):
    total = 0
    for opponent, me in rounds:
        if ultra_top_secret_strategy:
            me = decode_choice(me, opponent)
        else:
            me = DECODE_SHAPE[me]
        total += SHAPE_SCORE[me]
        total += SCORING[me][opponent]
    return total


if __name__ == '__main__':
    puzzle_input = parse_input('day_02.in')
    sample_input = parse_input('day_02.in.sample_01')

    # Part 1
    assert calculate_score(sample_input) == 15
    print(calculate_score(puzzle_input))

    # Part 2
    assert calculate_score(sample_input, ultra_top_secret_strategy=True) == 12
    print(calculate_score(puzzle_input, ultra_top_secret_strategy=True))
