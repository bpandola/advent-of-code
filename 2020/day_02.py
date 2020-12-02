

def parse_input(data):
    passwords = []
    for line in data:
        policy, password = line.split(': ')
        policy_range, letter = policy.split(' ')
        min_range, max_range = policy_range.split('-')
        passwords.append({
            'password': password,
            'letter': letter.strip(),
            'min': int(min_range.strip()),
            'max': int(max_range.strip()),
        })
    return passwords


def num_valid(passwords):
    valid = 0
    for meta in passwords:
        password = meta['password']
        letter = meta['letter']
        count = password.count(letter)
        if count >= meta['min'] and count <= meta['max']:
            valid+=1
    return valid

def num_valid2(passwords):
    valid = 0
    for meta in passwords:
        password = meta['password']
        letter = meta['letter']
        if int(password[meta['min']-1] == letter) ^ int(password[meta['max']-1]  == letter):
            valid+=1
    return valid

puzzle_input = [i for i in open('day_02.in').read().split('\n')]
sample_input = [
    '1-3 a: abcde',
'1-3 b: cdefg',
'2-9 c: ccccccccc',
]
inp = parse_input(puzzle_input)
print(num_valid(inp))
print(num_valid2(inp))