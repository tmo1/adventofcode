# https://adventofcode.com/2015/day/5#part2

import sys
nice = 0
for line in sys.stdin:
    prevPairs = set()
    prevPair = '##'
    prevLetter = '#'
    prevPrevLetter = ''
    rule1 = rule2 = False
    for letter in line:
        if (prevLetter + letter) in prevPairs:
            rule1 = True
        if letter == prevPrevLetter:
            rule2 = True
        prevPairs.add(prevPair)
        prevPair = prevLetter + letter
        prevPrevLetter = prevLetter
        prevLetter = letter
    if rule1 and rule2:
        nice += 1
print(nice)
