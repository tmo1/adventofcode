# https://adventofcode.com/2024/day/5#part2

from functools import cmp_to_key

total, rules = 0, set()
for line in open(0):
    line = line.strip()
    if '|' in line:
        rules.add(tuple(line.split('|')))
    elif line != '':
        line = line.split(',')
        line_sorted = sorted(line, key=cmp_to_key(lambda x, y: -1 if (x, y) in rules else 1 if (y, x) in rules else 0))
        if line != line_sorted:
            total += int(line_sorted[len(line) // 2])
print(total)
