def parse_input(filename):
    data = []
    data = open(filename).read().split(',')
    return data


def move_rock(x, y, delta, grid):
    while True:
        y += delta
        if y < 0:
            break
        spot = grid[y][x]
        if spot in ['#','O']:
            break
        if spot == '.':
            grid[y][x] = grid[y+1][x]
            grid[y+1][x] = '.'


def tilt_north(data):
    grid = data[:]
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            print(x,y)
            if grid[y][x] == 'O':
                move_rock(x, y, -1, grid)
    total = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == 'O':
                total += (len(grid) - y)
    return total

def hash_string(s):
    current_value = 0
    for char in s:
        ascii_char = ord(char)
        current_value += ascii_char
        current_value = current_value * 17
        current_value = current_value % 256
    return current_value

    # Determine the ASCII code for the current character of the string.
    # Increase the current value by the ASCII code you just determined.
    # Set the current value to itself multiplied by 17.
    # Set the current value to the remainder of dividing itself by 256.

def hash_values(values):
    total = 0
    for value in values:
        total += hash_string(value)
    return total

def focus_power(values):
    boxes = {}
    focal_lengths = {}
    for i in range(256):
        boxes[i]=[]
    for value in values:
        sep = '=' if '=' in value else '-'
        label = value.split(sep)[0]
        if sep == '=':
            focal_length = value.split(sep)[1]
        label_hash = hash_string(label)
        box = boxes[label_hash]
        if sep == '-':
            try:
                box.remove(label)
            except ValueError:
                pass
        elif sep == '=':
            if label in box:
                focal_lengths[label_hash][label] = int(focal_length)
            else:
                box.append(label)
                if label_hash not in focal_lengths:
                    focal_lengths[label_hash] = {}
                focal_lengths[label_hash][label] = int(focal_length)
    focusing_power = 0
    for i in range(256):
        box = boxes[i]
        for index, lens in enumerate(box, start=1):
            fp = (i+1)*(index)*focal_lengths[i][lens]
            focusing_power += fp
    return focusing_power


if __name__ == '__main__':
    sample_input = parse_input('day_15.in.sample')
    puzzle_input = parse_input('day_15.in')
    assert hash_string('HASH')==52
    print(hash_values(sample_input))
    print(hash_values(puzzle_input))
    print(focus_power(sample_input))
    print(focus_power(puzzle_input))
    # Part 1
    #assert tilt_north(sample_input) == 136
    #print(tilt_north(puzzle_input))

    # Part 2
    #assert summarize_reflections(sample_input)['fixed'] == 300
    #print(summarize_reflections(puzzle_input)['fixed'])
