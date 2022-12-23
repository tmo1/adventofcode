# https://adventofcode.com/2022/day/20

import sys

class Number:
    def __init__(self, num, left, right):
        self.num = num
        self.left = left
        self.right = right
prev = None
numbers = []
for line in sys.stdin:
    number = int(line)
    if prev is None:
        n = Number(number, None, None)
    else:
        n = Number(number, prev, None)
        prev.right = n
    if number == 0:
        zero = n
    prev = n
    numbers.append(n)
numbers[0].left = n
n.right = numbers[0]
for n in numbers:
    if n.num != 0:
        l = n.left
        r = n.right
        l.right = r
        r.left = l
        if n.num > 0:
            new_l = l
            for i in range(n.num):
                new_l = new_l.right
            new_r = new_l.right
            n.left = new_l
            n.right = new_r
            new_l.right = n
            new_r.left = n
        else:
            new_r = r
            for i in range(-n.num):
                new_r = new_r.left
            new_l = new_r.left
            n.left = new_l
            n.right = new_r
            new_r.left = n
            new_l.right = n
n = zero
total = 0
for i in range(3):
    for j in range(1000):
        n = n.right
    total += n.num
print(total)
