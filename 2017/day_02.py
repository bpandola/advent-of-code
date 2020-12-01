import sys
from itertools import permutations

puzzle_input = [[int(x.strip()) for x in line.split('\t')] for line in open('day_02.in').read().split('\n')]
print(puzzle_input)


accumulator = 0
for sequence in puzzle_input:
    sequence_min = sys.maxsize
    sequence_max = -sys.maxsize
    for number in sequence:
        if number > sequence_max:
            sequence_max = number
        if number < sequence_min:
            sequence_min = number
    accumulator += sequence_max - sequence_min
print(accumulator)


accumulator = 0
for sequence in puzzle_input:
    for divisor, dividend in permutations(sequence, 2):
        quotient = float(dividend / divisor)
        if quotient.is_integer():
            accumulator += quotient
            break
print(accumulator)
