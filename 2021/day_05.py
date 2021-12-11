def parse_input(filename):
    lines = open(filename).read().split('\n')
    segments = []
    for line in lines:
        line = line.replace(' -> ', ',')
        coords = [int(n) for n in line.split(',')]
        v1 = (coords[0], coords[1])
        v2 = (coords[2], coords[3])
        segments.append(Line(v1, v2))
    return segments


class Line:

    def __init__(self, v1, v2):
        self.x1, self.y1 = v1
        self.x2, self.y2 = v2

    @property
    def points(self):
        if self.is_straight:
            x1, x2 = (self.x1, self.x2) if self.x2 > self.x1 else (self.x2, self.x1)
            y1, y2 = (self.y1, self.y2) if self.y2 > self.y1 else (self.y2, self.y1)
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    yield x, y
        elif self.is_diagonal:
            x_step = 1 if self.x2 > self.x1 else -1
            y_step = 1 if self.y2 > self.y1 else -1
            x, y = self.x1, self.y1
            for i in range(abs(self.x1 - self.x2) + 1):
                yield x, y
                x += x_step
                y += y_step

    @property
    def is_horizontal(self):
        return self.y1 == self.y2

    @property
    def is_vertical(self):
        return self.x1 == self.x2

    @property
    def is_diagonal(self):
        return abs(self.x1 - self.x2) == abs(self.y1 - self.y2)

    @property
    def is_straight(self):
        return self.is_horizontal or self.is_vertical


def run_simulation(lines, consider_diagonal=False):
    overlaps = {}
    for line in lines:
        if line.is_straight or (line.is_diagonal and consider_diagonal):
            for point in line.points:
                if point in overlaps:
                    overlaps[point] += 1
                else:
                    overlaps[point] = 1
    return len([v for v in overlaps.values() if v > 1])


if __name__ == '__main__':
    puzzle_input = parse_input('day_05.in')
    sample_input = parse_input('day_05.in.sample_01')

    # Part 1
    assert run_simulation(sample_input) == 5
    print(run_simulation(puzzle_input))

    # Part 2
    assert run_simulation(sample_input, consider_diagonal=True) == 12
    print(run_simulation(puzzle_input, consider_diagonal=True))
