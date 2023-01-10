# https://adventofcode.com/2016/day/7

import sys

n = 0
for line in sys.stdin:
    prev, hypernet, good_abba = [], False, False
    for char in line.strip():
        match char:
            case '[':
                prev = []
                hypernet = True
            case ']':
                prev = []
                hypernet = False
            case other:
                prev.append(char)
                if len(prev) == 5:
                    prev.pop(0)
                if len(prev) == 4 and prev[0] == char and prev[0] != prev[1] and prev[1] == prev[2]:
                    if hypernet:
                        break
                    good_abba = True
    else:
        if good_abba:
            n += 1
print(n)
