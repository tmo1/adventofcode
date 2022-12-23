# https://adventofcode.com/2022/day/1

import sys

calories = max_calories = 0
for line in sys.stdin:
    if line == "\n":
        max_calories = max(max_calories, calories)
        calories = 0
    else:
        calories += int(line)
max_calories = max(max_calories, calories)
print(max_calories)