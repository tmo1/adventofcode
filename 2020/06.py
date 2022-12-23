#! /usr/bin/python3

# https://adventofcode.com/2020/day/6

f = open('aoc6-input', 'r')
total = 0
group = {}
questions = f.readlines()
questions.append('\n')
for line in questions:
	if line == '\n':
		total += len(group)
		group = {}
	else:
		for letter in line.rstrip():
			group[letter] = 1
print(total)

