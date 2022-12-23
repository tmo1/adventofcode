# https://adventofcode.com/2022/day/9#part2

import sys

knots = [[0, 0] for i in range(10)]
visited = {(0, 0)}
for line in sys.stdin:
    line = line.split()
    for i in range(int(line[1])):
        match line[0]:
            case 'U':
                knots[0][1] -= 1
            case 'D':
                knots[0][1] += 1
            case 'R':
                knots[0][0] += 1
            case 'L':
                knots[0][0] -= 1
        for j in range(1, 10):
            if abs(knots[j - 1][0] - knots[j][0]) == 2:
                knots[j][0] += ((knots[j - 1][0] - knots[j][0]) // 2)
                if abs(knots[j - 1][1] - knots[j][1]) == 2:
                    knots[j][1] += ((knots[j - 1][1] - knots[j][1]) // 2)
                else:
                    knots[j][1] = knots[j - 1][1]
            if abs(knots[j - 1][1] - knots[j][1]) == 2:
                knots[j][1] += ((knots[j - 1][1] - knots[j][1]) // 2)
                knots[j][0] = knots[j - 1][0]
        visited.add((knots[9][0], knots[9][1]))
print(len(visited))
