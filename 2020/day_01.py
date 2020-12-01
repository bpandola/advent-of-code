



puzzle_input = [int(i) for i in open('day_01.in').read().split('\n')]
print(puzzle_input)

for i in range(len(puzzle_input)):
    num_1 = puzzle_input[i]
    for j in range(len(puzzle_input)):
        num_2 = puzzle_input[j]
        for k in range(len(puzzle_input)):
            num_3 = puzzle_input[k]
            if num_1 + num_2 + num_3 == 2020:
                print("Indices ({}, {}): {}".format(i, j, num_1 * num_2  * num_3))