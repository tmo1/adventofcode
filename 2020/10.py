#! /usr/bin/python3

# https://adventofcode.com/2020/day/10
import sys
adapters = []
f = open('aoc10-input', 'r')
while number := f.readline():
	adapters.append(int(number))
adapters.sort()
previous, one, three = 0, 0, 0
for adapter in adapters:
	if adapter - previous == 1:
		one += 1
	else:
		three += 1
	previous = adapter
print(one * (three + 1))
