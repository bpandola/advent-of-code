

def parse_instruction(instruction):
    tokens = instruction.split(' ')
    instruction = tokens[0] if tokens[0] != 'turn' else tokens[1]
    grid_start = [int(t) for t in tokens[-3].split(',')]
    grid_end = [int(t) for t in tokens[-1].split(',')]
    return instruction, grid_start, grid_end


def display_lights(instructions):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for i in instructions:
        op, start, end = parse_instruction(i)
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if op == 'on':
                    grid[x][y] = 1
                elif op == 'off':
                    grid[x][y] = 0
                elif op == 'toggle':
                    grid[x][y] ^= 1
    return grid


def display_lights_with_brightness(instructions):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for i in instructions:
        op, start, end = parse_instruction(i)
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if op == 'on':
                    grid[x][y] += 1
                elif op == 'off':
                    grid[x][y] = grid[x][y] - 1 if grid[x][y] else grid[x][y]
                elif op == 'toggle':
                    grid[x][y] += 2
    return grid


if __name__ == '__main__':
    puzzle_input = open('day_6.in').read().split('\n')

    # Part 1
    rows = display_lights(['turn on 0,0 through 999,999'])
    assert sum(sum(row) for row in rows) == 1000000

    print sum(sum(row) for row in display_lights(puzzle_input))

    # Part 2
    print sum(sum(row) for row in display_lights_with_brightness(puzzle_input))
