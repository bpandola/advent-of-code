from itertools import combinations






if __name__ == '__main__':
    #puzzle_input = parse_input('day_15.in')
    #sample_input = parse_input('day_15.in.sample')

    #puzzle_input = [0,3,6]  # [6,3,15,13,1,0]:
    puzzle_input = [6,3,15,13,1,0]

    # Part 1
    for i in range(len(puzzle_input), 2020):
        # print(puzzle_input)
        num = puzzle_input[-1]
        if puzzle_input.count(num) == 1:
            puzzle_input.append(0)
        else:
            prev = [i for i, n in enumerate(puzzle_input) if n == num]

            puzzle_input.append(prev[-1]-prev[-2])
    print(puzzle_input[-1])

    puzzle_input = [6, 3, 15, 13, 1, 0]
    h = {}
    for i, n in enumerate(puzzle_input):
        h[n] = {}
        h[n]['cur'] = i
    current = puzzle_input[-1]

    for i in range(len(puzzle_input), 30000000):
        if h[current].get('prev') is None:
            current = 0
            h[current]['prev'] = h[current]['cur']
            h[current]['cur'] = i
        else:
            current = h[current]['cur'] - h[current]['prev']
            if current not in h:
                h[current] = {}
                h[current]['cur'] = i
            else:
                h[current]['prev'] = h[current]['cur']
                h[current]['cur'] = i
    print(current)

    #print(puzzle_input[-1])
    #print(puzzle_input)

    # Part 1


    # Part 2
