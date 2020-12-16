
class Range:

    def __init__(self, range_):
        self.min = int(range_.split('-')[0])
        self.max = int(range_.split('-')[1])

class Rule:

    def __init__(self, name, range):
        self.name = name
        self.ranges= []
        for r in range.split(' or '):
            self.ranges.append(Range(r))



def parse_input(filename):
    blobs = [blob for blob in open(filename).read().split('\n\n')]
    rules, ticket, nearby = blobs[0], blobs[1], blobs[2]
    parsed_rules = []
    for rule in rules.split('\n'):
        name, range_ = rule.split(': ')
        parsed_rules.append(Rule(name, range_))
    tickets_nearby = []
    for near in nearby.split('\n'):
        if near.startswith('nearby'):
            continue
        tickets_nearby.append(near.split(','))





    return parsed_rules, tickets_nearby


if __name__ == '__main__':
    puzzle_input = parse_input('day_16.in')
    sample_input = parse_input('day_16.in.sample')

    rules, tickets_nearby =  puzzle_input
    total=0
    for ticket in tickets_nearby[:]:
        for value in ticket:
            invalid = True
            for rule in rules:
                for r in rule.ranges:
                    if r.min <= int(value) <= r.max:
                        invalid = False
            if invalid:
                total += int(value)
                tickets_nearby.remove(ticket)
    print(total)
    my_ticket = [79,193,53,97,137,179,131,73,191,139,197,181,67,71,211,199,167,61,59,127]


    rule_names = [r.name for r in rules]
    name_order = []
    possible = {}
    position = 0
    while position < len(rule_names):
        #position = len(name_order)
        #print(name_order)
        for name in [n for n in rule_names if n not in name_order]:
            possibilities = []
            rule = next(r for r in rules if r.name == name)
            valid = True
            for ticket in tickets_nearby:
                value = int(ticket[position])
                if not any([r.min <= int(value) <= r.max for r in rule.ranges]):
                    valid = False
                if not valid:
                    break
            if valid:
                if name not in possible:
                    possible[name] = []
                possible[name].append(position)
                # break
        position += 1

    ordered = [True for _ in range(len(rule_names))]

    while True:
        for k, v in possible.items():
            if len(v) == 1:
                value = v[0]
                for j in possible:
                    if len(possible[j]) > 1 and value in possible[j]:
                        possible[j].remove(value)
        if all(len(v) == 1 for v in possible.values()):
            break
    name_order = ['' for _ in range(len(possible))]
    for k,v in possible.items():
        name_order[v[0]] = k
    print(name_order)
    total = 1
    for i, name in enumerate(name_order):
        if name.startswith('departure'):
            total *= my_ticket[i]
    print(total)

