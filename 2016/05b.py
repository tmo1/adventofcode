# https://adventofcode.com/2016/day/5#part2
# this took 33.181s on my W550s for my input

import sys
import hashlib

door_id, n, code, total = sys.stdin.readline().strip(), -1, ['*' for i in range(8)], 0
while True:
    n += 1
    h = hashlib.md5((door_id + str(n)).encode()).hexdigest()
    for d in h[:5]:
        if d != '0':
            break
    else:
        if h[5].isdigit():
            position = int(h[5])
            if 0 <= position <= 7 and code[position] == '*':
                code[position] = h[6]
                if total == 7:
                    print(''.join(code))
                    quit()
                total += 1
