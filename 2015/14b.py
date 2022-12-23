# https://adventofcode.com/2015/day/14#part2

import sys

reindeer = []
for line in sys.stdin:
    words = line.split()
    reindeer.append({'name': words[0], 'speed': int(words[3]), 'fly': int(words[6]), 'rest': int(words[13]), 'cycle': 0,
                     'distance': 0, 'score': 0})
for i in range(2503):
    for r in reindeer:
        if r['cycle'] < r['fly']:
            r['distance'] += r['speed']
        r['cycle'] = (r['cycle'] + 1) % (r['fly'] + r['rest'])
    lead = max([r['distance'] for r in reindeer])
    for r in reindeer:
        if r['distance'] == lead:
            r['score'] += 1
print(max([r['score'] for r in reindeer]))
