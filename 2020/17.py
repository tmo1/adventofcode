#! /usr/bin/python3

# https://adventofcode.com/2020/day/17

f = open('aoc-input', 'r')
#f = open('sample', 'r')
init = f.readlines()
x, y, z = 12 + len(init[0]), 12 + len(init), 13
grid = [[['.' for k in range(z)] for j in range(y)] for i in range(x)]

for i in range(len(init)):
	for j in range(len(init[i]) - 1):
		grid[j + 6][i + 6][6] = init[i][j]

for c in range(6):
	new_grid = [[['.' for k in range(13)] for j in range(y)] for i in range(x)]
	for i in range(x):
		for j in range(y):
			for k in range(z):
				neighbors = 0
				for l in [i - 1, i, i + 1]:
					if l < 0 or l == x:
						continue
					for m in [j - 1, j, j + 1]:
						if m < 0 or m == y:
							continue
						for n in [k - 1, k, k + 1]:
							if n < 0 or n == z or (l == i and m == j and n == k):
								continue
							if grid[l][m][n] == '#':
								neighbors += 1
				if (neighbors == 3) or (grid[i][j][k] == '#' and neighbors == 2):
					new_grid[i][j][k] = '#'
	grid = new_grid
	
total = 0
for i in range(x):
	for j in range(y):
		for k in range(z):
			if grid[i][j][k] == '#':
				total += 1
print(total)
