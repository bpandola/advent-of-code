import string

PRIORITIES = {}
for priority, key in enumerate(string.ascii_lowercase + string.ascii_uppercase, start=1):
    PRIORITIES[key] = priority
    priority += 1

filename = 'day_03.in.sample_01'
filename = 'day_03.in'
lines = open(filename).read().split('\n')
total = 0
for line in lines:

    comp_1, comp_2 = set(line[:int(len(line)/2)]), set(line[int(len(line)/2):])
    duplicates = comp_1.intersection(comp_2)
    assert len(duplicates) == 1
    for d in duplicates:
        total += PRIORITIES[d]

print(total)


total = 0
comp_1, comp_2 = set(),set()
for index, line in enumerate(lines, start=1):

    if index % 3 == 0:
        s1, s2, s3 = set(lines[index-3]),set(lines[index-2]),set(lines[index-1])
        duplicates = s1.intersection(s2.intersection(s3))
        assert len(duplicates) == 1
        for d in duplicates:
            total += PRIORITIES[d]
        comp_1, comp_2 = set(), set()

print(total)


