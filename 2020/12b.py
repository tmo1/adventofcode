#! /usr/bin/python3

# https://adventofcode.com/2020/day/12

f = open('aoc-input', 'r')
#f = open('sample', 'r')
x, y, l, m = 10, 1, 0, 0
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
		for k in range(v // 90):
			x, y = y ,-x
	elif a == 'L':
		for k in range(v // 90):
			x, y = -y ,x
	elif a == 'F':
		l, m = l + (x * v), m + (y * v)
print(abs(l) + abs(m))
