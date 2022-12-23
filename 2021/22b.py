#! /usr/bin/python3

# https://adventofcode.com/2021/day/22#part2

import sys

def cubes(c):
	return (c[0][1] - c[0][0] + 1) * (c[1][1] - c[1][0] + 1) * (c[2][1] - c[2][0] + 1)
	
def diff(a, b):
	if (b[0][1] < a[0][0] or b[0][0] > a[0][1]) or (b[1][1] < a[1][0] or b[1][0] > a[1][1]) or (b[2][1] < a[2][0] or b[2][0] > a[2][1]):
		return [a]
	
	regions = []
	if b[0][0] > a[0][0]:
		regions.append([[a[0][0], b[0][0] - 1], [a[1][0], a[1][1]], [a[2][0], a[2][1]]])
	if b[0][1] < a[0][1]:
		regions.append([[b[0][1] + 1, a[0][1]], [a[1][0], a[1][1]], [a[2][0], a[2][1]]])
	
	if b[1][0] > a[1][0]:
		regions.append([[max([a[0][0], b[0][0]]), min(a[0][1], b[0][1])], [a[1][0], b[1][0] - 1], [a[2][0], a[2][1]]])
	if b[1][1] < a[1][1]:
		regions.append([[max([a[0][0], b[0][0]]), min(a[0][1], b[0][1])], [b[1][1] + 1, a[1][1]], [a[2][0], a[2][1]]])
	
	if b[2][0] > a[2][0]:
		regions.append([[max([a[0][0], b[0][0]]), min(a[0][1], b[0][1])], [max([a[1][0], b[1][0]]), min(a[1][1], b[1][1])], [a[2][0], b[2][0] - 1]])
	if b[2][1] < a[2][1]:
		regions.append([[max([a[0][0], b[0][0]]), min(a[0][1], b[0][1])], [max([a[1][0], b[1][0]]), min(a[1][1], b[1][1])], [b[2][1] + 1, a[2][1]]])
	
	return regions

regions = []
for line in sys.stdin:
	o, cube = line.split()
	cube = cube.split(',')
	for i in range(3):
		cube[i] = cube[i][2:].split('..')
		cube[i] = [int(cube[i][0]), int(cube[i][1])]
	regions2 = []
	for r in regions:
		regions2 += diff(r, cube)
	if o == 'on':
		regions2.append(cube)
	regions = regions2

total = 0
for region in regions:
	total += cubes(region)
print(total)
