#! /usr/bin/python3

# https://adventofcode.com/2021/day/20

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

def calc(x, y, depth):
	if depth == 0:
		return '1' if (x, y) in pixels else '0'
	n = ''
	for y1 in range(y - 1, y + 2):
		for x1 in range(x - 1, x + 2):
			n += calc(x1, y1, depth - 1)
	n = int(n, 2)
	return '1' if algo[n] == '#' else '0'

xmin = min(pixels, key = lambda t: t[0])[0] - 10
ymin = min(pixels, key = lambda t: t[1])[1] - 10
xmax = max(pixels, key = lambda t: t[0])[0] + 10
ymax = max(pixels, key = lambda t: t[1])[1] + 10
total = 0
for x in range(xmin, xmax):
	for y in range(ymin, ymax):
		if calc(x, y, 2) == '1':
			total += 1
print(total)
