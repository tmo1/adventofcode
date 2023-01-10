# https://adventofcode.com/2016/day/16
# both parts - see comment below

import sys

# set 'disk_length' to 272 for part 1, leave as is for part 2
disk_length = 35651584
data = list(sys.stdin.readline().strip())
while len(data) < disk_length:
    data += ['0'] + list(reversed(['0' if c == '1' else '1' for c in data]))
data = data[:disk_length]
while len(data) % 2 == 0:
    data = ['1' if data[i] == data[i + 1] else '0' for i in range(0, len(data), 2)]
print(''.join(data))
