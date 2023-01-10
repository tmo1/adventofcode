# https://adventofcode.com/2016/day/15
# both parts - see comment below

import sys

discs, t = [], 0
for line in sys.stdin:
    line = line[:-2].split()
    discs.append((int(line[3]), int(line[11])))
# comment out the following line for part 1, leave uncommented for part 2
discs.append((11, 0))
while True:
    for count, disc in enumerate(discs):
        if (disc[1] + count + 1 + t) % disc[0] != 0:
            break
    else:
        print(t)
        quit()
    t += 1
