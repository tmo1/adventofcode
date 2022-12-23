# https://adventofcode.com/2022/day/8

import sys

trees = []
for line in sys.stdin:
    trees.append([int(n) for n in line.strip()])
y_len = len(trees)
x_len = len(trees[0])


def check_tree(y1, x1):
    for i in range(y1):
        if trees[i][x1] >= trees[y1][x1]:
            break
    else:
        return True
    for i in range(x1):
        if trees[y1][i] >= trees[y1][x1]:
            break
    else:
        return True
    for i in range(y1 + 1, y_len):
        if trees[i][x1] >= trees[y1][x1]:
            break
    else:
        return True
    for i in range(x1 + 1, x_len):
        if trees[y1][i] >= trees[y1][x1]:
            break
    else:
        return True
    return False


visible = 0
for y in range(y_len):
    for x in range(x_len):
        if check_tree(y, x):
            visible += 1
print(visible)
