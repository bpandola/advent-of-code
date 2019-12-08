IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6


if __name__ == '__main__':
    puzzle_input = [int(i) for i in open('day_8.in').read()]

    # Part 1
    data = list(puzzle_input)

    fewest_zeros = IMAGE_HEIGHT * IMAGE_WIDTH
    checksum = 0

    while data:
        layer = data[:IMAGE_WIDTH * IMAGE_HEIGHT]
        data = data[IMAGE_WIDTH * IMAGE_HEIGHT:]

        num_zeros = layer.count(0)
        if num_zeros < fewest_zeros:
            fewest_zeros = num_zeros
            checksum = layer.count(1) * layer.count(2)

    print checksum

    # Part 2
    image = ''
    for i in range(IMAGE_WIDTH * IMAGE_HEIGHT):
        pixel = 'not rendered'
        for layer in range(len(puzzle_input) / (IMAGE_WIDTH * IMAGE_HEIGHT) - 1, -1, -1):
            p = puzzle_input[layer * IMAGE_HEIGHT * IMAGE_WIDTH + i]
            if p == 0:
                pixel = ' '
            elif p == 1:
                pixel = '|'
        assert pixel != 'not rendered'
        image = image + pixel

    for i in range(IMAGE_HEIGHT):
        print image[i * IMAGE_WIDTH:(i + 1) * IMAGE_WIDTH]
