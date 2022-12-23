#! /usr/bin/python3

# https://adventofcode.com/2020/day/10
# Efficient solution to part 2

adapters = [0]
f = open('aoc10-input', 'r')
while number := f.readline():
	adapters.append(int(number))
adapters.sort()
adapters.append(adapters[len(adapters) - 1] + 3)

sequences = []
x = 0
for i in range(1, len(adapters)):
	if adapters[i] - adapters[i - 1] == 3:
		sequences.append(adapters[x:i])
		x = i

def selection(i, sequence):
	global valid
	if sequence[i] - chain[len(chain) - 1] > 3:
		return 0
	if i == len(sequence) - 1:
		valid += 1
		return
	chain.append(sequence[i])
	if selection(i + 1, sequence) == 0:
		return
	chain.pop()
	if selection(i + 1, sequence) == 0:
		return

total = 1
for sequence in sequences:
	chain = [sequence[0]]
	valid = 0
	if len(sequence) > 1:
		selection(1, sequence)
		total *= valid

print(total)
