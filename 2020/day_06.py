from string import ascii_lowercase
print(ascii_lowercase)
lines = [line.split('\n') for line in open('day_06.in').read().split('\n\n')]


total = 0
for group in lines:
    yeses = set()
    for person in group:
        for c in person:
            yeses.add(c)
    total += len(yeses)
print(total)


total = 0
for group in lines:
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if all([c in person for person in group]):
            total += 1
print(total)
