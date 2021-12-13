def parse_input(filename):
    lines = [[int(n) for n in line] for line in open(filename).read().split('\n')]
    line_length = len(lines[0])
    border_num = -999999
    top = bottom = [border_num] * (line_length + 2)
    # Add a border all the way around, to simplify adjacency lookups.
    lines_with_border = [top]
    for line in lines:
        lines_with_border.append([border_num] + line + [border_num])
    lines_with_border.append(bottom)
    return lines_with_border


def run_simulation(octo_grid, max_step=100):
    grid = [line[:] for line in octo_grid]
    total_flashes = 0
    step = 1
    while True:
        flashers = {}
        # First, the energy level of each octopus increases by 1.
        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0]) - 1):
                grid[row][col] += 1
                if grid[row][col] > 9:
                    flashers[(col, row)] = False  # False means we haven't flashed yet.
        # Flash
        for flasher in list(flashers.keys()):
            def flash(coord):
                if flashers[coord]:
                    return
                flashers[coord] = True
                deltas = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
                for delta in deltas:
                    xd, yd = delta
                    x, y = coord
                    c = x + xd
                    r = y + yd
                    grid[r][c] += 1
                    if grid[r][c] > 9:
                        if (c, r) not in flashers:
                            flashers[(c, r)] = False
                            flash((c, r))
                        else:
                            if not flashers[(c, r)]:
                                flash((c, r))

            flash(flasher)
        # We don't return until all have flashed, but we stop totalling
        # after we reach the simulation step count.
        if step <= max_step:
            total_flashes += len(flashers)
        # Check for simultaneous flash.
        if len(flashers) == 100:
            return total_flashes, step
        # Reset flashers.
        for (col, row) in flashers.keys():
            grid[row][col] = 0
        flashers = {}
        step += 1


if __name__ == '__main__':
    puzzle_input = parse_input('day_11.in')
    sample_input = parse_input('day_11.in.sample_01')

    # Part 1
    assert run_simulation(sample_input)[0] == 1656
    print(run_simulation(puzzle_input)[0])

    # Part 2
    assert run_simulation(sample_input)[1] == 195
    print(run_simulation(puzzle_input)[1])
