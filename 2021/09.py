#! /usr/bin/python3

# https://adventofcode.com/2021/day/9

import sys

total = 0
vents = []
for line in sys.stdin:
	points = list(line.strip())
	nums = []
	for point in points:
		nums.append(int(point))
	vents.append(nums)
for i in range(len(vents)):
	for j in range(len(vents[0])):
		low = 1
		for k in range(-1, 2):
			if i + k < 0 or i + k >= len(vents):
				continue
			for l in range (-1, 2):
				if j + l < 0 or j + l >= len(vents[0]):
					continue
				if k == 0 and l == 0:
					continue
				if vents[i + k][j + l] < vents[i][j]:
					low = 0
					break
		if low == 1:
			total += 1 + vents[i][j]
print(total)
