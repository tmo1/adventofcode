#! /usr/bin/python3

# https://adventofcode.com/2021/day/24#part2

# this is basically the same code as the code for part 1, with a couple
# of '>'s flipped to '<'s. Additionally, we take advantage of the fact
# that w, x, and y do not carry over between input segments (w is
# overwritted by input, and x and y are set to 0) to make the code
# simpler and faster (16 minutes vs. 28 minutes), although it's still
# too slow

import sys

instructions = {'inp': 0, 'add': 1, 'mul': 2, 'div': 3, 'mod': 4, 'eql': 5}
program = []

for line in sys.stdin:
	instruction = line.split()
	instruction[0] = instructions[instruction[0]]
	if len(instruction) == 3 and not instruction[2].isalpha():
		instruction[2] = int(instruction[2])
	program.append(instruction)

def run(inp, z, program):
	v = {'w': 0, 'x': 0, 'y': 0, 'z': z}
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
	return (v['z'])

sections = []
for line in program:
	if line[0] == 0:
		sections.append([])
		section = sections[-1]
	section.append(line)

results = {0: []}

for i in range(14):
	print('i: ', i, 'results: ', len(results))
	new_results = {}
	for j in range(1, 10):
		for result in results:
			new_result = run(j, result, sections[i])
			if new_result in new_results:
				if results[result] + [j] < new_results[new_result]:
					new_results[new_result] = results[result] + [j]
			else:
				new_results[new_result] = results[result] + [j]
	results = new_results

monad = [9 for i in range(14)]
for result in results:
	if result == 0 and results[result] < monad:
		monad = results[result]
print(''.join(map(str(monad)))
