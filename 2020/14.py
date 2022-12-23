#! /usr/bin/python3

# https://adventofcode.com/2020/day/14

f = open('aoc-input', 'r')
#f = open('sample', 'r')
one_mask, zero_mask = 0, 0
memory = {}
while line := f.readline():
	if line[:3] == 'mem':
		i = 4
		while line[i] != ']':
			i += 1
		address = int(line[4:i])
		value = int(line[i + 4:])
		value |= one_mask
		value &= zero_mask
		memory[address] = value
	else:
		mask = line[7:].rstrip()
		one_mask_list, zero_mask_list = [], []
		for bit in mask:
			if bit == 'X':
				one_mask_list.append('0')
				zero_mask_list.append('1')
			else:
				zero_mask_list.append(bit)
				one_mask_list.append(bit)
		one_mask = int(''.join(one_mask_list), 2)
		zero_mask = int(''.join(zero_mask_list), 2)
total = 0
for address in memory:
	total += memory[address]
print(total)
		
		
		
		
		
		
	
