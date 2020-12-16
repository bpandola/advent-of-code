from collections import defaultdict


class Range:

    def __init__(self, range_):
        min_, max_ = range_
        self.min = min_
        self.max = max_


class Rule:

    def __init__(self, name, ranges):
        self.name = name
        self.ranges = []
        for r in ranges:
            self.ranges.append(Range(r))


def parse_input(filename):
    blobs = [blob for blob in open(filename).read().split('\n\n')]
    rules_raw, ticket, nearby = blobs[0], blobs[1], blobs[2]
    parsed_rules = []
    for rule in rules_raw.split('\n'):
        name, range_ = rule.split(': ')
        ranges = []
        for r in range_.split(' or '):
            ranges.append((int(r.split('-')[0]), int(r.split('-')[1])))
        parsed_rules.append(Rule(name, ranges))
    ticket = list(map(int, ticket.split('\n')[1].split(',')))
    tickets_nearby = []
    for near in nearby.split('\n'):
        if near.startswith('nearby'):
            continue
        tickets_nearby.append(list(map(int, near.split(','))))
    return parsed_rules, ticket, tickets_nearby


def validate_tickets(tickets, constraints):
    tickets_validated = tickets[:]
    ticket_error_rate = 0
    for ticket in tickets:
        for value in ticket:
            invalid = True
            for constraint in constraints:
                for r in constraint.ranges:
                    if r.min <= value <= r.max:
                        invalid = False
            if invalid:
                ticket_error_rate += value
                tickets_validated.remove(ticket)
    return tickets_validated, ticket_error_rate


def ascertain_field_order(tickets_validated, constraints):
    possible = defaultdict(list)
    for constraint in constraints:
        for position in range(len(constraints)):
            valid = True
            for ticket in tickets_validated:
                value = int(ticket[position])
                if not any([r.min <= int(value) <= r.max for r in constraint.ranges]):
                    valid = False
                if not valid:
                    break
            if valid:
                possible[constraint.name].append(position)
    # Loop through the possibilities until we only have one possible
    # field name left for each position.  If we encounter a possible
    # positions array with only one value, we know that is correct,
    # so we remove that value from all other possible position arrays.
    while any(len(v) != 1 for v in possible.values()):
        for possible_positions in possible.values():
            if len(possible_positions) == 1:
                value = possible_positions[0]
                for j in possible:
                    if len(possible[j]) > 1 and value in possible[j]:
                        possible[j].remove(value)
    # Now we have dictionary of field names to positions, which we
    # want to translate to an ordered array of field names.
    return [item[0] for item in sorted(possible.items(), key=lambda item: item[1][0])]


if __name__ == '__main__':
    puzzle_input = parse_input('day_16.in')

    # Part 1
    sample_input = parse_input('day_16.in.sample_01')
    _, error_rate = validate_tickets(sample_input[2], sample_input[0])
    assert error_rate == 71

    valid_tickets, error_rate = validate_tickets(puzzle_input[2], puzzle_input[0])
    print(error_rate)

    # Part 2
    sample_input = parse_input('day_16.in.sample_02')
    valid_sample_tickets, _ = validate_tickets(sample_input[2], sample_input[0])
    fields = ascertain_field_order(valid_sample_tickets, sample_input[0])
    assert fields == ['row', 'class', 'seat']

    rules, my_ticket, _ = puzzle_input
    field_order = ascertain_field_order(valid_tickets, rules)
    total = 1
    for i, field in enumerate(field_order):
        if field.startswith('departure'):
            total *= my_ticket[i]
    print(total)
