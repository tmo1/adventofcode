# https://adventofcode.com/2022/day/20#part2

import sys

class Number:
    def __init__(self, num, left, right):
        self.num = num
        self.left = left
        self.right = right
    modulo = None
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
total = len(numbers)
for n in numbers:
    multiplied = n.num * 811589153
    n.modulo = multiplied % (total - 1) if n.num > 0 else -(-multiplied % (total - 1))
    n.num = multiplied
for i in range(10):
    for n in numbers:
        if n.num != 0:
            l = n.left
            r = n.right
            l.right = r
            r.left = l
            if n.num > 0:
                new_l = l
                for j in range(n.modulo):
                    new_l = new_l.right
                new_r = new_l.right
                n.left = new_l
                n.right = new_r
                new_l.right = n
                new_r.left = n
            else:
                new_r = r
                for j in range(-n.modulo):
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
