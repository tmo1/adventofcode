#! /usr/bin/python3

# https://adventofcode.com/2020/day/22

from collections import deque

f = open('aoc-input', 'r')
#f = open('sample', 'r')
f.readline()

me = deque([])
crab = deque([])
ME = 1
CRAB = 2

while (card := f.readline()) != '\n':
	me.append(int(card))
f.readline()
while card := f.readline():
	crab.append(int(card))

known_games = {}
def game(me, crab, seen_games):
	game_bytes = bytes(list(me) + [0] + list(crab))
	if game_bytes in known_games:
		return known_games[game_bytes]
	while me and crab:
		cards = bytes(list(me) + [0] + list(crab))
		if cards in seen_games:
			known_games[game_bytes] = ME
			return ME
		seen_games.add(cards)
		my_card = me.popleft()
		crab_card = crab.popleft()
		if len(me) >= my_card and len(crab) >= crab_card:
			new_me = deque([me[i] for i in range(my_card)])
			new_crab = deque([crab[i] for i in range(crab_card)])
			winner = game(new_me, new_crab, set())
		else:
			winner = ME if my_card > crab_card else CRAB
		if winner == ME:
			me.extend([my_card, crab_card])
		else:
			crab.extend([crab_card, my_card])
	known_games[game] = ME if me else CRAB
	return ME if me else CRAB

win_deck = me if game(me, crab, set()) == ME else crab
win_deck.reverse()
score = 0
for i in range(len(win_deck)):
	score += win_deck[i] * (i + 1)
print(score)
