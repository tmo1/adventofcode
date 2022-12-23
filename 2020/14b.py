#! /usr/bin/python3

# https://adventofcode.com/2020/day/14

f = open('aoc-input', 'r')
#f = open('sample', 'r')
mask = []
memory = {}
def compute_address(address, i, value):
	if i == 36:
		memory[address] = value
		return
	if mask[i] == 'X':
		address |= 1 << (35 - i)
		compute_address(address, i + 1, value)
		address &= ~(1 << (35 - i))
	elif mask[i] == '1':
		address |= 1 << (35 - i)
	compute_address(address, i + 1, value)	
while line := f.readline():
	if line[:3] == 'mem':
		i = 4
		while line[i] != ']':
			i += 1
		address = int(line[4:i])
		value = int(line[i + 4:])
		compute_address(address, 0, value)
	else:
		mask = line[7:].rstrip()
total = 0
for address in memory:
	total += memory[address]
print(total)
		
		
		
		
		
		
	
