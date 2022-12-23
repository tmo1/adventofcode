# https://adventofcode.com/2022/day/16

import sys
import re

valves = {}
for line in sys.stdin:
    line = re.split('[ =]', line)
    valves[line[1]] = {'flow': int(line[5][:-1]), 'valves': [x[:2] for x in line[10:]]}
location = 'AA'
openable_valves = set(x for x in valves.keys() if valves[x]['flow'] > 0)
openable_valves.add('AA')
for v in openable_valves:
    valve = valves[v]
    valve['distances'] = {x: {'visited': False, 'distance': 30} for x in valves.keys()}
    valve['distances'][v]['distance'] = 0
    while True:
        min_distance = 30
        x = None
        for y in valve['distances'].keys():
            if valve['distances'][y]['visited'] is False and valve['distances'][y]['distance'] <= min_distance:
                x = y
                min_distance = valve['distances'][y]['distance']
        if x is None:
            break
        for y in valves[x]['valves']:
            if valve['distances'][y]['distance'] > valve['distances'][x]['distance'] + 1:
                valve['distances'][y]['distance'] = valve['distances'][x]['distance'] + 1
        valve['distances'][x]['visited'] = True
openable_valves.remove('AA')
max_flow = 0


def next_valve(cur_valve, minute, flow):
     global max_flow
     for x in openable_valves:
        if cur_valve['distances'][x]['distance'] + minute < 29:
            openable_valves.remove(x)
            new_flow = flow + (30 - minute - cur_valve['distances'][x]['distance'] - 1) * valves[x]['flow']
            max_flow = max(max_flow, new_flow)
            next_valve(valves[x], minute + cur_valve['distances'][x]['distance'] + 1, new_flow)
            openable_valves.add(x)


next_valve(valves['AA'], 0, 0)
print(max_flow)
