from functools import lru_cache
import sys
sys.setrecursionlimit(1500)
class Rule:

    def __init__(self, raw_rule):
        num, exp = raw_rule.split(': ')
        self.id = int(num)
        self.pattern = []
        self.pattern_or = []
        if exp[0] == "\"":
            self.pattern.append(exp[1])
        elif len(exp.split('|')) > 1:
            one, two = exp.split('|')
            for c in one.split(' '):
                if c == '':
                    continue
                else:
                    self.pattern.append(int(c))
            for c in two.split(' '):
                if c == '':
                    continue
                else:
                    self.pattern_or.append(int(c))
        else:
            for c in exp.split(' '):
                if c == '':
                    continue
                else:
                    self.pattern.append(int(c))


    @property
    def patterns(self):
        return [self.pattern, self.pattern_or]


    def __str__(self):
        return f"{self.id}: {self.pattern} | {self.pattern_or}"

    __repr__ = __str__

def resolve_rules(rules, rule_num):
    rules_ = sorted(rules, key=lambda r: r.id)

    cache = {}
    def resolve_rule(num):
        if num in cache:
            return cache[num]
        return resolve_rule2(num)
    def resolve_rule2(rule_num):
        if rule_num in cache:
            return cache[rule_num]
        try:
            rule = rules_[rule_num]
        except TypeError:
            print('wrf')
        resolved = []
        pat = ''
        patterns = [pat]
        for r in rule.pattern:
            if str(r).isdigit():
                resolved_rule = resolve_rule(r)
                # resolved.append(resolved_rule[0])
                patterns = [p + s for opt in resolved_rule for p in patterns for s in opt]
                # pat += resolved_rule[0]
            else:
                # resolved.append([r])
                #  pat += r
                patterns = [p + r for p in patterns]
        pat_or = ''
        patterns_or = [pat_or]
        for r in rule.pattern_or:
            if str(r).isdigit():
                resolved_rule = resolve_rule(r)
                # resolved.append(resolved_rule[0])
                # pat += resolved_rule[0]
                patterns_or = [p + s for opt in resolved_rule for p in patterns_or for s in opt]
            else:
                # resolved.append([r])
                # pat += r
                patterns_or = [p + r for p in patterns_or]
        if patterns and patterns[0] != '':
            resolved.append(patterns)
        if patterns_or and patterns_or[0] != '':
            resolved.append(patterns_or)
        cache[rule_num] = resolved
        return resolved

    # Maximum recursion depth
    to_resolv = [rul.id for rul in rules if 'a' in rul.pattern or 'b' in rul.pattern]
    while len(cache) != len(rules):
        more = []
        for r in to_resolv:
            resolve_rule(r)
        temp = 0
        while not more:
            # more += [rul.id for rul in rules if (len(set(rul.pattern + rul.pattern_or) - set(to_resolv)) == temp)]
            # temp += 1
            for rul in rules:
                if rul.id in cache:
                    continue
                rule_set = set(rul.pattern + rul.pattern_or)
                diff = rule_set - set(to_resolv)
                for num in rule_set:
                    if num not in cache:
                        break
                else:
                    more.append(rul.id)
                # diff = rule_set - set(to_resolv)
                # if len(diff) == 0:
                #     more.append(rul.id)
            if not more:
                break
        to_resolv += more
        if not more:
            break

    return resolve_rule(rule_num)

def parse_input(filename):
    blobs = open(filename).read().split('\n\n')
    rules = []
    for line in blobs[0].split('\n'):
        rules.append(Rule(line))
    messages = [m for m in blobs[1].split('\n')]
    return rules, messages



if __name__ == '__main__':
    puzzle_input = parse_input('day_19.in')
    sample_input = parse_input('day_19.in.sample')

    inp = puzzle_input
    resolved = resolve_rules(inp[0], 0)
    total = 0
    for m in inp[1]:
        if m in resolved[0]:
            total+=1



    print(total)
