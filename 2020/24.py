#! /usr/bin/python3

# https://adventofcode.com/2020/day/24

import re
tiles = {}

f = open('aoc-input', 'r')
#f = open('sample', 'r')
dir_re = re.compile('(e|se|sw|w|nw|ne)')

while line := f.readline().rstrip():
	dirs = dir_re.split(line)
	x, y = 0, 0
	for d in dirs:
		if d == 'e':
			x += 1
		elif d == 'w':
			x -= 1
		elif d == 'ne':
			x += 1
			y -= 1
		elif d == 'sw':
			x -= 1
			y += 1
		elif d == 'nw':
			y -= 1
		elif d == 'se':
			y += 1
	if (x,y) in tiles:
		tiles[(x,y)] = 1 - tiles[(x,y)]
	else:
		tiles[(x,y)] = 1

total = 0
for tile in tiles:
	total += tiles[tile]
print(total)
	
