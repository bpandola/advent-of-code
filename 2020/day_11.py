from itertools import combinations
from functools import reduce
from collections import defaultdict

def parse_input(filename):
    lines = [line for line in  open(filename).read().split('\n')]
    # Translate into a more convenient data structure.
    # defaultdict[(x, y)] = data; default is '.'
    translated = defaultdict(lambda: '.')

    for y, line in enumerate(lines):
        for x, data in enumerate(lines[y]):
            translated[(x, y)] = data
    return translated

def run_simulation(area_map, ticks=0):
    area = area_map.copy()

    def num_occupied(coords):
        x,y = coords
        occupied = 0
        if area[(x-1, y-1)] == '#':
            occupied+=1
        if area[(x, y - 1)] == '#':
            occupied += 1
        if area[(x+1, y - 1)] == '#':
            occupied += 1
        if area[(x-1, y+1)] == '#':
            occupied+=1
        if area[(x, y + 1)] == '#':
            occupied += 1
        if area[(x+1, y + 1)] == '#':
            occupied += 1
        if area[(x-1, y)] == '#':
            occupied+=1
        if area[(x+1, y)] == '#':
            occupied += 1
        return occupied

    while True:
        area_new = area.copy()
        for coords in list(area.keys()):
            if area[coords] == 'L' and num_occupied(coords) == 0:
                area_new[coords] = '#'
            elif area[coords] == '#' and num_occupied(coords) >= 4:
                area_new[coords] = 'L'

        for coords in list(area_new.keys()):
            if area[coords] != area_new[coords]:
                stopped = False
                break
        else:
            stopped = True

        if stopped:
            break
        area = area_new.copy()

    return len([(k,v) for k,v in area.items() if v == '#'])

dirs = [

(-1,-1),
(0,-1),
(1,-1),
(-1,1),
(0,1),
(1,1),
(-1,0),
(1,0),
]

def run_simulation2(area_map, ticks=0):
    area = area_map.copy()
    minx = min(k[0] for k in area_map.keys())
    maxx = max(k[0] for k in area_map.keys())
    miny = min(k[1] for k in area_map.keys())
    maxy = max(k[1] for k in area_map.keys())

    def num_occupied(coords):
        x,y = coords
        occupied = 0

        for i in range(8):
            px, py = x, y
            while True:
                px += dirs[i][0]
                py += dirs[i][1]
                if area[(px,py)] == 'L':
                    break
                if area[(px, py)] == '#':
                    occupied += 1
                    break
                if px < minx or px > maxx:
                    break
                if py < miny or py > maxy:
                    break



        return occupied

    while True:
        area_new = area.copy()
        for coords in list(area.keys()):
            if area[coords] == 'L' and num_occupied(coords) == 0:
                area_new[coords] = '#'
            elif area[coords] == '#' and num_occupied(coords) >= 5:
                area_new[coords] = 'L'

        for coords in list(area_new.keys()):
            if area[coords] != area_new[coords]:
                stopped = False
                break
        else:
            stopped = True

        if stopped:
            break
        area = area_new.copy()

    return len([(k,v) for k,v in area.items() if v == '#'])



puzzle_input = parse_input('day_11.in')



print(run_simulation(puzzle_input))
print(run_simulation2(puzzle_input))
