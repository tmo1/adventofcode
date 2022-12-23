#! /usr/bin/python3

# https://adventofcode.com/2020/day/18

import re
token_re = re.compile('\d+|[()+*]')

f = open('aoc-input', 'r')
#f = open('sample', 'r')

def solve(i):
	total, j, operator = 0, i, ''
	while j < len(line):
		m = token_re.match(line[j:])
		token = m.group()
		j += len(token)
		if token == '*' or token == '+':
			operator = token
			continue
		if token == ')':
			return [total, j]
		if token == '(':
			s = solve(j)
			n = s[0]
			j = s[1]
		else:
			n = int(token)
		total = n if operator == '' else total + n if operator == '+' else total * n
	return [total, j]
total = 0
while line := f.readline():
	line = ''.join(line.split())
	r = solve(0)
	total += r[0]
print(total)


