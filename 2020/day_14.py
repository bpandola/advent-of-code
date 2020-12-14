from itertools import combinations


def parse_input(filename):
    lines = [line.strip() for line in open(filename).read().split('\n')]
    ops = []
    for line in lines:
        # tuple(action, address or mask, num)
        data = line.split(' = ')
        if line.startswith('mask'):
            ops.append(('mask', data[1].strip(), ''))
        else:
            mem_num = data[0][4:-1]
            ops.append(('mem', mem_num, data[1].strip()))
    return ops


def mask_num(num, mask):
    padding = ''.join(['0' for _ in range(0, 36 - len(num))])
    padded_num = [c for c in padding + num]
    for i, b in enumerate(mask):
        if b == '1':
            padded_num[i] = '1'
        elif b == '0':
            padded_num[i] = '0'
    return int(''.join(padded_num), base=2)


def mask_memory(num, mask):
    padding = ''.join(['0' for _ in range(0, 36 - len(num))])
    padded_num = [c for c in padding + num]
    padded_nums = []
    for i, b in enumerate(mask):
        if b == '1':
            padded_num[i] = '1'
        elif b == 'X':
            padded_num[i] = 'X'
    num_x = padded_num.count('X')
    str_x = [c for c in ''.join(['01' for _ in range(num_x)])]
    for c in set(combinations(str_x, num_x)):
        subs = list(c)
        new_num = padded_num[:]
        for index, ch in enumerate(padded_num):
            if ch == 'X':
                new_num[index] = subs.pop()
        padded_nums.append(new_num)
    return [int(''.join(n), base=2) for n in padded_nums]


def memory_sum(program):
    mask = None
    mem = {}
    for action, mask_or_address, num in program:
        if action == 'mask':
            mask = mask_or_address
        elif action == 'mem':
            number = "{0:b}".format(int(num))
            mem[int(mask_or_address)] = mask_num(number, mask)
    return sum(mem.values())


def memory_sum_v2(program):
    mask = None
    mem = {}
    for action, mask_or_address, num in program:
        if action == 'mask':
            mask = mask_or_address
        elif action == 'mem':
            number = "{0:b}".format(int(mask_or_address))
            numbers = mask_memory(number, mask)
            for n in numbers:
                mem[n] = int(num)
    return sum(mem.values())


if __name__ == '__main__':
    puzzle_input = parse_input('day_14.in')

    # Part 1
    sample_input = parse_input('day_14.in.sample_01')
    assert memory_sum(sample_input) == 165
    print(memory_sum(puzzle_input))

    # Part 2
    sample_input = parse_input('day_14.in.sample_02')
    assert memory_sum_v2(sample_input) == 208
    print(memory_sum_v2(puzzle_input))
