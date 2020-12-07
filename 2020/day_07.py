from functools import reduce

puzzle_input = [line for line in open('day_07.in').read().split('\n')]
bags = {}
for line in puzzle_input:
    outer, contents = line.split(' bags contain')
    outer = outer.strip()
    contents = contents.split(',')
    bags[outer] = {}
    for bag in contents:
        content = bag.split(' ')
        if content[1] == 'no':
            continue
        bag_name = content[2] + ' ' + content[3]
        bags[outer][bag_name] = int(content[1])

contains_gold = []
def visit(bag, bags, path=None):
    if path is None:
        path = [bag]
    for b in bags[bag]:
        bpath = visit(b, bags, path + [b])
        # Stop if we hit gold
        if bpath[-1] == 'shiny gold':
            for i in range(len(bpath)-1):
                if bpath[i] not in contains_gold:
                    contains_gold.append(bpath[i])
    return path
gold_paths = []
def visit_gold(bag, bags, path=None):
    if path is None:
        path = [bag]
    for b in bags[bag]:
        bpath = visit_gold(b, bags, path + [b] + [bags[bag][b]])
        # Avert thy gaze!!!
        gold_paths.append(bpath[::2][1:])
    return path
containers = []
for bag in bags:
    path = visit(bag, bags)
print(len(contains_gold))

path = visit_gold('shiny gold', bags)
total_bags = 0
for bleh in gold_paths:
    sub_total = reduce(lambda x, y: x * y, bleh)
    total_bags += sub_total
print(total_bags)
