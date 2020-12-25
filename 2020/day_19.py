def parse_input(filename, part_two=False):
    rules, messages = open(filename).read().split('\n\n')
    parsed_rules = {}
    for rule in rules.split('\n'):
        rule_num, options = rule.split(': ')
        if int(rule_num) == 8 and part_two:
            parsed_rules[int(rule_num)] = "42 | 42 8"
        elif int(rule_num) == 11 and part_two:
            parsed_rules[int(rule_num)] = "42 31 | 42 11 31"
        else:
            parsed_rules[int(rule_num)] = options
    return [msg for msg in messages.split('\n')], parsed_rules


def matches_rule(message, rule_num, rules):
    # Shamelessly stolen from `geohot`.  Thanks George!  You're a genius.
    def consume(fragment, rn):
        rule = rules[rn]
        if rule[0] == '"':  # terminal symbol
            ch = rule.strip('"')
            if fragment.startswith(ch):
                return [len(ch)]
            else:
                return []

        bret = []
        for option in rule.split(' | '):
            acc = [0]
            for rn in option.split(' '):
                nacc = []
                rn = int(rn)
                for ac in acc:
                    ret = consume(fragment[ac:], rn)
                    for c in ret:
                        nacc.append(c + ac)
                acc = nacc
            bret += acc
        return bret

    return consume(message, rule_num)


def num_matches(messages, rules):
    total_matches = 0
    for message in messages:
        total_matches += len(message) in matches_rule(message, 0, rules)
    return total_matches


if __name__ == '__main__':
    # Part 1
    sample_input = parse_input('day_19.in.sample_01')
    assert num_matches(sample_input[0], sample_input[1]) == 2

    puzzle_input = parse_input('day_19.in')
    print(num_matches(puzzle_input[0], puzzle_input[1]))

    # Part 2
    sample_input = parse_input('day_19.in.sample_02', part_two=True)
    assert num_matches(sample_input[0], sample_input[1]) == 12

    puzzle_input = parse_input('day_19.in', part_two=True)
    print(num_matches(puzzle_input[0], puzzle_input[1]))
