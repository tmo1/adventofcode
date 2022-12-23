# https://adventofcode.com/2020/day/1

import sys

numbers = [int(line) for line in sys.stdin]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == 2020:
            print(numbers[i] * numbers[j])
            quit()
