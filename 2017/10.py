# https://adventofcode.com/2017/day/10

import sys

numbers, current, skip = [n for n in range(256)], 0, 0
for length in sys.stdin.readline().split(','):
    length = int(length)
    x = current + length
    if x < 256:
        numbers = numbers[:current] + list(reversed(numbers[current:x])) + numbers[x:]
    else:
        x -= 256
        r = list(reversed(numbers[current:] + numbers[:x]))
        numbers = r[-x:] + numbers[x:current] + r[:-x]
    current = (current + length + skip) % 256
    skip += 1
print(numbers[0] * numbers[1])
