# https://adventofcode.com/2022/day/11#part2

import sys

monkeys = []
while True:
    line = sys.stdin.readline()
    if not line:
        break
    monkeys.append([[int(x.strip(',')) for x in sys.stdin.readline().split()[2:]], sys.stdin.readline().split()[4:],
                    int(sys.stdin.readline().split()[-1]), int(sys.stdin.readline().split()[-1]),
                    int(sys.stdin.readline().split()[-1]), 0])
    sys.stdin.readline()
n = 1
for monkey in monkeys:
    n *= monkey[2]
for i in range(10000):
    for monkey in monkeys:
        for item in monkey[0]:
            second_op = item if monkey[1][1] == 'old' else int(monkey[1][1])
            if monkey[1][0] == '+':
                new_worry = item + second_op
            else:
                new_worry = item * second_op
            new_worry %= n
            monkeys[monkey[3] if new_worry % monkey[2] == 0 else monkey[4]][0].append(new_worry)
        monkey[-1] += len(monkey[0])
        monkey[0] = []
items_inspected = sorted([monkey[-1] for monkey in monkeys])
print(items_inspected[-1] * items_inspected[-2])
