#! /usr/bin/python3

# https://adventofcode.com/2020/day/8

f = open('aoc8-input', 'r')
program = f.readlines()
i, acc = 0, 0
while program[i] != '*':
	words = program[i].split()
	program[i] = '*'
	if words[0] == 'nop':
		i += 1
	elif words[0] == 'acc':
		acc += int(words[1])
		i += 1
	elif words[0] == 'jmp':
		i += int(words[1])
print(acc)

