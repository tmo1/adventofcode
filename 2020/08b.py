#! /usr/bin/python3

# https://adventofcode.com/2020/day/8

import sys

f = open('aoc8-input', 'r')
program = f.readlines()
for i in range(len(program)):
	words = program[i].split()
	if words[0] == 'acc':
		continue
	program_copy = program.copy()
	program_copy[i] = ('nop' if words[0] == 'jmp' else 'jmp') + program[i][3:]
	program_copy.append('!')
	j, acc = 0, 0
	while program_copy[j] != '*':
		if program_copy[j] == '!':
			print(acc)
			sys.exit()
		words = program_copy[j].split()
		program_copy[j] = '*'
		if words[0] == 'nop':
			j += 1
		elif words[0] == 'acc':
			acc += int(words[1])
			j += 1
		elif words[0] == 'jmp':
			j += int(words[1])


