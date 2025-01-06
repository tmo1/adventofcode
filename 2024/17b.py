 # https://adventofcode.com/2024/day/17#part2

import re

numbers = [int(n) for n in re.findall(r"\d+", open(0).read())][-1:2:-1]

def next_number(a, i):
    if i == len(numbers):
        print(a)
        quit()
    a2 = a << 3
    for b in range(8):
        if (b ^ (a2 + b >> (b ^ 7))) % 8 == numbers[i]: next_number(a2 + b, i + 1)

next_number(0, 0)
