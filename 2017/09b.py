# https://adventofcode.com/2017/day/9#part2
# I don't get this one: my solution for part 2 was much simpler and required much less debugging than my solution for
# part 1. Perhaps I missed something that would have made the solution to part 1 much simpler.

import sys

stream, total, i = sys.stdin.readline().strip(), 0, 0
while i < len(stream):
    if stream[i] == '<':
        j = i + 1
        while stream[j] != '>':
            if stream[j] == '!':
                j += 2
            else:
                j += 1
                total += 1
        i = j + 1
    else:
        i += 1
print(total)
