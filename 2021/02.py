#! /usr/bin/python3

# https://adventofcode.com/2021/day/2

import sys

x = 0
y = 0

for line in sys.stdin:
	(command, n) = line.split()
	n = int(n)
	if command == 'forward':
		x += n
	if command == 'down':
		y += n
	if command == 'up':
		y -= n

print(x * y)
