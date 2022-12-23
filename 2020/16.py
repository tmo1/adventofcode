#! /usr/bin/python3

# https://adventofcode.com/2020/day/16

import re

f = open('aoc-input', 'r')
#f = open('sample', 'r')
rules = []
p = re.compile('.*: (\d*)-(\d*) or (\d*)-(\d*)')
while (rule := f.readline()) != '\n':
	m = p.match(rule)
	rules.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))))
while f.readline() != 'nearby tickets:\n':
	pass
total = 0
while (line := f.readline()):
	values = line.split(',')
	for value in values:
		valid = 0
		n = int(value)
		for rule in rules:
			if (n >= rule[0] and n <= rule[1]) or (n >= rule[2] and n <= rule[3]):
				valid = 1
				break
		if not valid:
			total += n
print(total)
		
		
		
		
		
		
	
