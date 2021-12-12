from functools import reduce


def parse_input(filename):
    lines = [s for s in open(filename).read().split('\n')]
    line_length = len(lines[0])
    top = bottom = '9' * (line_length + 2)
    # Add a border of 9s all the way around, to make simplify adjacency lookups.
    lines_with_border = [top]
    for line in lines:
        lines_with_border.append('9' + line + '9')
    lines_with_border.append(bottom)
    return lines_with_border


def find_low_points(heightmap):
    low_points = {}
    for row in range(1, len(heightmap) - 1):
        for col in range(1, len(heightmap[0]) - 1):
            point = int(heightmap[row][col])
            conditions = [
                int(heightmap[row - 1][col]) > point,
                int(heightmap[row][col - 1]) > point,
                int(heightmap[row][col + 1]) > point,
                int(heightmap[row + 1][col]) > point,
            ]
            if all(conditions):
                low_points[(col, row)] = point
    return low_points


def calculate_risk_level(heightmap):
    low_points = find_low_points(heightmap)
    return sum(low_points.values()) + len(low_points)


def calculate_basin_cipher(heightmap):
    low_points = find_low_points(heightmap)
    basins = []

    def find_basin_points(origin, existing_points):
        surrounding_points_in_basin = set()
        x, y = origin
        if int(heightmap[y - 1][x]) != 9 and (x, y - 1) not in existing_points:
            surrounding_points_in_basin.add((x, y - 1))
        if int(heightmap[y][x - 1]) != 9 and (x - 1, y) not in existing_points:
            surrounding_points_in_basin.add((x - 1, y))
        if int(heightmap[y][x + 1]) != 9 and (x + 1, y) not in existing_points:
            surrounding_points_in_basin.add((x + 1, y))
        if int(heightmap[y + 1][x]) != 9 and (x, y + 1) not in existing_points:
            surrounding_points_in_basin.add((x, y + 1))
        if not len(surrounding_points_in_basin):
            return
        existing_points |= surrounding_points_in_basin
        for coords in surrounding_points_in_basin:
            find_basin_points(coords, existing_points)

    for point in low_points.keys():
        basin = {point}
        find_basin_points(point, basin)
        basins.append(basin)
    basin_sizes = sorted([len(b) for b in basins])
    result = reduce((lambda x, y: x * y), basin_sizes[-3:])
    return result


if __name__ == '__main__':
    puzzle_input = parse_input('day_09.in')
    sample_input = parse_input('day_09.in.sample_01')

    # Part 1
    assert calculate_risk_level(sample_input) == 15
    print(calculate_risk_level(puzzle_input))

    # Part 2
    assert calculate_basin_cipher(sample_input) == 1134
    print(calculate_basin_cipher(puzzle_input))
