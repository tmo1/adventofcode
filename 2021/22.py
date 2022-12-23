#! /usr/bin/python3

# https://adventofcode.com/2021/day/22

import sys

on = set()
for line in sys.stdin:
	o, cube = line.split()
	cube = cube.split(',')
	for i in range(3):
		cube[i] = cube[i][2:].split('..')
		cube[i] = [int(cube[i][0]), int(cube[i][1])]
	for x in range(max(cube[0][0], -50), min(cube[0][1] + 1, 51)):
		for y in range(max(cube[1][0], -50), min(cube[1][1] + 1, 51)):
			for z in range(max(cube[2][0], -50), min(cube[2][1] + 1, 51)):
				if o == 'on':
					on.add((x, y, z))
				else:
					on.discard((x, y, z))
print(len(on))
