#! /usr/bin/python3

# https://adventofcode.com/2021/day/20#part2
# this takes a bit over 20 seconds on my W550s for my puzzle input,
# so it must not be quite an optimum solution, according to:
# https://adventofcode.com/2021/about

import sys

algo = sys.stdin.readline()
pixels = set()
y = 0
sys.stdin.readline()
for line in sys.stdin:
	for x in range(len(line) - 1):
		if line[x] == '#':
			pixels.add((x, y))
	y += 1

iterations = 50
known_pixels = [{} for i in range(iterations)]

def calc(x, y, depth):
	if depth == 0:
		return '1' if (x, y) in pixels else '0'
	if (x, y) in known_pixels[depth - 1]:
		return known_pixels[depth - 1][(x, y)]
	n = ''
	for y1 in range(y - 1, y + 2):
		for x1 in range(x - 1, x + 2):
			n += calc(x1, y1, depth - 1)
	n = int(n, 2)
	if algo[n] == '#':
		known_pixels[depth - 1][(x, y)] = '1'
		return '1'
	else:
		known_pixels[depth - 1][(x, y)] = '0'
		return '0'

xmin = min(pixels, key = lambda t: t[0])[0] - iterations - 1
ymin = min(pixels, key = lambda t: t[1])[1] - iterations - 1
xmax = max(pixels, key = lambda t: t[0])[0] + iterations + 1
ymax = max(pixels, key = lambda t: t[1])[1] + iterations + 1
total = 0
for x in range(xmin, xmax):
	for y in range(ymin, ymax):
		if calc(x, y, iterations) == '1':
			total += 1
print(total)
