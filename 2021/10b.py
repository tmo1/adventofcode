#! /usr/bin/python3

# https://adventofcode.com/2021/day/10#part2

import sys

delims = {'{': '}', '[': ']', '(': ')', '<': '>'}
score = {')': 1, ']': 2, '}': 3, '>': 4}
scores = []

for line in sys.stdin:
	stack = []
	for c in line.strip():
		if c in delims.keys():
			stack.append(c)
		else:
			if c == delims[stack[-1]]:
				stack.pop()
			else:
				stack.append('*')
				break
	if len(stack) > 0 and stack[-1] != '*':
		completion = []
		while len(stack) > 0:
			completion.append(delims[stack[-1]])
			stack.pop()
		total = 0
		for i in range(len(completion)):
			total = (total * 5) + score[completion[i]]
		scores.append(total)

scores.sort()
print(scores[len(scores) // 2])
