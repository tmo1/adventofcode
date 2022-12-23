#! /usr/bin/python3

# https://adventofcode.com/2020/day/18

import re
token_re = re.compile('(\d+|[()+*])(.*)')
f = open('aoc-input', 'r')
#f = open('sample', 'r')

def reduce(expr):
	i = 0
	while i < len(expr):
		if expr[i] == '(':
			expr = expr[:i] + reduce(expr[i+1:])
		elif expr[i] == ')':
			return [solve(expr[:i])] + expr[i+1:]
		i += 1
	return solve(expr)

def solve(expr):
	i = 0
	while i < len(expr):
		if expr[i] == '+':
			expr = expr[:i-1] + [expr[i-1] + expr[i+1]] + expr[i+2:]
			continue
		i += 1
	i = 0
	while i < len(expr):
		if expr[i] == '*':
			expr = expr[:i-1] + [expr[i-1] * expr[i+1]] + expr[i+2:]
			continue
		i += 1
	return expr[0]

total = 0
while line := f.readline():
	expr = []
	line = ''.join(line.split())
	while line:
		m = token_re.match(line)
		expr.append(int(m.group(1)) if m.group(1).isdigit() else m.group(1))
		line = m.group(2)
	#print('tokenization:', expr)
	total += reduce(expr)

print(total)
