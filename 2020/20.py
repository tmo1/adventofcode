#! /usr/bin/python3

# https://adventofcode.com/2020/day/20

f = open('aoc-input', 'r')
#f = open('sample', 'r')

def reverse(num):
    result = 0
    for i in range(10):
        result = (result << 1) + (num & 1)
        num >>= 1
    return result
    
tiles = []
TLEN = 10
#TNUM = 3
TNUM = 12

while line := f.readline():
	if line[0] == 'T':
		num = int(line[5:len(line) - 2])
		tile = []
		while (line := f.readline().rstrip()) != '':
			line = line.translate(line.maketrans('.#', '01'))
			tile.append(line)
		up = int(tile[0], base=2)
		down = int(tile[TLEN - 1], base=2)
		right = int(''.join([tile[i][TLEN - 1] for i in range(TLEN)]), base=2)
		left = int(''.join([tile[i][0] for i in range(TLEN)]), base=2)
		up_rev = reverse(up)
		down_rev = reverse(down)
		right_rev = reverse(right)
		left_rev = reverse(left)
		tiles.append([(up, right, down, left), (left_rev, up, right_rev, down), (down_rev, left_rev, up_rev, right_rev), (right, down_rev, left, up_rev), (up_rev, left, down_rev, right), (right_rev, up_rev, left_rev, down_rev), (down, right_rev, up, left_rev), (left, down, right, up), set((up, down, right, left, up_rev, down_rev, right_rev, left_rev)), num, set()])

for i in range(len(tiles)):
	for j in range(i + 1, len(tiles)):
		if tiles[i][8] & tiles[j][8]:
			tiles[i][10].add(j)
			tiles[j][10].add(i)

def puzzle(square, avail, x, y):
	possibs = avail.copy()
	if x > 0:
		possibs &= tiles[square[x-1][y]['tile']][10]
	if y > 0:
		possibs &= tiles[square[x][y-1]['tile']][10]
	for i in possibs:
		new_avail = avail.copy()
		new_avail.remove(i)
		square[x][y]['tile'] = i
		for j in range(8):
			if x > 0:
				if tiles[i][j][3] != tiles[square[x-1][y]['tile']][square[x-1][y]['orient']][1]:
					continue
			if y > 0:
				if tiles[i][j][0] != tiles[square[x][y-1]['tile']][square[x][y-1]['orient']][2]:
					continue
			square[x][y]['orient'] = j
			if x == TNUM - 1 and y == TNUM - 1:
				print(tiles[square[0][0]['tile']][9] * tiles[square[0][TNUM - 1]['tile']][9] * tiles[square[TNUM - 1][0]['tile']][9] * tiles[square[TNUM - 1][TNUM - 1]['tile']][9])
				raise SystemExit
			else:
				puzzle(square.copy(), new_avail, 0 if x == TNUM - 1 else x + 1, y + 1 if x == TNUM - 1 else y)
		square[x][y] = {}

square = [[{} for i in range(TNUM)] for i in range(TNUM)]				
avail = set(i for i in range(len(tiles)))
puzzle(square, avail, 0, 0)
