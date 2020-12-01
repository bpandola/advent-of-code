puzzle_input = [int(x) for x in open('day_01.in').read()]
print(puzzle_input)

accumulator = 0
sequence = puzzle_input[:] + [puzzle_input[0]]
for i in range(len(sequence)-1):
    if sequence[i] == sequence[i+1]:
        accumulator += sequence[i]
print(accumulator)


accumulator = 0
sequence = puzzle_input[:]
seq_len = len(sequence)
for i in range(seq_len):
    if sequence[i] == sequence[(i+seq_len//2)%seq_len]:
        accumulator += sequence[i]
print(accumulator)
