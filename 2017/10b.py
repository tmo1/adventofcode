# https://adventofcode.com/2017/day/10#part2

import sys

numbers, current, skip, lengths = [n for n in range(256)], 0, 0, [ord(x) for x in sys.stdin.readline().strip()] + [17, 31, 73, 47, 23]
for i in range(64):
    for length in lengths:
        x = current + length
        if x < 256:
            numbers = numbers[:current] + list(reversed(numbers[current:x])) + numbers[x:]
        else:
            x -= 256
            r = list(reversed(numbers[current:] + numbers[:x]))
            numbers = r[256-current:] + numbers[x:current] + r[:256-current]
        current = (current + length + skip) % 256
        skip += 1
for i in range(0, 256, 16):
    x = 0
    for j in range(i, i + 16):
        x ^= numbers[j]
    print(hex(x)[2:] if x > 15 else '0' + hex(x)[2:], end='')
print()
