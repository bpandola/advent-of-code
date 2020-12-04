
fields =  [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid',
]

def validator(name, value):
    if name == 'byr':
        if len(value) != 4:
            return False
        if not (1920 <= int(value) <= 2002):
            return False
    elif name == 'iyr':
        if len(value) != 4:
            return False
        if not (2010 <= int(value) <= 2020):
            return False
    elif name == 'eyr':
        if len(value) != 4:
            return False
        if not (2020 <= int(value) <= 2030):
            return False
    elif name == 'hgt':
        if value.endswith('cm') or value.endswith('in'):
            if value.endswith('cm'):
                if not (150 <= int(value[:-2]) <= 193):
                    return False
            if value.endswith('in'):
                if not (59 <= int(value[:-2]) <= 76):
                    return False
        else:
            return False
    elif name == 'hcl':
        if value[0] != '#':
            return False
        valid_chars = '#0123456789abcdef'
        for c in value:
            if c not in valid_chars:
                return False
    elif name == 'ecl':
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if value not in colors:
            return False
    elif name == 'pid':
        if len(value) != 9:
            return False
        digits = '0123456789'
        for c in value:
            if c not in digits:
                return False
    return True


valid = 0
p = [line for line in open('day_04.in').read().split('\n\n')]
p = [line.replace('\n', ' ') for line in p]
# print(p)
for passport in p:
    missing_field = 0
    missing_cid = False
    for field in fields:
        if field not in passport:
            missing_field += 1
            if field == 'cid':
                missing_cid = True
    if missing_field == 1 and missing_cid or (missing_field == 0):
        pass_fields = passport.split(' ')
        for pf in pass_fields:
            name, value = pf.split(':')
            if not validator(name, value):
                break
        else:
            valid += 1

print(valid)

# print(p)