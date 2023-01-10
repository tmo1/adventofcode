# https://adventofcode.com/2016/day/2

import sys

x, y = 0, 0
for line in sys.stdin:
    for letter in line:
        match letter:
            case 'U':
                y = max(-1, y - 1)
            case 'D':
                y = min(1, y + 1)
            case 'R':
                x = min(1, x + 1)
            case 'L':
                x = max(-1, x - 1)
    print(((y + 1) * 3) + x + 2, end='')
print()
