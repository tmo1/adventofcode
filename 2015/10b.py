# https://adventofcode.com/2015/day/10#part2

import sys
seq = sys.stdin.readline().strip()
for i in range(50):
    run = 0
    new_seq = ''
    j = 0
    while True:
        run += 1
        if j + 1 == len(seq):
            seq = new_seq + str(run) + seq[j]
            break
        if not seq[j + 1] == seq[j]:
            new_seq += str(run) + seq[j]
            run = 0
        j += 1
print(len(seq))
