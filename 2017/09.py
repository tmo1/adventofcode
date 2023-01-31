# https://adventofcode.com/2017/day/9

import sys

stream, total, i = sys.stdin.readline().strip(), 0, 0
while i < len(stream):
    if stream[i] == '<':
        j = i + 1
        while stream[j] != '>':
            j += 2 if stream[j] == '!' else 1
        stream = stream[:i] + stream[j + 1:]
    else:
        i += 1
stream = [char for char in stream if char != ',']


def do_group(x, containing):
    global total
    total += containing
    sub_group_start, sub_group_end, balance = 1, 1, 0
    while sub_group_end < len(x) - 1:
        balance += 1 if x[sub_group_end] == '{' else -1
        if balance == 0:
            do_group(x[sub_group_start:sub_group_end + 1], containing + 1)
            sub_group_start = sub_group_end + 1
        sub_group_end += 1


do_group(stream, 1)
print(total)
