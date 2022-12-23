#! /usr/bin/python3

# https://adventofcode.com/2021/day/14#part2

import sys

polymer = list(sys.stdin.readline().strip())
sys.stdin.readline()
rules = {}
for line in sys.stdin:
	rules[line[0:2]] = (line[-2], line[0] + line[-2], line[-2] + line[1])
letters = {}
for letter in polymer:
	letters[letter] = letters[letter] + 1 if letter in letters else 1
pairs = {}
for i in range(len(polymer) - 1):
	pairs[polymer[i] + polymer[i + 1]] = pairs[polymer[i] + polymer[i + 1]] + 1 if polymer[i] + polymer[i + 1] in pairs else 1

for i in range(40):
	letters2 = {}
	for letter in letters:
		letters2[letter] = letters[letter]
	pairs2 = {}
	for pair in pairs:
		n = pairs[pair]
		letters2[rules[pair][0]] = letters2[rules[pair][0]] + n if rules[pair][0] in letters2 else n
		pairs2[rules[pair][1]] = pairs2[rules[pair][1]] + n if rules[pair][1] in pairs2 else n
		pairs2[rules[pair][2]] = pairs2[rules[pair][2]] + n if rules[pair][2] in pairs2 else n
	letters = letters2
	pairs = pairs2

print(max(letters.values()) - min(letters.values()))
