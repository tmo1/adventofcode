# https://adventofcode.com/2016/day/5

import sys
import hashlib

door_id, n, code = sys.stdin.readline().strip(), -1, []
for i in range(8):
    while True:
        n += 1
        h = hashlib.md5((door_id + str(n)).encode()).hexdigest()
        for d in h[:5]:
            if d != '0':
                break
        else:
            code.append(h[5])
            break
print(''.join(code))
