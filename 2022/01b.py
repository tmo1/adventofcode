# https://adventofcode.com/2022/day/1#part2

import sys

elves = []
calories = max_calories = 0
for line in sys.stdin:
    if line == "\n":
        elves.append(calories)
        calories = 0
    else:
        calories += int(line)
elves.append(calories)
print(sum(sorted(elves)[-3:]))
