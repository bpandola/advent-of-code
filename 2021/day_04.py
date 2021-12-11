def parse_input(filename):
    lines = open(filename).read().split('\n\n')
    draws = [int(n) for n in lines[0].split(',')]
    lines = lines[1:]
    boards = []
    for line in lines:
        board = []
        rows = line.strip().split('\n')
        for row in rows:
            row = row.strip().replace('  ', ' ')
            numbers = [int(n) for n in row.split(' ')]
            assert len(numbers) == 5
            board.append(numbers)
        boards.append(BingoBoard(board))
    return draws, boards


class BingoBoard:

    def __init__(self, board):
        self._board = board
        self._size = len(board)
        self._winning_combinations = self._generate_winning_combinations()

    def _generate_winning_combinations(self):
        combos = []
        for row in range(0, self._size):
            combo = []
            for col in range(0, self._size):
                combo.append(self._board[row][col])
            combos.append(combo)
        for col in range(0, self._size):
            combo = []
            for row in range(0, self._size):
                combo.append(self._board[row][col])
            combos.append(combo)
        return combos

    def has_a_bingo(self, numbers_drawn):
        for combo in self._winning_combinations:
            if len(set(combo).intersection(set(numbers_drawn))) == self._size:
                return True
        return False

    @property
    def all_numbers(self):
        return [
            number for row in self._board for number in row
        ]

    def unselected_numbers(self, numbers_drawn):
        return set(self.all_numbers) - set(numbers_drawn)

    def score(self, numbers_drawn):
        return sum(self.unselected_numbers(numbers_drawn)) * numbers_drawn[-1]


def run_winning_simulation(simulation_input):
    numbers_drawn, boards = simulation_input
    current_draw = []
    for number in numbers_drawn:
        current_draw.append(number)
        for board in boards:
            if board.has_a_bingo(current_draw):
                return board.score(current_draw)


def run_losing_simulation(simulation_input):
    numbers_drawn, boards = simulation_input
    current_draw = []
    current_boards = []
    for number in numbers_drawn:
        current_draw.append(number)
        for board in boards:
            if not board.has_a_bingo(current_draw):
                current_boards.append(board)
            else:
                if len(boards) == 1:
                    return board.score(current_draw)
        boards = current_boards[:]
        current_boards = []


if __name__ == '__main__':
    puzzle_input = parse_input('day_04.in')
    sample_input = parse_input('day_04.in.sample_01')

    # Part 1
    assert run_winning_simulation(sample_input) == 4512
    print(run_winning_simulation(puzzle_input))

    # Part 2
    assert run_losing_simulation(sample_input) == 1924
    print(run_losing_simulation(puzzle_input))
