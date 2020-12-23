




if __name__ == '__main__':
    # puzzle_input = parse_input('day_23.in')
    # sample_input = parse_input('day_23.in.sample_01')
    # sample_input2 = parse_input('day_23.in.sample_02')

    puzzle_input = [int(c) for c in "135468729"]

    # print(puzzle_input)

    cups = puzzle_input[:]
    # PART2
    # for n in range(len(cups)+1, 1000001):
    #     cups.append(n)
    total_cups = len(cups)
    current_cup_index = 0
    current_cup = cups[current_cup_index]
    for i in range(100):
        three_cups = []
        for j in range(1,4):
            index = current_cup_index + j
            if index >= len(cups):
                index = index % len(cups)
            three_cups.append(cups[index])
        cups = [c for c in cups if c not in three_cups]
        current_cup_index = cups.index(current_cup)
        destination = cups[current_cup_index] - 1
        while True:
            if destination < min(cups+three_cups):
                destination = max(cups + three_cups)
            if destination not in three_cups:
                break
            destination -= 1
        index = cups.index(destination)
        for cup in three_cups:
            index = index + 1
            if index >= total_cups:
                index = index % total_cups
            cups.insert(index, cup)
            index = cups.index(cup)
        current_cup_index = cups.index(current_cup)
        current_cup_index+=1
        if current_cup_index >= len(cups):
            current_cup_index = 0
        current_cup = cups[current_cup_index]
        current_cup_index = cups.index(current_cup)
    print(cups)
    # one_index = cups.index(1)
    # next_index = one_index+1
    # if next_index >= len(cups):
    #     next_index = 0
    # op1 = cups[next_index]
    # next_index+=1
    # if next_index >= len(cups):
    #     next_index = 0
    # op2 = cups[next_index]
    # print(op1 * op2)







