#! /usr/bin/python3

# https://adventofcode.com/2021/day/10

import sys

delims = {'{': '}', '[': ']', '(': ')', '<': '>'}
score = {')': 3, ']': 57, '}': 1197, '>': 25137}
total = 0

for line in sys.stdin:
	stack = []
	for c in line.strip():
		if c in delims.keys():
			stack.append(c)
		else:
			if c == delims[stack[-1]]:
				stack.pop()
			else:
				total += score[c]
				break
print(total)
