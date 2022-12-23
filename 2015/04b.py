# https://adventofcode.com/2015/day/4#part2

import sys
import hashlib
secret = sys.stdin.readline().strip()
x = 1
while True:
    if hashlib.md5((secret + str(x)).encode('utf8')).hexdigest()[:6] == '000000':
        print(x)
        break
    x += 1
