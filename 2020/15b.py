#! /usr/bin/python3

# https://adventofcode.com/2020/day/15

#f = open('aoc-input', 'r')
#f = open('sample', 'r')
numbers, last = {16:1, 1:2, 0:3, 18:4, 12:5, 14:6}, 19
for i in range(len(numbers) + 2, 30000001):
	number = i - (1 + numbers[last]) if last in numbers else 0
	numbers[last] = i -1
	last = number
print(last)
		
		
		
		
		
		
	
