import sys
from functools import reduce


def parse_input(filename):
    lines = [line.strip() for line in open(filename).read().split('\n')]
    timestamp = int(lines[0])
    buses = [int(num) if num != 'x' else num for num in lines[1].split(',')]
    bus_tuples = []
    # Create a list of tuples (remainder, bus) where
    # remainder = the expected remainder based on the bus' index
    # in the array (for Chinese Remainder Theorem computation).
    for i, bus in enumerate(buses):
        if bus == 'x':
            continue
        remainder = (bus - i) % bus
        bus_tuples.append((remainder, bus))
    return timestamp, bus_tuples


def calc_earliest_bus_magic_number(data):
    timestamp, buses = data
    bus_num, earliest = -sys.maxsize, sys.maxsize
    for _, bus in buses:
        departure = bus - (timestamp % bus)
        if departure < earliest:
            bus_num = bus
            earliest = departure
    return bus_num * earliest


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def calc_bus_departures_magic_timestamp(data):
    _, buses = data
    # https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
    summed = 0
    prod = reduce(lambda a, b: a * b, [bus[1] for bus in buses])
    for a_i, n_i in buses:
        p = prod // n_i
        summed += a_i * mul_inv(p, n_i) * p
    return summed % prod


if __name__ == '__main__':
    puzzle_input = parse_input('day_13.in')
    sample_input = parse_input('day_13.in.sample')

    # Part 1
    assert calc_earliest_bus_magic_number(sample_input) == 295
    print(calc_earliest_bus_magic_number(puzzle_input))

    # Part 2
    assert calc_bus_departures_magic_timestamp(sample_input) == 1068781
    print(calc_bus_departures_magic_timestamp(puzzle_input))
