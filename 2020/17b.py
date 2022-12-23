#! /usr/bin/python3

# https://adventofcode.com/2020/day/17

f = open('aoc-input', 'r')
#f = open('sample', 'r')
init = f.readlines()
x, y, z, w = 12 + len(init[0]), 12 + len(init), 13, 13
grid = [[[['.' for l in range(w)] for k in range(z)] for j in range(y)] for i in range(x)]

for i in range(len(init)):
	for j in range(len(init[i]) - 1):
		grid[j + 6][i + 6][6][6] = init[i][j]

for c in range(6):
	new_grid = [[[['.' for l in range(w)] for k in range(z)] for j in range(y)] for i in range(x)]
	for i in range(x):
		for j in range(y):
			for k in range(z):
				for l in range(w):
					neighbors = 0
					for m in [i - 1, i, i + 1]:
						if m < 0 or m == x:
							continue
						for n in [j - 1, j, j + 1]:
							if n < 0 or n == y:
								continue
							for o in [k - 1, k, k + 1]:
								if o < 0 or o == z:
									continue
								for p in [l - 1, l, l + 1]:
									if p < 0 or p == w or (m == i and n == j and o == k and p == l):
										continue
									if grid[m][n][o][p] == '#':
										neighbors += 1
					if (neighbors == 3) or (grid[i][j][k][l] == '#' and neighbors == 2):
						new_grid[i][j][k][l] = '#'
	grid = new_grid
	
total = 0
for i in range(x):
	for j in range(y):
		for k in range(z):
			for l in range(w):
				if grid[i][j][k][l] == '#':
					total += 1
print(total)
