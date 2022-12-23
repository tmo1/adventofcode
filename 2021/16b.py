#! /usr/bin/python3

# https://adventofcode.com/2021/day/16#part2

import sys

msg = sys.stdin.readline().strip()
bits = []
for digit in msg:
	bits += f'{int(digit, 16):04b}'
bits.reverse()

def parse(data):
	version = int(''.join(data.pop() for i in range(3)), 2)
	tid = int(''.join(data.pop() for i in range(3)), 2)
	if tid == 4:
		literal = ''
		while True:
			flag = data.pop()
			for i in range(4):
				literal += data.pop()
			if flag == '0':
				break
		return int(literal, 2)
	else:
		subs = []
		if data.pop() == '0':
			length2 = int(''.join(data.pop() for i in range(15)), 2)
			curlength = len(data)
			while curlength - len(data) < length2:
				subs.append(parse(data))
		else:
			num2 = int(''.join(data.pop() for i in range(11)), 2)
			for i in range(num2):
				subs.append(parse(data))
		if tid == 0:
			return sum(subs)
		if tid == 1:
			prod = 1
			for s in subs:
				prod *= s
			return prod
		if tid == 2:
			return min(subs)
		if tid == 3:
			return max(subs)
		if tid == 5:
			return 1 if subs[0] > subs[1] else 0
		if tid == 6:
			return 1 if subs[0] < subs[1] else 0
		if tid == 7:
			return 1 if subs[0] == subs[1] else 0

print(parse(bits))

