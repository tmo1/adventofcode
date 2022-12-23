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
	for n in values:
		valid = 0
		for rule in rules:
			if (n >= rules[rule][0] and n <= rules[rule][1]) or (n >= rules[rule][2] and n <= rules[rule][3]):
				valid = 1
				break
		if not valid:
			break
	if valid:
		valid_tickets.append(values)

length = len(rules)
rule_sets = [set() for i in range(length)]
for i in range(length):
	for rule in rules:
		for ticket in valid_tickets:
			valid = 1
			if (ticket[i] < rules[rule][0] or ticket[i] > rules[rule][1]) and (ticket[i] < rules[rule][2] or ticket[i] > rules[rule][3]):
				valid = 0
				break
		if valid:
			rule_sets[i].add(rule)

def solve(order, i):
	if i == length:
		print('solved!\n', order)
		n = 1
		for i in range(length):
			if order[i][:9] == 'departure':
				n *= my_ticket[i]
		print(n)
		raise SystemExit
	for rule in rule_sets[i]:
		if not rule in order:
			valid = 1
			for ticket in valid_tickets:
				n = ticket[i]
				if (n < rules[rule][0] or n > rules[rule][1]) and (n < rules[rule][2] or n > rules[rule][3]):
					valid = 0
					break
			if valid:
				order.append(rule)
				solve(order, i +1)
				order.pop()

solve([], 0)
