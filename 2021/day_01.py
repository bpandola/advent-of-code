
def num_depth_increases(depths):
    increase_count = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increase_count += 1
    return increase_count


def num_window_increases(depths, window_length=3):
    windows = []
    for i in range(0, len(depths) - window_length + 1):
        windows.append([])
        for j in range(0, window_length):
            windows[i].append(depths[i + j])
    increase_count = 0
    for i in range(1, len(windows)):
        if sum(windows[i]) > sum(windows[i - 1]):
            increase_count += 1
    return increase_count


if __name__ == '__main__':
    puzzle_input = [int(i) for i in open('day_01.in').read().split('\n')]
    sample_input = [199,
                    200,
                    208,
                    210,
                    200,
                    207,
                    240,
                    269,
                    260,
                    263]

    # Part 1
    assert num_depth_increases(sample_input) == 7
    print(num_depth_increases(puzzle_input))

    # Part 2
    assert num_window_increases(sample_input) == 5
    print(num_window_increases(puzzle_input))
