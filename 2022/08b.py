# https://adventofcode.com/2022/day/8#part2

import sys

trees = []
for line in sys.stdin:
    trees.append([int(n) for n in line.strip()])
y_len = len(trees)
x_len = len(trees[0])


def check_tree(y1, x1):
    a = b = c = d = 0
    for i in range(y1 - 1, -1, -1):
        a += 1
        if trees[i][x1] >= trees[y1][x1]:
            break
    for i in range(x1 - 1, -1, -1):
        b += 1
        if trees[y1][i] >= trees[y1][x1]:
            break
    for i in range(y1 + 1, y_len):
        c += 1
        if trees[i][x1] >= trees[y1][x1]:
            break
    for i in range(x1 + 1, x_len):
        d += 1
        if trees[y1][i] >= trees[y1][x1]:
            break
    return a * b * c * d


most_scenic = 0
for y in range(y_len):
    for x in range(x_len):
        most_scenic = max(most_scenic, check_tree(y, x))
print(most_scenic)
