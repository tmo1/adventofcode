#! /usr/bin/python3

# https://adventofcode.com/2020/day/5

f = open('aoc5-input', 'r')
seats = []
while board := f.readline():
	board = board.replace('F', '0')
	board = board.replace('B', '1')
	board = board.replace('L', '0')
	board = board.replace('R', '1')
	seats.append(int(board[:7], base=2) * 8 + int(board[7:], base=2))
seats.sort()
previous = -10
for seat in seats:
	if seat - previous == 2:
		print(seat - 1)
		break
	previous = seat
