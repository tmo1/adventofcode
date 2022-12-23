#! /usr/bin/python3

# https://adventofcode.com/2021/day/14

import sys

polymer = list(sys.stdin.readline().strip())
sys.stdin.readline()
rules = {}
for line in sys.stdin:
	rules[line[0:2]] = line[-2]

for i in range(10):
	polymer2 = []
	for j in range(len(polymer) - 1):
		polymer2.append(polymer[j])
		polymer2.append(rules[polymer[j] + polymer[j + 1]])
	polymer2.append(polymer[-1])
	polymer = polymer2

letters = {}
for letter in polymer:
	if letter in letters:
		letters[letter] += 1
	else:
		letters[letter] = 1
print(max(letters.values()) - min(letters.values()))
