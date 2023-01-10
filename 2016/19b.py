# https://adventofcode.com/2016/day/19
# this takes 19m12.531s for my input on my Z440

import sys

elves, elf = [i + 1 for i in range(int(sys.stdin.readline()))], 0
while len(elves) != 1:
    n = (elf + (len(elves) // 2)) % len(elves)
    elves.pop(n)
    if n > elf:
        elf += 1
    if elf == len(elves):
        elf = 0
print(elves[0])
