# https://adventofcode.com/2017/day/15#part2
# Although my solution for part 1 took about 22s for my input on my W550s, this solution for part 2, which uses
# essentially the same straightforward approach to the puzzle, took only about 14s

puzzle = open(0)
n, total, seen, a, b = 0, 0, {}, int(puzzle.readline().split()[-1]), int(puzzle.readline().split()[-1])
while n < 5000000:
    while True:
        a = (a * 16807) % 2147483647
        if a & 3 == 0:
            break
    while True:
        b = (b * 48271) % 2147483647
        if b & 7 == 0:
            break
    if a & 65535 == b & 65535:
        total += 1
    n += 1
print(total)
