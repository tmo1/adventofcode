# https://adventofcode.com/2023/day/19

category_map = {'x': 0, 'm': 1, 'a': 2, 's': 3}
mode = 'workflows'
workflows, parts = {}, []
total = 0
for line in open(0):
    if line == '\n':
        mode = 'parts'
        continue
    if mode == 'workflows':
        line = line.split('{')
        rules = line[1][:-1].split(',')
        workflows[line[0]] = []
        for rule in rules[:-1]:
            condition, action = rule.split(':')
            workflows[line[0]].append({'category': category_map[condition[0]], 'operator': condition[1], 'value': int(condition[2:]), 'action': action})
        workflows[line[0]].append(rules[-1][:-1])
    else:
        part = [int(x[2:]) for x in line[1:-2].split(',')]
        workflow = workflows['in']
        while workflow is not None:
            for rule in workflow:
                if isinstance(rule, dict):
                    match rule['operator']:
                        case '<':
                            action = rule['action'] if part[rule['category']] < rule['value'] else None
                        case '>':
                            action = rule['action'] if part[rule['category']] > rule['value'] else None
                        case '=':
                            action = rule['action'] if part[rule['category']] == rule['value'] else None
                else:
                    action = rule
                if action is not None:
                    workflow = None
                    match action:
                        case 'A':
                            total += sum(part)
                        case 'R':
                            pass
                        case _:
                            workflow = workflows[action]

                    break
print(total)
