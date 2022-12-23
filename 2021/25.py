#! /usr/bin/python3

# https://adventofcode.com/2021/day/25

import sys

floor = []
for line in sys.stdin:
	floor.append(list(line.strip()))

xlen, ylen = len(floor[0]), len(floor)
flag = False
steps = 0
while flag is False:
	flag = True
	new_floor = [['.' for x in range(xlen)] for y in range(ylen)]
	for y in range(ylen):
		for x in range(xlen):
			if floor[y][x] == '>':
				if floor[y][(x + 1) % xlen] == '.':
					new_floor[y][(x + 1) % xlen] = '>'
					flag = False
				else:
					new_floor[y][x] = '>'
			elif floor[y][x] == 'v':
				new_floor[y][x] = 'v'
	floor = new_floor
	new_floor = [['.' for x in range(xlen)] for y in range(ylen)]
	for y in range(ylen):
		for x in range(xlen):
			if floor[y][x] == 'v':
				if floor[(y + 1) % ylen][x] == '.':
					new_floor[(y + 1) % ylen][x] = 'v'
					flag = False
				else:
					new_floor[y][x] = 'v'
			elif floor[y][x] == '>':
				new_floor[y][x] = '>'
	floor = new_floor
	steps += 1
print(steps)
