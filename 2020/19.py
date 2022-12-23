#! /usr/bin/python3

# https://adventofcode.com/2020/day/19

# this solves both part 1 and part 2 (somewhat efficiently), despite
# the warnings, and ignoring the hints, given in the part 2 section

f = open('aoc-input', 'r')
#f = open('sample', 'r')

lines = []
while (line := f.readline()) != '\n':
	rule = line.split()
	rule[0] = int(rule[0][:len(rule[0]) - 1])
	lines.append(rule)
rules = [[] for i in range(max(lines[i][0] for i in range(len(lines))) + 1)]
for line in lines:
	rule, subrule = [], []
	for word in line[1:]:
		if word == '|':
			rules[line[0]].append(subrule)
			subrule = []
		else:
			subrule.append(int(word) if word.isdigit() else word[1])
	rules[line[0]].append(subrule)

for i in range(len(rules)):
	if len(rules[i]) == 1 and len(rules[i][0]) == 1:
		for j in range(len(rules)):
			for k in range(len(rules[j])):
				for l in range(len(rules[j][k])):
					if rules[j][k][l] == i:
						rules[j][k][l] = rules[i][0][0]

validated = {}

def slice_seq(seq, n, sequences, stack):
	if n == 1:
		stack.append(seq)
		sequences.append(stack.copy())
		stack.pop()
		return sequences
	for i in range(1, (len(seq) - n) + 2):
		stack.append(seq[:i])
		sequences = slice_seq(seq[i:], n - 1, sequences, stack)
		stack.pop()
	return sequences
	
def validate(message, n):
	if message in validated and n in validated[message]:
		return validated[message][n]
	valid = 0
	for subrule in rules[n]:
		sequences = slice_seq(message, len(subrule), [], [])
		for sequence in sequences:
			for i in range(len(subrule)):
				if type(subrule[i]) == int:
					if not validate(sequence[i], subrule[i]):
						break
				elif sequence[i] != subrule[i]:
					break
			else:
				if not message in validated:
					validated[message] = {}
				validated[message][n] = 1
				return 1
	if not message in validated:
		validated[message] = {}
	validated[message][n] = 0
	return 0

total = 0
while line := f.readline().rstrip():
	total += validate(line, 0)
print(total)
