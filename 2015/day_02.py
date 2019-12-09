def dimension_string_to_dict(dimension_string):
    return {
        'length': int(dimension_string.split('x')[0]),
        'width': int(dimension_string.split('x')[1]),
        'height': int(dimension_string.split('x')[2]),
    }


def calculate_paper_needed(dimensions):
    dimensions = dimension_string_to_dict(dimensions)
    side_dimensions = [
        dimensions['length'] * dimensions['width'],
        dimensions['width'] * dimensions['height'],
        dimensions['height'] * dimensions['length'],
    ]
    total = 0
    for i in side_dimensions:
        total += i * 2
    smallest_side = min(side_dimensions)
    total += smallest_side
    return total


def calculate_ribbon_needed(dimensions):
    dimensions = list(dimension_string_to_dict(dimensions).values())
    side_lengths = sorted(dimensions)
    ribbon = (side_lengths[0] * 2) + (side_lengths[1] * 2)
    bow = dimensions[0] * dimensions[1] * dimensions[2]
    return ribbon + bow


if __name__ == '__main__':
    puzzle_input = open('day_02.in').read().split('\n')

    # Part 1
    assert calculate_paper_needed('2x3x4') == 58
    assert calculate_paper_needed('1x1x10') == 43

    print(sum([calculate_paper_needed(d) for d in puzzle_input]))

    # Part 2
    assert calculate_ribbon_needed('2x3x4') == 34
    assert calculate_ribbon_needed('1x1x10') == 14

    print(sum([calculate_ribbon_needed(d) for d in puzzle_input]))
