from itertools import combinations
from functools import reduce
puzzle_input = [int(line) for line in open('day_10.in').read().split('\n')]

adapters = puzzle_input[:]
order = [(0,0)]
#print(puzzle_input)
joltage=0
diff_seek = 1
max_rating = max(adapters)+3
adapters.append(max_rating)
while adapters:



    for index, adapter in enumerate(adapters):
        if adapter-joltage == diff_seek:
            joltage = adapter
            order.append((adapter, diff_seek))
            adapters.remove(adapter)
            diff_seek = 0
            break
    diff_seek+=1
    assert 0 < diff_seek < 4


print(order)
print(joltage)
diff_1 = len([(o, v) for (o,v) in order if v == 1])
diff_3 = len([(o, v) for (o,v) in order if v == 3])
print(diff_1*diff_3)

for j in range(1,4):
    print(list(combinations([5,6,7], j)))

adapters = [a for (a,j) in order]
chains = []
index = 1 #  because we start at 0,0
link_left = 0
link_right = 0
chains.append([adapters[0]])
while index < len(adapters):
    sub = [a for a in adapters[index:] if a - adapters[link_left] <= 3]
    if len(sub) == 1:
        chains.append(sub)
        index+=1
        link_left=index-1
        link_right = index
    elif len(sub) > 1:
        length = len(sub)
        link_right+= length
        link_left+=length
        index+=length
        combos = []
        for i in range(1,len(sub)+1):
            pot = list(combinations(sub,i))
            for p in pot:
                if p[0] - adapters[link_left] <= 3:
                    if adapters[link_right] - p[-1] <=3:
                        combos.append(p)
        chains.append(combos)


print(chains)
total = 1
for i in chains:
    total*=len(i)
print(total)




