#! /usr/bin/python3

# https://adventofcode.com/2021/day/1#part2

import sys

total = 0

p = int(sys.stdin.readline())
q = int(sys.stdin.readline())
r = int(sys.stdin.readline())

for line in sys.stdin:
	s = int(line)
	if s > p:
		total += 1
	p = q
	q = r
	r = s

print(total)
