# https://adventofcode.com/2023/day/19#part2

import copy
from functools import reduce

category_map, workflows = {'x': 0, 'm': 1, 'a': 2, 's': 3}, {}
for line in open(0):
    if line == '\n':
        break
    line = line.split('{')
    rules = line[1].split(',')
    workflows[line[0]] = []
    parts = [{'>=': 1, '<=': 4000, '!=': set()} for i in range(4)]
    for rule in rules:
        if rule.find(':') >= 0:
            condition, action = rule.split(':')
            category, num = category_map[condition[0]], int(condition[2:])
            parts_condition_met = copy.deepcopy(parts)
            match condition[1]:
                case '<':
                    parts_condition_met[category]['<='] = min(parts_condition_met[category]['<='], num - 1)
                    parts[category]['>='] = max(parts_condition_met[category]['>='], num)
                case '>':
                    parts_condition_met[category]['>='] = max(parts_condition_met[category]['>='], num + 1)
                    parts[category]['<='] = min(parts_condition_met[category]['<='], num)
                case '=':
                    parts_condition_met[category]['<='] = min(parts_condition_met[category]['<='], num)
                    parts_condition_met[category]['>='] = max(parts_condition_met[category]['>='], num)
                    parts[category]['!='].add(num)
            workflows[line[0]].append(parts_condition_met + [action])
        else:
            workflows[line[0]].append(parts + [rule[:-2]])
part_ranges, total = [[{'>=': 1, '<=': 4000, '!=': set()} for i in range(4)] + ['A']], 0
while part_ranges:
    part_range = part_ranges.pop()
    if part_range[4] == 'in':
        total += reduce(lambda a, b: a * b, [x['<='] - x['>='] + 1 - sum([1 for y in x['!='] if x['>='] <= y <= x['<=']]) for x in part_range[:4]])
        continue
    for workflow_name, workflow in workflows.items():
        for rule in workflow:
            if rule[4] == part_range[4]:
                new_part_range = [{'>=': max(part_range[i]['>='], rule[i]['>=']), '<=': min(part_range[i]['<='], rule[i]['<=']), '!=': part_range[i]['!='] | rule[i]['!=']} for i in range(4)]
                if not [i for i in range(4) if new_part_range[i]['>='] > new_part_range[i]['<=']]:
                    part_ranges.append(new_part_range + [workflow_name])
print(total)
