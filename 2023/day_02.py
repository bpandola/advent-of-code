from math import prod


def parse_input(filename):
    games = []
    lines = open(filename).read().split('\n')
    for line in lines:
        _, arr = line.split(': ')
        draws = []
        for data in arr.split('; '):
            picks = data.split(', ')
            counts = {}
            for pick in picks:
                num, color = pick.split()
                counts[color] = int(num)
            draws.append(counts)
        games.append(draws)
    return games


def validate_games(games, constraints):
    valid_game_ids = []
    for i, game in enumerate(games, start=1):
        game_valid = True
        for draw in game:
            for color, num in constraints.items():
                if draw.get(color, 0) > num:
                    game_valid = False
                    break
        if game_valid:
            valid_game_ids.append(i)
    return sum(valid_game_ids)


def calculate_games_power(games):
    powers = []
    for game in games:
        color_minimums = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        for draw in game:
            for color, num in draw.items():
                if num > color_minimums[color]:
                    color_minimums[color] = num
        powers.append(prod(color_minimums.values()))
    return sum(powers)


if __name__ == '__main__':
    puzzle_input = parse_input('day_02.in')
    sample_input = parse_input('day_02.in.sample')

    # Part 1
    game_constraints = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    assert validate_games(sample_input, game_constraints) == 8
    print(validate_games(puzzle_input, game_constraints))

    # Part 2
    assert calculate_games_power(sample_input) == 2286
    print(calculate_games_power(puzzle_input))
