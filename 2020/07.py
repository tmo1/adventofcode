#! /usr/bin/python3

# https://adventofcode.com/2020/day/7

f = open('aoc7-input', 'r')
rules = {}
bags = []
while line := f.readline():
	words = line.split(' ')
	rules[words[0] + words[1]] = []
	if words[4] != 'no':
		bags.append(words[0] + words[1])
		for i in range(4, len(words), 4):
			rules[words[0] + words[1]].append((int(words[i]), words[i +1] + words[i + 2]))

goal = 'shinygold'

def contains(bag):
	for allowed in rules[bag]:
		if allowed[1] == goal:
			return 1
		if contains(allowed[1]):
			return 1
	return 0

total = 0

for bag in bags:
	if contains(bag):
		total += 1

print(total)

