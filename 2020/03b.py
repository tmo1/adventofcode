#! /usr/bin/python3

# https://adventofcode.com/2020/day/3

f = open('aoc3-input', 'r')
forest = f.readlines()
width = len(forest[0]) - 1
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total = 1
for slope in slopes:
	x, y, trees = 0, 0, 0
	while 1:
		y += slope[1]
		if y >= len(forest):
			break
		x = (x + slope[0]) % width
		if forest[y][x] == '#':
			trees += 1
	total *= trees
print(total)
