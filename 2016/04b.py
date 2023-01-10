# https://adventofcode.com/2016/day/4#part2

import sys

for line in sys.stdin:
    sector_id = int(line.split('-')[-1][:-8])
    if ''.join([chr(((ord(c) - 97 + sector_id) % 26) + 97) if c != '-' else ' ' for c in line][:24]) == 'northpole object storage':
        print(sector_id)
        quit()
