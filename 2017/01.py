# https://adventofcode.com/2017/day/1
# both parts - see comments below

import sys

digits = sys.stdin.readline().strip()
digits_length = len(digits)
# print(sum([int(digit) for i, digit in enumerate(digits) if digits[i] == digits[(i + 1) % digits_length]])) # part 1
print(sum([int(digit) for i, digit in enumerate(digits) if digits[i] == digits[(i + digits_length // 2) % digits_length]])) # part 2

