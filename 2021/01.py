#! /usr/bin/python3

# https://adventofcode.com/2021/day/1

import sys

total = 0
prev = int(sys.stdin.readline())

for line in sys.stdin:
	n = int(line)
	if n > prev:
		total += 1
	prev = n

print(total)
