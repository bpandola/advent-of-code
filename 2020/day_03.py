
import functools


puzzle_input = [line for line in open('day_03.in').read().split('\n')]

dxs = [1,3,5,7,1]
dys = [1,1,1,1,2]


dx = 3
dy = 1
trees = 0
trees_hit = []
for i in range(len(dxs)):
    trees = 0
    dx = dxs[i]
    dy = dys[i]
    x, y = 0,0
    while True:
        x += dx
        y += dy
        if y >= len(puzzle_input):
            break
        try:
            if puzzle_input[y][x%len(puzzle_input[y])] == '#':
                trees += 1
        except IndexError:
            print('wtf')
    trees_hit.append(trees)
print(trees_hit[1])
print(functools.reduce((lambda x, y: x * y), trees_hit))
