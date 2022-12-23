#! /usr/bin/python3

# https://adventofcode.com/2020/day/10

# This is a correct solution to part 2, but it takes much too long to
# run. A more complex but efficient solution is '10c.py'

adapters = [0]
f = open('aoc10-input', 'r')
while number := f.readline():
	adapters.append(int(number))
adapters.sort()
adapters.append(adapters[len(adapters) - 1] + 3)
last_adapter = len(adapters) - 1
chain = [0]
valid = 0
def selection(i):
	global valid
	if adapters[i] - chain[len(chain) - 1] > 3:
		return 0
	if i == last_adapter:
		valid += 1
		return
	chain.append(adapters[i])
	if selection(i + 1) == 0:
		return
	chain.pop()
	if selection(i + 1) == 0:
		return
selection(1)
print(valid)
