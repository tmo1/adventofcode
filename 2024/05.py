# https://adventofcode.com/2024/day/5

total, rules = 0, []
for line in open(0):
    line = line.strip()
    if '|' in line:
        rules.append(line.split('|'))
    elif line != '':
        line = line.split(',')
        for rule in rules:
            if rule[0] in line and rule[1] in line and line.index(rule[0]) > line.index(rule[1]):
                break
        else:
            total += int(line[len(line) // 2])
print(total)
