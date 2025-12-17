# https://adventofcode.com/2025/day/10#part2

from z3 import *

buttons = [Int('x%s' % i) for i in range(16)]
total = 0
for m, machine in enumerate(open(0)):
    machine = machine.split(' ')
    joltage_reqs = [int(n) for n in machine[-1][1:-2].split(',')]
    wiring_schematics = sorted([[int(button) for button in wiring_schematic[1:-1].split(',')] for wiring_schematic in machine[1:-1]], key=lambda x: len(x))
    s = Solver()
    s.add([joltage_req == sum([buttons[y] for y in range(len(wiring_schematics)) if z in wiring_schematics[y]]) for z, joltage_req in enumerate(joltage_reqs)] + [button >= 0 for button in buttons[:len(wiring_schematics)]])
    for i in range(max(joltage_reqs), 1000):
        s.push()
        s.add(sum(buttons[:len(wiring_schematics)]) == i)
        if s.check() == sat:
            total += i
            break
        s.pop()
print(total)