#! /usr/bin/python3

# https://adventofcode.com/2020/day/24

import re
tiles = set()

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
		tiles.remove((x,y))
	else:
		tiles.add((x,y))

def count(tile):
	total = 0
	if (tile[0] + 1, tile[1]) in tiles:
		total += 1
	if (tile[0] - 1, tile[1]) in tiles:
		total += 1
	if (tile[0] + 1, tile[1] - 1) in tiles:
		total += 1
	if (tile[0] - 1, tile[1] + 1) in tiles:
		total += 1
	if (tile[0], tile[1] - 1) in tiles:
		total += 1
	if (tile[0], tile[1] + 1) in tiles:
		total += 1
	return total
		
for i in range(100):
	new_tiles = set()
	for tile in tiles:
		neighbors = count(tile)
		if neighbors == 1 or neighbors == 2:
			new_tiles.add(tile)
		for ntile in [(tile[0] + 1, tile[1]), (tile[0] - 1, tile[1]), (tile[0] + 1, tile[1] - 1), (tile[0] - 1, tile[1] + 1), (tile[0], tile[1] - 1), (tile[0], tile[1] + 1)]:
			if ntile not in tiles and count(ntile) == 2:
				new_tiles.add(ntile)
	tiles = new_tiles
	
print(len(tiles))
