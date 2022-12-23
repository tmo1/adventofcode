#! /usr/bin/python3

https://adventofcode.com/2020/day/4
# We had to add a newline to the end of the input for this to work

f = open('aoc4-input', 'r')
passport = {}
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
total = 0
while line := f.readline():
	if line == '\n':
		invalid = 0
		for r in required:
			if not r in passport:
				invalid = 1
				#print(passport)
				break
		if not invalid:
			total += 1
		passport = {}
	else:
		fields = line.split()
		for field in fields:
			k, v = field.split(':')
			passport[k] = v
print(total)
