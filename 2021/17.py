#! /usr/bin/python3

# https://adventofcode.com/2021/day/17

import sys
import re
import math

line = sys.stdin.readline()
# https://stackoverflow.com/a/4289348
nums = re.findall(r'\d+', line)
tx1 = int(nums[0])
tx2 = int(nums[1])
ty1 = - int(nums[2])
ty2 = - int(nums[3])

ymaxmax = 0
discriminant = 1 + (4 * 2 * (ty1 + (((tx2 * (tx2 + 1)) // 2))))
discriminant = math.sqrt(discriminant)
uppery = int(2 + max((-1 + discriminant) / 2, (-1 - discriminant) / 2))

for xvel in range(tx2 + 1):
	for yvel in range(ty1 - 1, uppery):
		(xvelcur, yvelcur) = (xvel, yvel)
		(x, y, ymax) = (0, 0, 0)
		while y >= ty2 and x <= tx2:
			x += xvelcur
			y += yvelcur
			ymax = max(ymax, y)
			if x >= tx1 and x <= tx2 and y >= ty1 and y <= ty2:
				ymaxmax = max(ymax, ymaxmax)
			if xvelcur != 0:
				xvelcur -= 1
			yvelcur -= 1

print(ymaxmax)
