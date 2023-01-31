# https://adventofcode.com/2017/day/7#part2

import sys
from collections import defaultdict

programs, weights = {}, {}
for line in sys.stdin:
    line = line.split()
    programs[line[0]] = {'weight': int(line[1][1:-1])}
    if len(line) > 2:
        programs[line[0]]['children'] = {x.strip(',') for x in line[3:]}


def get_weight(p):
    if p not in weights:
        program = programs[p]
        weight = program['weight']
        if 'children' in program:
            weight += sum(get_weight(c) for c in program['children'])
        weights[p] = weight
    return weights[p]


for prog_name, prog_details in programs.items():
    if 'children' in prog_details:
        children = defaultdict(lambda: 0)
        for child in prog_details['children']:
            children[get_weight(child)] += 1
        if len(children) == 2:
            wrong_weight, right_weight = min(children, key=children.get), max(children, key=children.get)
            for child in prog_details['children']:
                if get_weight(child) == wrong_weight:
                    print(programs[child]['weight'] + right_weight - wrong_weight)
                    quit()
