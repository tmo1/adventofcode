# https://adventofcode.com/2016/day/19

import sys


class Elf:
    def __init__(self, num, next_elf):
        self.num = num
        self.next_elf = next_elf


first_elf = elf = Elf(1, None)
for i in range(2, int(sys.stdin.readline()) + 1):
    new_elf = Elf(i, None)
    elf.next_elf = new_elf
    elf = new_elf
elf.next_elf = first_elf
elf = first_elf
while elf.next_elf != elf:
    elf.next_elf = elf.next_elf.next_elf
    elf = elf.next_elf
print(elf.num)
