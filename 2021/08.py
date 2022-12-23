#! /usr/bin/python3

# https://adventofcode.com/2021/day/8

import sys

total = 0
uniq = {2, 4, 3, 7}
for line in sys.stdin:
	(patterns, values) = line.split('|')
	values = values.split()
	for value in values:
		if len(value) in uniq:
			total += 1
print(total)
	
