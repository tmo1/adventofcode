#! /usr/bin/python3

# https://adventofcode.com/2021/day/23

import sys

instructions = {'inp': 0, 'add': 1, 'mul': 2, 'div': 3, 'mod': 4, 'eql': 5}
program = []

for line in sys.stdin:
	instruction = line.split()
	instruction[0] = instructions[instruction[0]]
	if len(instruction) == 3 and not instruction[2].isalpha():
		instruction[2] = int(instruction[2])
	program.append(instruction)

def run(inp, results, program):
	v = {'w': results[0], 'x': results[1], 'y': results[2], 'z': results[3]}
	for line in program:
		if line[0] == 0:
			v[line[1]] = inp
		elif line[0] == 1:
			v[line[1]] += line[2] if type(line[2]) is int else v[line[2]]
		elif line[0] == 2:
			v[line[1]] *= line[2] if type(line[2]) is int else v[line[2]]
		elif line[0] == 3:
			v[line[1]] //= line[2] if type(line[2]) is int else v[line[2]]
		elif line[0] == 4:
			v[line[1]] %= line[2] if type(line[2]) is int else v[line[2]]
		else:
			v[line[1]] = 1 if v[line[1]] == (line[2] if type(line[2]) is int else v[line[2]]) else 0
	return (v['w'], v['x'], v['y'], v['z'])

sections = []
for line in program:
	if line[0] == 0:
		sections.append([])
		section = sections[-1]
	section.append(line)

results = {(0, 0, 0, 0): []}

for i in range(14):
	new_results = {}
	for j in range(1, 10):
		for result in results:
			new_result = run(j, result, sections[i])
			if new_result in new_results:
				if results[result] + [j] > new_results[new_result]:
					new_results[new_result] = results[result] + [j]
			else:
				new_results[new_result] = results[result] + [j]
	results = new_results

monad = []
for result in results:
	if result[3] == 0 and results[result] > monad:
		monad = results[result]
print((str(monad)))
