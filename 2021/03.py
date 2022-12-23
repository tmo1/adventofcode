#! /usr/bin/python3

# https://adventofcode.com/2021/day/3

import sys

lines = []
num_lines = 0

for line in sys.stdin:
	lines.append(list(line.strip()))
	num_lines += 1
	
len_line = len(lines[0])
gamma = ['0'] * len_line
epsilon = ['0'] * len_line
for pos in range(len_line):
	n = 0
	for line in lines:
		if line[pos] == '1':
			n += 1
	if n > num_lines / 2:
		gamma[pos] = '1'
	else:
		epsilon[pos] = '1'
			
print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))
