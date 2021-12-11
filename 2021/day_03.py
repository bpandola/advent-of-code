
def parse_input(filename):
    binary_numbers = open(filename).read().split('\n')
    return binary_numbers


def transform_numbers_to_bits(binary_numbers):
    bits = []  # Each index in this array will be all bit values for that index.
    num_bits = len(binary_numbers[0])
    for bit in range(0, num_bits):
        bits.append([int(binary[bit]) for binary in binary_numbers])
    return bits


def calculate_power_consumption(binary_numbers):
    bits = transform_numbers_to_bits(binary_numbers)
    gamma, epsilon = '', ''
    for values in bits:
        common_value = 1 if sum(values) > len(values) / 2 else 0
        gamma += str(common_value)
        epsilon += str(common_value ^ 1)
    return int(gamma, 2) * int(epsilon, 2)


def find_rating_value(binary_numbers, bit_criteria):
    remaining_numbers = binary_numbers[:]
    bits = transform_numbers_to_bits(remaining_numbers)
    bit_position = 0
    while len(remaining_numbers) > 1:
        common_value = 1 if sum(bits[bit_position]) >= len(bits[bit_position]) / 2 else 0
        common_value = common_value if bit_criteria else common_value ^ 1
        temp = []
        for index, value in enumerate(remaining_numbers):
            if bits[bit_position][index] == common_value:
                temp.append(value)
        bit_position += 1
        remaining_numbers = temp[:]
        bits = transform_numbers_to_bits(remaining_numbers)
    return remaining_numbers[0]


def calculate_life_support_rating(binary_numbers):
    o2_generator_rating = find_rating_value(binary_numbers, 1)
    c02_scrubber_rating = find_rating_value(binary_numbers, 0)
    return int(o2_generator_rating, 2) * int(c02_scrubber_rating, 2)


if __name__ == '__main__':
    puzzle_input = parse_input('day_03.in')
    sample_input = parse_input('day_03.in.sample_01')

    # Part 1
    assert calculate_power_consumption(sample_input) == 198
    print(calculate_power_consumption(puzzle_input))

    # Part 2
    assert calculate_life_support_rating(sample_input) == 230
    print(calculate_life_support_rating(puzzle_input))
