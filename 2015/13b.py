# https://adventofcode.com/2015/day/13#part2

import sys

rules = {}
people = set()
for line in sys.stdin:
    words = line.split()
    words[-1] = words[-1].strip('.')
    rules[(words[0], words[-1])] = int(words[3]) if words[2] == 'gain' else -int(words[3])
    people.add(words[0])
    people.add(words[-1])
happiest = 0


def arrange(last, happy, remaining):
    global happiest
    if remaining:
        for person in remaining:
            new_happy = happy + rules[(last, person)] + rules[(person, last)] if last else happy
            arrange(person, new_happy, remaining - {person})
    elif happy > happiest:
        happiest = happy


arrange(None, 0, people)
print(happiest)
