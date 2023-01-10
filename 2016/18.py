# https://adventofcode.com/2016/day/18
# both parts - see comment below
# this takes nearly 20 seconds for part 2 for my input on my W550s

import sys

rows = [[c for c in sys.stdin.readline().strip()]]
# set the value in the following line to 39 for part 1 and 399999 for part 2
for i in range(399999):
    row = rows[i]
    new_row = []
    for j in range(len(row)):
        left = '.' if j == 0 or row[j - 1] == '.' else '^'
        center = row[j]
        right = '.' if j == len(row) - 1 or row[j + 1] == '.' else '^'
        new_row.append('^' if (left == '^' and right == '.') or (left == '.' and right == '^') else '.')
    rows.append(new_row)
print(sum([sum([1 for x in row if x == '.']) for row in rows]))
