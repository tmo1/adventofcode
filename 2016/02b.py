# https://adventofcode.com/2016/day/2#part2

import sys

x, y, code = 0, 2, []
keypad = [['0', '0', '1', '0', '0'], ['0', '2', '3', '4', '0'], ['5', '6', '7', '8', '9'], ['0', 'A', 'B', 'C', '0'],
          ['0', '0', 'D', '0', '0']]
for line in sys.stdin:
    for letter in line:
        match letter:
            case 'U':
                if y > 0 and keypad[y - 1][x] != '0':
                    y -= 1
            case 'D':
                if y < 4 and keypad[y + 1][x] != '0':
                    y += 1
            case 'R':
                if x < 4 and keypad[y][x + 1] != '0':
                    x += 1
            case 'L':
                if x > 0 and keypad[y][x - 1] != '0':
                    x -= 1
    code.append(keypad[y][x])
print(''.join(code))
