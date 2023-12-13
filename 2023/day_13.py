def parse_input(filename):
    data = []
    patterns = open(filename).read().split('\n\n')
    for pattern in patterns:
        lines = pattern.split('\n')
        horizontal = lines
        w, h = len(lines[0]), len(lines)
        vertical = []
        for i in range(w):
            line = ''
            for j in range(h):
                line += lines[j][i]
            vertical.append(line)
        data.append((list(horizontal), list(vertical)))
    return data

def summarize_reflections(patterns):
    total = 0
    for pattern in patterns:
        for i in [0,1]:
            p = pattern[i]
            for col, line in enumerate(p, start=1):
                if col >= len(p):
                    continue
                if p[col-1] == p[col]:
                    col1, col2 =col-1,col
                    potential_mirror_col = col
                    mirror = True
                    while True:
                        if col1<0 or col2 >= len(p):
                            break
                        if p[col1] != p[col2]:
                            mirror = False
                            break
                        col1-=1
                        col2+=1
                    if mirror:
                        t = potential_mirror_col
                        if i == 0:
                            t *=100
                        total+=t
                        break

    return total







if __name__ == '__main__':
    sample_input = parse_input('day_13.in.sample')
    puzzle_input = parse_input('day_13.in')

    # Part 1
    assert summarize_reflections(sample_input) == 405
    print(summarize_reflections(puzzle_input))

    # Part 2
    #assert find_prev_values(sample_input) == 2
    #print(find_prev_values(puzzle_input))
