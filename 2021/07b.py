#! /usr/bin/python3

# https://adventofcode.com/2021/day/7#part2

import sys

line = sys.stdin.readline().split(',')
crabs = {}
for x in line:
	crab = int(x)
	if crab in crabs:
		crabs[crab] += 1
	else:
		crabs[crab] = 1
minfuel = -1
for i in range(min(crabs.keys()), max(crabs.keys()) + 1):
	total = 0
	for crab in crabs.keys():
		total += crabs[crab] * abs(crab - i) * (abs(crab - i) + 1) // 2
	if minfuel == -1 or total < minfuel:
		pos = i
		minfuel = total
print(minfuel)
