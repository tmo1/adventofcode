# https://adventofcode.com/2022/day/25

import sys

digit_map = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
digit_reverse_map = {2: '2', 1: '1', 0: '0', 3: '=', 4: '-', 5: '0'}
n = 0
for line in sys.stdin:
    n += sum((5 ** i) * digit_map[digit] for i, digit in enumerate(reversed(line.strip())))
snafu, carry = [], 0
while n > 0:
    x = n % 5 + carry
    snafu.append(digit_reverse_map[x])
    carry = 1 if x > 2 else 0
    n //= 5
print(''.join(reversed(snafu)))
