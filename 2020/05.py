#! /usr/bin/python3

# https://adventofcode.com/2020/day/5

f = open('aoc5-input', 'r')
high = 0
while board := f.readline():
	board = board.replace('F', '0')
	board = board.replace('B', '1')
	board = board.replace('L', '0')
	board = board.replace('R', '1')
	if (seat_id := int(board[:7], base=2) * 8 + int(board[7:], base=2)) > high:
		high = seat_id
print(high)

