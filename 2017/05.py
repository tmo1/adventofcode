# https://adventofcode.com/2017/day/5
# both parts - see comments below

import sys

jumps, i, steps = [int(x) for x in sys.stdin], 0, 0
length = len(jumps)
while 0 <= i < length:
    new_i = i + jumps[i]
    # uncomment the following line for part 1, or the subsequent one for part 2
    # jumps[i] += 1  # part 1
    jumps[i] += -1 if jumps[i] >= 3 else 1  # part 2
    i = new_i
    steps += 1
print(steps)
