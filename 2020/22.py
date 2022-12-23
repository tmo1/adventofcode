#! /usr/bin/python3

# https://adventofcode.com/2020/day/22

from collections import deque

f = open('aoc-input', 'r')
#f = open('sample', 'r')
f.readline()

me = deque([])
crab = deque([])

while (card := f.readline()) != '\n':
	me.append(int(card))
f.readline()
while card := f.readline():
	crab.append(int(card))

while me and crab:
	my_card = me.popleft()
	crab_card = crab.popleft()
	if my_card > crab_card:
		me.extend([my_card, crab_card])
	else:
		crab.extend([crab_card, my_card])

win_deck = me if me else crab
win_deck.reverse()
score = 0
for i in range(len(win_deck)):
	score += win_deck[i] * (i + 1)
print(score)
	
