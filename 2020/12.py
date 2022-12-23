#! /usr/bin/python3

# https://adventofcode.com/2020/day/12

f = open('aoc-input', 'r')
#f = open('sample', 'r')
x, y, d, = 0, 0, 0
while i := f.readline():
	a, v = i[0], int(i[1:])
	if a == 'N':
		y += v
	elif a == 'S':
		y -= v
	elif a == 'E':
		x += v
	elif a == 'W':
		x -= v
	elif a == 'R':
		d = (d + v) % 360
	elif a == 'L':
		d = (d - v) % 360
	elif a == 'F':
		if d == 0:
			x += v
		elif d == 90:
			y -= v
		elif d == 180:
			x -= v
		elif d == 270:
			y += v
print(abs(x) + abs(y))
