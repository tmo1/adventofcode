#! /usr/bin/python3

https://adventofcode.com/2020/day/4
# We had to add a newline to the end of the input for this to work

f = open('aoc4-input', 'r')
passport = {}
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
total = 0
while line := f.readline():
	if line == '\n':
		invalid = 0
		for r in required:
			if not r in passport:
				invalid = 1
				break
		if invalid:
			passport = {}
			continue
		for digit in passport['hcl'][1:]:
			if not ((digit >= '0' and digit <= '9') or (digit >= 'a' and digit <= 'f')):
				invalid = 1
				print("Bad hcl: ", passport['hcl'])
				break
		for digit in passport['pid']:
			if not digit.isdigit:
				invalid = 1
				print("Bad pid: ", passport['pid'])
				break
		if (invalid or (int(passport['byr']) < 1920) or (int(passport['byr']) > 2002) or (int(passport['iyr']) < 2010) or (int(passport['iyr']) > 2020) or (int(passport['eyr']) < 2020) or (int(passport['eyr']) > 2030) or (not passport['ecl'] in ecls) or (len(passport['hgt']) < 3) or (passport['hcl'][0] != '#') or (len(passport['pid']) != 9)):
			print("Bad passport: ", passport)
			passport = {}
			continue
		height, h_unit = int(passport['hgt'][:-2]), passport['hgt'][-2:]
		if not ((h_unit == 'in' and height >= 59 and height <= 76) or (h_unit == 'cm' and height >= 150 and height <= 193)):
			print(height, h_unit, "Bad height: ", passport['hgt'])
			passport = {}
			continue
		total += 1
		passport = {}
	else:
		fields = line.split()
		for field in fields:
			k, v = field.split(':')
			passport[k] = v
print(total)
