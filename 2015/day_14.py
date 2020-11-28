class ReinderStateMachine:

    def __init__(self, name, distance_per_second, seconds_before_rest, seconds_to_rest):
        self.name = name
        self.distance_per_second = distance_per_second
        self.seconds_before_rest = seconds_before_rest
        self.seconds_to_rest = seconds_to_rest
        self._stack = []
        self.distance_traveled = 0

    def tick(self):
        if not self._stack:
            for _ in range(self.seconds_before_rest):
                self._stack.append(self.distance_per_second)
            for _ in range(self.seconds_to_rest):
                self._stack.append(0)
        self.distance_traveled += self._stack.pop(0)

    def __repr__(self):
        return self.name + ': ' + str(self.distance_traveled)


def parse_input(data):
    reindeer = []
    for line in data.split('\n'):
        line = line.strip()
        tokens = line.split(' ')
        name = tokens[0]
        speed = int(tokens[3])
        duration = int(tokens[6])
        rest = int(tokens[13])
        reindeer.append(ReinderStateMachine(name, speed, duration, rest))
    return reindeer


if __name__ == '__main__':
    puzzle_input = open('day_14.in').read().strip()

    # Part 1
    reindeer = parse_input(puzzle_input)
    for i in range(2503):
        for each in reindeer:
            each.tick()
    fastest = max(reindeer, key=lambda r: r.distance_traveled)
    print(fastest)

    # Part 2
    reindeer = parse_input(puzzle_input)
    points = {}
    for each in reindeer:
        points[each.name] = 0
    for i in range(2503):
        for each in reindeer:
            each.tick()
        furthest = max(reindeer, key=lambda r: r.distance_traveled)
        for points_iter in reindeer:
            if points_iter.distance_traveled == furthest.distance_traveled:
                points[points_iter.name] += 1
    print([(k, v) for k, v in points.items() if v == max(points.values())])
