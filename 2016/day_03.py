def count_possible_triangles(triangle_specs):
    count = 0
    for side_lengths in triangle_specs:
        if side_lengths[0] + side_lengths[1] > side_lengths[2]:
            if side_lengths[0] + side_lengths[2] > side_lengths[1]:
                if side_lengths[2] + side_lengths[1] > side_lengths[0]:
                    count += 1
    return count


if __name__ == '__main__':
    puzzle_input = [row for row in open('day_03.in').read().split('\n')]

    # Part 1
    input_part_1 = [[int(i[0:5]), int(i[5:10]), int(i[10:15])] for i in puzzle_input]
    print(count_possible_triangles(input_part_1))

    # Part 2
    input_part_2 = []
    for i in range(0, len(puzzle_input) - 2, 3):
        for j in range(3):
            sides = [
                int(puzzle_input[i][j * 5:(j + 1) * 5]),
                int(puzzle_input[i + 1][j * 5:(j + 1) * 5]),
                int(puzzle_input[i + 2][j * 5:(j + 1) * 5]),
            ]
            input_part_2.append(sides)
    print(count_possible_triangles(input_part_2))
