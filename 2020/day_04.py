def parse_input(filename):
    lines = [line.replace('\n', ' ') for line in open(filename).read().split('\n\n')]
    passports = []
    for line in lines:
        passport = {}
        kvs = line.split()
        for kv in kvs:
            key, value = kv.split(':')
            passport[key] = value
        passports.append(passport)
    return passports


def check_constraint(key, value):
    if key == 'byr':
        if len(value) != 4:
            return False
        if not (1920 <= int(value) <= 2002):
            return False
    elif key == 'iyr':
        if len(value) != 4:
            return False
        if not (2010 <= int(value) <= 2020):
            return False
    elif key == 'eyr':
        if len(value) != 4:
            return False
        if not (2020 <= int(value) <= 2030):
            return False
    elif key == 'hgt':
        if value.endswith('cm') or value.endswith('in'):
            if value.endswith('cm'):
                if not (150 <= int(value[:-2]) <= 193):
                    return False
            if value.endswith('in'):
                if not (59 <= int(value[:-2]) <= 76):
                    return False
        else:
            return False
    elif key == 'hcl':
        if value[0] != '#':
            return False
        valid_chars = '#0123456789abcdef'
        for c in value:
            if c not in valid_chars:
                return False
    elif key == 'ecl':
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if value not in colors:
            return False
    elif key == 'pid':
        if len(value) != 9:
            return False
        digits = '0123456789'
        for c in value:
            if c not in digits:
                return False
    return True


class PassportValidator:
    REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    OPTIONAL_FIELDS = ['cid']

    def __init__(self, check_constraints=False):
        self.check_constraints = check_constraints

    def validate(self, passport):
        if self.REQUIRED_FIELDS - set(passport.keys()):
            return False
        if self.check_constraints:
            return all(check_constraint(k, v) for k, v in passport.items())
        return True


if __name__ == '__main__':
    puzzle_input = parse_input('day_04.in')

    # Part 1
    sample_input = parse_input('day_04.in.sample_01')
    pv = PassportValidator()
    assert sum(pv.validate(p) for p in sample_input) == 2
    print(sum(pv.validate(p) for p in puzzle_input))

    # Part 2
    sample_input_invalid = parse_input('day_04.in.sample_02a')
    sample_input_valid = parse_input('day_04.in.sample_02b')
    pv = PassportValidator(check_constraints=True)
    assert sum(pv.validate(p) for p in sample_input_invalid) == 0
    assert sum(pv.validate(p) for p in sample_input_valid) == 4
    print(sum(pv.validate(p) for p in puzzle_input))
