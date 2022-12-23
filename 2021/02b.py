#! /usr/bin/python3

# https://adventofcode.com/2021/day/2#part2

import sys

x = 0
y = 0
a = 0

for line in sys.stdin:
	(command, n) = line.split()
	n = int(n)
	if command == 'forward':
		x += n
		y += n * a
	if command == 'down':
		a += n
	if command == 'up':
		a -= n

print(x * y)
