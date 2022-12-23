#! /usr/bin/python3

# https://adventofcode.com/2020/day/6

f = open('aoc6-input', 'r')
total = 0
first = 1
questions = f.readlines()
questions.append('\n')
for line in questions:
	if first == 1:
		group = {}
	if line == '\n':
		total += len(group)
		first = 1
	else:
		group = set(line.rstrip()) if first == 1 else group & set(line.rstrip())
		first = 0
print(total)

