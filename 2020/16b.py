#! /usr/bin/python3

# https://adventofcode.com/2020/day/16

import re

f = open('aoc-input', 'r')
#f = open('sample', 'r')
rules = {}
p = re.compile('(.*): (\d*)-(\d*) or (\d*)-(\d*)')
while (rule := f.readline()) != '\n':
	m = p.match(rule)
	rules[m.group(1)] = (int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
#print(rules)
f.readline()
my_ticket = list(map(lambda x: int(x), f.readline().split(',')))
f.readline()
f.readline()
tickets = []
while (line := f.readline()):
	tickets.append(line.rstrip())
valid_tickets = []
for ticket in tickets:
	values = list(map(lambda x: int(x), ticket.split(',')))
	#print(values)
	for n in values:
		valid = 0
		for rule in rules:
			#print(rule)
			if (n >= rules[rule][0] and n <= rules[rule][1]) or (n >= rules[rule][2] and n <= rules[rule][3]):
				valid = 1
				break
		if not valid:
			#print('invalid ticket: ', ticket)
			break
	if valid:
		valid_tickets.append(values)

length = len(rules)
def solve(order, i):
	#print(order, i)
	if i == length:
		print('solved!\n', order)
		n = 1
		for i in range(length):
			#print(order[i])
			if order[i][:9] == 'departure':
				n *= my_ticket[i]
		print(n)
		raise SystemExit
	for rule in rules:
		if not rule in order:
			#print('\ntrying ', rule, 'in position ', i)
			valid = 1
			for ticket in valid_tickets:
				#print('considering ticket: ', ticket)
				n = ticket[i]
				#print('considering value', i, 'of ticket', ticket)
				#print('considering value: ', n)
				if (n < rules[rule][0] or n > rules[rule][1]) and (n < rules[rule][2] or n > rules[rule][3]):
					valid = 0
					#print('failed on ticket: ', ticket)
					break
			if valid:
				order.append(rule)
				solve(order, i +1)
				order.pop()

solve([], 0)
#print(valid_tickets)
#print(total)
		
