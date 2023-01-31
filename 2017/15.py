# https://adventofcode.com/2017/day/15
# This took about 22s for my input on my W550s

puzzle = open(0)
n, total, seen, a, b = 0, 0, {}, int(puzzle.readline().split()[-1]), int(puzzle.readline().split()[-1])
while n < 40000000:
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if a & 65535 == b & 65535:
        total += 1
    n += 1
print(total)
