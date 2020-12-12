def parse_input(filename):
    lines = [line.strip() for line in open(filename).read().split('\n')]
    instructions = []
    for line in lines:
        action, value = line[0], int(line[1:])
        instructions.append((action, value))
    return instructions


def nav_with_assumed_instructions(instructions):
    headings = ['N', 'E', 'S', 'W']
    delta_x = {'N': 0, 'S': 0, 'W': -1, 'E': 1}
    delta_y = {'N': 1, 'S': -1, 'W': 0, 'E': 0}

    heading = 'E'
    x, y = 0, 0

    for action, value in instructions:
        if action == 'N':
            y += 1 * value
        elif action == 'S':
            y -= 1 * value
        elif action == 'E':
            x += 1 * value
        elif action == 'W':
            x -= 1 * value
        elif action == 'F':
            x += delta_x[heading] * value
            y += delta_y[heading] * value
        elif action == 'L':
            dir_index = headings.index(heading)
            for _ in range(value // 90):
                dir_index = (dir_index + 3) % 4
            heading = headings[dir_index]
        elif action == 'R':
            dir_index = headings.index(heading)
            for _ in range(value // 90):
                dir_index = (dir_index + 1) % 4
            heading = headings[dir_index]

    return abs(x) + abs(y)


def nav_with_correct_instructions(instructions):
    way_x, way_y = 10, 1
    x, y = 0, 0

    for action, value in instructions:
        if action == 'N':
            way_y += 1 * value
        elif action == 'S':
            way_y -= 1 * value
        elif action == 'E':
            way_x += 1 * value
        elif action == 'W':
            way_x -= 1 * value
        elif action == 'F':
            x += way_x * value
            y += way_y * value
        # Originally, I looked up the math for rotating a point.
        # This works, but it leaves us with a floating point number
        # that is *very* close to being wrong.
        # elif action == 'L' or action == 'R':
        #     angle = math.radians(-value if action == 'R' else value)
        #     tx = math.cos(angle) * way_x - math.sin(angle) * way_y
        #     ty = math.sin(angle) * way_x + math.cos(angle) * way_y
        #     way_x, way_y = tx, ty
        #
        # I got the following from Jonathan Paulson. Very cool trick!
        # Complex numbers are a good way to think about rotations!
        # Think of the point (x,y) as the complex number x+iy
        # Remember i^2=-1. Multiplying by i is the same as rotating 90 degrees.
        # Why? Note i^4 = (-1)^2 = 1, so multiplying by i four times does nothing.
        # i^2 = -1, so multiplying by i flips you around the x and y axes (which is a 180-degree rotation).
        # (x,y)*i = (x+iy)*i = ix+i^2y = -y+ix = (-y,x)
        # (x,y)*i^3 = (x+iy)*i^3 = i^3x+i^4y = y - ix = (y,-x)
        # https://calcworkshop.com/transformations/rotation-rules/
        elif action == 'L':
            for _ in range(value // 90):
                way_x, way_y = -way_y, way_x
        elif action == 'R':
            for _ in range(value // 90):
                way_x, way_y = way_y, -way_x

    return abs(x) + abs(y)


if __name__ == '__main__':
    puzzle_input = parse_input('day_12.in')
    sample_input = parse_input('day_12.in.sample')

    # Part 1
    assert nav_with_assumed_instructions(sample_input) == 25
    print(nav_with_assumed_instructions(puzzle_input))

    # Part 1
    assert nav_with_correct_instructions(sample_input) == 286
    print(nav_with_correct_instructions(puzzle_input))
