from functools import lru_cache
import sys
sys.setrecursionlimit(1500)
class Rule:

    def __init__(self, raw_rule):
        num, exp = raw_rule.split(': ')
        self.id = int(num)
        self.loop =  False
        self.pattern = []
        self.pattern_or = []
        self.resolved = []
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

def resolve_rules(rules, rule_num, messages=None):
    rules_ = sorted(rules, key=lambda r: r.id)

    cache = {}
    def resolve_rule(num):
        if num in cache:
            return cache[num]
        return resolve_rule2(num)
    def resolve_rule2(rule_num, resolve_loop=False):
        if rule_num in cache:
            return cache[rule_num]
        try:
            rule = rules_[rule_num]
        except (TypeError, IndexError):
            rule = next(r for r in rules_ if r.id == rule_num)
        resolved = []
        pat = ''
        patterns = [pat]
        for r in rule.pattern:
            if rule.loop and not resolve_loop:
                break
            if str(r).isdigit():
                resolved_rule = resolve_rule(r)
                # resolved.append(resolved_rule[0])

                # This is special cased for *my* input
                if rule.loop:
                    patterns = [p + '{' + s + '}' for opt in resolved_rule for p in patterns for s in opt]
                else:
                    patterns = [p + s for opt in resolved_rule for p in patterns for s in opt]
                # pat += resolved_rule[0]
            else:
                # resolved.append([r])
                #  pat += r
                patterns = [p + r for p in patterns]
        pat_or = ''
        patterns_or = [pat_or]
        for r in rule.pattern_or:
            if rule.loop and resolve_loop:
                break
            if int(r) == rule.id:
                resolved_rule = resolve_rule2(r, resolve_loop=True)
                patterns_or = [p + s for opt in resolved_rule for p in patterns_or for s in opt]
            elif str(r).isdigit():
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
        more += [rul.id for rul in rules if (len(set(rul.pattern + rul.pattern_or) - set(to_resolv)) == 0) and rul.id not in cache]
        # temp = 0
        # while not more:
        #     # more += [rul.id for rul in rules if (len(set(rul.pattern + rul.pattern_or) - set(to_resolv)) == temp)]
        #     # temp += 1
        #     for rul in rules:
        #         if rul.id in cache:
        #             continue
        #         rule_set = set(rul.pattern + rul.pattern_or)
        #         diff = rule_set - set(to_resolv)
        #         for num in rule_set:
        #             if num not in cache:
        #                 break
        #         else:
        #             more.append(rul.id)
        #         # diff = rule_set - set(to_resolv)
        #         # if len(diff) == 0:
        #         #     more.append(rul.id)
        #     if not more:
        #         break
        to_resolv += more
        if not more:
            break

    missing = [r.id for r in rules if r.id not in cache and r.id != 0]
    assert all(ru.loop for ru in rules if ru.id in missing)
    # if missing:
    #     for num in missing:
    #         resolve_rule(num)
    rule_0 = next(r for r in rules if r.id == 0)

    # messages = [
    #    'bbabbbbaabaabba',
    #    'babbbbaabbbbbabbbbbbaabaaabaaa',
    #    'aaabbbbbbaaaabaababaabababbabaaabbababababaaa',
    #    'bbbbbbbaaaabbbbaaabbabaaa',
    #    'bbbababbbbaaaaaaaabbababaaababaabab',
    #    'ababaaaaaabaaab',
    #    'ababaaaaabbbaba',
    #    'baabbaaaabbaaaababbaababb',
    #    'abbbbabbbbaaaababbbbbbaaaababb',
    #    'aaaaabbaabaaaaababaa',
    #    'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa',
    #    'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba',
    # ]
    prefix = resolve_rule(8)
    suffix = resolve_rule(11)
    valids = []
    for msg in messages:
        print(msg)
        valid = False
        for pre in prefix[0]:
            t1, t2 = pre.split('{')
            t2 = t2[:-1]
            if not msg.startswith(t1):
                continue
            temp = msg[len(t1):]
            if not temp.startswith(t2):
                continue
            while temp.startswith(t2):
                temp = temp[len(t2):]
            valid = True
            break
        if not valid:
            continue
        valid = False
        for suf in suffix[0]:
            k1, k2 = suf.split('}{')
            t1, t2 = k1.split('{')
            t3, t4 = k2.split('}')
            if not temp.endswith(t4):
                continue
            try:
                index = msg.rfind(t1)
            except ValueError:
                continue
            if index == -1:
                continue
            temp = msg[index:]
            if not temp.startswith(t1):
                continue
            infinite = temp[len(t1):-len(t4)]
            valid = True
            while infinite:
                if infinite.startswith(t2) or infinite.endswith(t3):
                    if infinite.startswith(t2):
                        infinite = infinite[len(t2):]
                    if infinite.endswith(t3):
                        infinite = infinite[:-len(t3)]
                else:
                    valid = False
                    break

                valid = True
            if valid:
                break

        if valid:
            valids.append(msg)

    print(valids)
    print(len(valids))



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
    sample_input2 = parse_input('day_19.in.sample_02')

    inp = puzzle_input
    # resolved = resolve_rules(inp[0], 0)
    # total = 0
    # for m in inp[1]:
    #     if m in resolved[0]:
    #         total+=1
    # print(total)

    # Part 2
    rule_8 = next(rule for rule in inp[0] if rule.id == 8)
    rule_11 = next(rule for rule in inp[0] if rule.id == 11)
    rule_8.loop = True
    rule_8.pattern_or = [42, 8]
    rule_11.loop = True
    rule_11.pattern_or = [42,11,31]
    resolved = resolve_rules(inp[0], 0, inp[1])
    total = 0
    for m in inp[1]:
        if m in resolved[0]:
            total+=1
    print(total)


