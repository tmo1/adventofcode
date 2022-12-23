#! /usr/bin/python3

# https://adventofcode.com/2021/day/3#part2

import sys

lines = []
num_lines = 0

for line in sys.stdin:
	lines.append(list(line.strip()))
	num_lines += 1
	
len_line = len(lines[0])

oxy_lines = ['y'] * len(lines)
pos = 0
remaining = len(lines)
while remaining > 1:
	n = 0
	for i in range(len(lines)):
		if oxy_lines[i] == 'y' and lines[i][pos] == '1':
			n += 1
	crit = '1' if n >= remaining / 2 else '0'
	for i in range(len(lines)):
		if oxy_lines[i] == 'y' and lines[i][pos] != crit:
			oxy_lines[i] = 'n'
			remaining -= 1
	pos += 1

l = 0
for i in range(len(lines)):
	if oxy_lines[i] == 'y':
		l = i
		break

oxy = int(''.join(lines[l]), 2)

co2_lines = ['y'] * len(lines)
pos = 0
remaining = len(lines)
while remaining > 1:
	n = 0
	for i in range(len(lines)):
		if co2_lines[i] == 'y' and lines[i][pos] == '1':
			n += 1
	crit = '0' if n >= remaining / 2 else '1'
	for i in range(len(lines)):
		if co2_lines[i] == 'y' and lines[i][pos] != crit:
			co2_lines[i] = 'n'
			remaining -= 1
	pos += 1

for i in range(len(lines)):
	if co2_lines[i] == 'y':
		l = i
		break

co2 = int(''.join(lines[l]), 2)
print(oxy * co2)
