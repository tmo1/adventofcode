# https://adventofcode.com/2020/day/1#part2

import sys

numbers = [int(line) for line in sys.stdin]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print(numbers[i] * numbers[j] * numbers[k])
                quit()
