# https://adventofcode.com/2024/day/5#part2

from functools import cmp_to_key

def cmp(a, b):
    for r in rules:
        if (r[0], r[1]) == (a, b):
            return -1
        if (r[1], r[0]) == (a, b):
            return 1
    return 0

total, rules = 0, []
for line in open(0):
    line = line.strip()
    if '|' in line:
        rules.append(line.split('|'))
    elif line != '':
        line = line.split(',')
        line_sorted = sorted(line, key=cmp_to_key(cmp))
        if line != line_sorted:
            total += int(line_sorted[len(line) // 2])
print(total)
