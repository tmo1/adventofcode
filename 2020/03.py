#! /usr/bin/python3

# https://adventofcode.com/2020/day/3

f = open('aoc3-input', 'r')
forest = f.readlines()
width = len(forest[0]) - 1
x, y, trees = 0, 0, 0
while 1:
	y += 1
	if y == len(forest):
		break
	x = (x + 3) % width
	if forest[y][x] == '#':
		trees += 1
#		print('Tree!')
#	else:
#		print('No tree.')
print(trees)
