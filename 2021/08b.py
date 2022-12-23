#! /usr/bin/python3

# https://adventofcode.com/2021/day/8#part2

import sys

total = 0
uniq_to_digits = {2: 1, 4: 4, 3: 7, 7: 8}

for line in sys.stdin:
	(patterns, values) = line.split('|')
	patterns = patterns.split()
	pattern_sets = []
	digit_sets = [0] * 10
	for pattern in patterns:
		pattern_sets.append(set(pattern))
	for pattern in pattern_sets:
		if len(pattern) in uniq_to_digits:
			digit_sets[uniq_to_digits[len(pattern)]] = pattern
	for pattern in pattern_sets:
		if len(pattern) == 5 and pattern > digit_sets[1]:
			digit_sets[3] = pattern
		if len(pattern) == 6:
			if pattern > digit_sets[4]:
				digit_sets[9] = pattern
			elif not pattern > digit_sets[1]:
					digit_sets[6] = pattern
			else:
				digit_sets[0] = pattern
	for pattern in pattern_sets:
		if len(pattern) == 5:
			if pattern < digit_sets[6]:
				digit_sets[5] = pattern
			elif digit_sets[3] != pattern:
					digit_sets[2] = pattern
			
	values = values.split()
	num = ''
	for value in values:
		segments = set(value)
		for i in range(len(digit_sets)):
			if segments == digit_sets[i]:
				num = num + str(i)
	total += int(num)

print(total)
