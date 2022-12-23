#! /usr/bin/python3

# https://adventofcode.com/2020/day/9
import sys
numbers = []
f = open('aoc9-input', 'r')
while number := f.readline():
	numbers.append(int(number))
for i in range(25, len(numbers)):
	valid = 0
	for j in range(i-25, i):
		for k in range(j + 1, i):
			if numbers[j] + numbers[k] == numbers[i]:
				valid = 1
				break
		if valid:
			break
	if not valid:
		print(numbers[i])
		sys.exit()
