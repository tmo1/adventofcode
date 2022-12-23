#! /usr/bin/python3

# https://adventofcode.com/2021/day/11

import sys

total = 0
grid = []

for line in sys.stdin:
	octos = []
	for i in range(10):
		octos.append(int(line[i]))
	grid.append(octos)

def flash(i, j):
	grid[i][j] = -1
	global total
	total += 1
	for k in range(-1, 2):
		if i + k >= 0 and i + k < 10:
			for l in range(-1, 2):
				if j + l >= 0 and j + l < 10 and (k != 0 or l != 0) and grid[i + k][j + l] < 10 and grid[i + k][j + l] > -1:
					grid[i + k][j + l] += 1
					if grid[i + k][j + l] == 10:
						flash(i + k, j + l)

for steps in range(100):
	for i in range(10):
		for j in range(10):
			grid[i][j] += 1
	for i in range(10):
		for j in range(10):
			if grid[i][j] == 10:
				flash(i, j)
	for i in range(10):
		for j in range(10):
			if grid[i][j] == -1:
				grid[i][j] = 0
print(total)
