import math


def num_asteroids_visible_from_location(coords, data):
    ax, ay = coords[0], coords[1]
    visible = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == '#':
                dx = x - ax
                dy = y - ay
                if (dx, dy) == (0, 0):
                    continue  # self
                gcd = math.gcd(dx, dy)
                dx //= gcd
                dy //= gcd
                # Start from monitoring location and step
                # toward target asteroid coordinates.
                i, j = ax, ay
                while True:
                    i += dx
                    j += dy
                    if (i, j) == (x, y):
                        # Made it to target asteroid.
                        visible.append((x, y))
                        break
                    if data[j][i] == '#':
                        # Not visible.  Another asteroid is blocking our path.
                        break
    return visible


def find_best_location_for_monitoring_station(data):
    asteroids_visible_by_location = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == '#':
                asteroids_visible_by_location[(x, y)] = num_asteroids_visible_from_location((x, y), data)
    best_location = max(asteroids_visible_by_location, key=lambda l: len(asteroids_visible_by_location[l]))
    return best_location, len(asteroids_visible_by_location[best_location])


def calculate_vaporization_order(coords, data):
    x, y = coords[0], coords[1]
    vaporized = []
    asteroids_visible = num_asteroids_visible_from_location((x, y), data)
    while asteroids_visible:
        data = data[:]
        angle_to_asteroid = {}
        for (asteroid_x, asteroid_y) in asteroids_visible:
            dx = asteroid_x - x
            dy = asteroid_y - y
            angle = math.atan2(dy, dx)
            # Adjust coordinates so 0/360 degrees is pointing up.
            if dy < 0 <= dx:
                angle_adjusted = abs(angle + math.pi / 2)
            elif dy >= 0 < dx:
                angle_adjusted = angle + math.pi / 2
            elif dx <= 0 <= dy:
                angle_adjusted = angle + math.pi / 2
            else:
                angle_adjusted = 2 * math.pi - abs(angle + math.pi / 2)
            angle_to_asteroid[angle_adjusted] = (asteroid_x, asteroid_y)
        sorted_angles = sorted(angle_to_asteroid.keys())  # Clockwise sweep.
        for asteroid_coords in [angle_to_asteroid[angle] for angle in sorted_angles]:
            vx, vy = asteroid_coords[0], asteroid_coords[1]
            row = data[vy]
            row = row[:vx] + '.' + row[vx + 1:]  # Remove asteroid from grid.
            data[vy] = row
            vaporized.append((vx, vy))
        asteroids_visible = num_asteroids_visible_from_location((x, y), data)
    return [(-1, -1)] + vaporized  # Make it 1-based array for easier assertions.


if __name__ == '__main__':
    puzzle_input = open('day_10.in').read().split('\n')

    # Part 1
    sample_1 = [
        '......#.#.',
        '#..#.#....',
        '..#######.',
        '.#.#.###..',
        '.#..#.....',
        '..#....#.#',
        '#..#....#.',
        '.##.#..###',
        '##...#..#.',
        '.#....####',
    ]
    location, num_asteroids_visible = find_best_location_for_monitoring_station(sample_1)
    assert location == (5, 8)
    assert num_asteroids_visible == 33

    sample_2 = [
        '#.#...#.#.',
        '.###....#.',
        '.#....#...',
        '##.#.#.#.#',
        '....#.#.#.',
        '.##..###.#',
        '..#...##..',
        '..##....##',
        '......#...',
        '.####.###.',
    ]
    location, num_asteroids_visible = find_best_location_for_monitoring_station(sample_2)
    assert location == (1, 2)
    assert num_asteroids_visible == 35

    sample_3 = [
        '.#..#..###',
        '####.###.#',
        '....###.#.',
        '..###.##.#',
        '##.##.#.#.',
        '....###..#',
        '..#.#..#.#',
        '#..#.#.###',
        '.##...##.#',
        '.....#.#..',
    ]
    location, num_asteroids_visible = find_best_location_for_monitoring_station(sample_3)
    assert location == (6, 3)
    assert num_asteroids_visible == 41

    sample_4 = [
        '.#..##.###...#######',
        '##.############..##.',
        '.#.######.########.#',
        '.###.#######.####.#.',
        '#####.##.#.##.###.##',
        '..#####..#.#########',
        '####################',
        '#.####....###.#.#.##',
        '##.#################',
        '#####.##.###..####..',
        '..######..##.#######',
        '####.##.####...##..#',
        '.#####..#.######.###',
        '##...#.##########...',
        '#.##########.#######',
        '.####.#.###.###.#.##',
        '....##.##.###..#####',
        '.#.#.###########.###',
        '#.#.#.#####.####.###',
        '###.##.####.##.#..##',
    ]
    location, num_asteroids_visible = find_best_location_for_monitoring_station(sample_4)
    assert location == (11, 13)
    assert num_asteroids_visible == 210

    _, num_asteroids_visible = find_best_location_for_monitoring_station(puzzle_input)
    print(num_asteroids_visible)

    # Part 2
    location, _ = find_best_location_for_monitoring_station(sample_4)
    asteroids_to_be_vaporized = calculate_vaporization_order(location, sample_4)
    assert asteroids_to_be_vaporized[1] == (11, 12)
    assert asteroids_to_be_vaporized[2] == (12, 1)
    assert asteroids_to_be_vaporized[3] == (12, 2)
    assert asteroids_to_be_vaporized[10] == (12, 8)
    assert asteroids_to_be_vaporized[20] == (16, 0)
    assert asteroids_to_be_vaporized[50] == (16, 9)
    assert asteroids_to_be_vaporized[100] == (10, 16)
    assert asteroids_to_be_vaporized[199] == (9, 6)
    assert asteroids_to_be_vaporized[200] == (8, 2)
    assert asteroids_to_be_vaporized[201] == (10, 9)
    assert asteroids_to_be_vaporized[299] == (11, 1)

    sample_5 = [
        '.#....#####...#..',
        '##...##.#####..##',
        '##...#...#.#####.',
        '..#.....#...###..',
        '..#.#.....#....##',
    ]
    location, _ = find_best_location_for_monitoring_station(sample_5)
    asteroids_to_be_vaporized = calculate_vaporization_order(location, sample_5)
    assert asteroids_to_be_vaporized[1] == (8, 1)
    assert asteroids_to_be_vaporized[2] == (9, 0)
    assert asteroids_to_be_vaporized[3] == (9, 1)
    assert asteroids_to_be_vaporized[9] == (15, 1)
    assert asteroids_to_be_vaporized[10] == (12, 2)
    assert asteroids_to_be_vaporized[20] == (2, 3)
    assert asteroids_to_be_vaporized[36] == (14, 3)

    location, _ = find_best_location_for_monitoring_station(puzzle_input)
    asteroids_to_be_vaporized = calculate_vaporization_order(location, puzzle_input)
    print(asteroids_to_be_vaporized[200][0] * 100 + asteroids_to_be_vaporized[200][1])
