# https://adventofcode.com/2023/day/15

total = 0
for step in open(0).readline().strip().split(','):
    v = 0
    for char in step:
        v += ord(char)
        v *= 17
        v %= 256
    total += v
print(total)
