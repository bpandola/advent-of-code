import sys
from functools import reduce
from itertools import chain, combinations, permutations

def parse_input(filename):
    lines = [line.strip() for line in open(filename).read().split('\n')]
    # action, address or mask, num
    ops = []
    for line in lines:
        data = line.split(' = ')
        if line.startswith('mask'):
            ops.append(('mask', data[1].strip(), ''))
        else:
            mem_num = data[0][4:-1]
            ops.append(('mem', mem_num, data[1].strip()))
    return ops

def mask_num(num, mask):
    padding = ['0' for _ in range(0,36-len(num))]
    padding = ''.join(padding)
    padded_num = [ c for c in padding + num]
    for index, b in enumerate(mask):
        if b == '1':
            padded_num[index] = '1'
        elif b == '0':
            padded_num[index] = '0'

    return int(''.join(padded_num), base=2)

def mask_memory(num, mask):
    padding = ['0' for _ in range(0,36-len(num))]
    padding = ''.join(padding)
    padded_num = [ c for c in padding + num]
    padded_nums = []
    for index, b in enumerate(mask):
        if b == '1':
            padded_num[index] = '1'
        elif b == 'X':
            padded_num[index] = 'X'

    num_x = padded_num.count('X')
    str_x = ['01' for _ in range(num_x)]
    str_x = ''.join(str_x)
    str_x = [c for c in str_x]
    for c in set(combinations(str_x, num_x)):
        subs = list(c)
        new_num = padded_num[:]
        for index, ch in enumerate(padded_num):
            if ch =='X':
                new_num[index] = subs.pop()
        padded_nums.append(new_num)



    return [int(''.join(n), base=2) for n in padded_nums]

if __name__ == '__main__':
    puzzle_input = parse_input('day_14.in')
    #sample_input = parse_input('day_14.in.sample')



    # Part 1
    inp = puzzle_input
    mask = ''
    mem = {}
    for action, mask_or_address, num in inp:
        if action == 'mask':
            mask = mask_or_address
        elif action == 'mem':
            number = "{0:b}".format(int(num))
            mem[int(mask_or_address)] = mask_num(number, mask)
        else:
            raise RuntimeError('bad action')

    print(sum(mem.values()))

    # Part 2
    inp = puzzle_input
    mask = ''
    mem = {}
    for action, mask_or_address, num in inp:
        if action == 'mask':
            mask = mask_or_address
        elif action == 'mem':
            number = "{0:b}".format(int(mask_or_address))
            numbers = mask_memory(number, mask)
            for n in numbers:
                mem[n] = int(num)
        else:
            raise RuntimeError('bad action')

    print(sum(mem.values()))

