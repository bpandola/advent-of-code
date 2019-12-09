def calculate_wire_points(path):
    delta_x = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    delta_y = {'L': 0, 'R': 0, 'U': 1, 'D': -1}
    points = {}
    x = 0
    y = 0
    total_length = 0
    for cmd in path:
        direction, length = cmd[0], int(cmd[1:])
        for _ in range(length):
            x += delta_x[direction]
            y += delta_y[direction]
            total_length += 1
            # Don't re-add if it crosses itself.
            if (x, y) not in points:
                points[(x, y)] = total_length
    return points


def find_shortest_intersection_distance(points1, points2):
    intersections = set(points1) & set(points2)
    return min(abs(x) + abs(y) for (x, y) in intersections)


def find_intersection_with_fewest_steps(points1, points2):
    intersections = set(points1) & set(points2)
    return min(points1[p] + points2[p] for p in intersections)


if __name__ == '__main__':
    puzzle_input = [i.split(',') for i in open('day_03.in').read().split('\n')]

    # Part 1
    wires = [
        ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
        ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'],
    ]
    p1 = calculate_wire_points(wires[0])
    p2 = calculate_wire_points(wires[1])
    assert find_shortest_intersection_distance(p1, p2) == 159

    wires = [
        ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
        ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'],
    ]
    p1 = calculate_wire_points(wires[0])
    p2 = calculate_wire_points(wires[1])
    assert find_shortest_intersection_distance(p1, p2) == 135

    p1 = calculate_wire_points(puzzle_input[0])
    p2 = calculate_wire_points(puzzle_input[1])
    print(find_shortest_intersection_distance(p1, p2))

    # Part 2
    wires = [
        ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
        ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'],
    ]
    p1 = calculate_wire_points(wires[0])
    p2 = calculate_wire_points(wires[1])
    assert find_intersection_with_fewest_steps(p1, p2) == 610

    wires = [
        ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
        ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'],
    ]
    p1 = calculate_wire_points(wires[0])
    p2 = calculate_wire_points(wires[1])
    assert find_intersection_with_fewest_steps(p1, p2) == 410

    p1 = calculate_wire_points(puzzle_input[0])
    p2 = calculate_wire_points(puzzle_input[1])
    print(find_intersection_with_fewest_steps(p1, p2))
