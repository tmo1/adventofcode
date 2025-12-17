# https://adventofcode.com/2025/day/10

def solve(remaining, index, pressed):
    if remaining == 0:
        return True if ['#' if sum([1 for button in pressed if i in button]) % 2 == 1 else '.' for i in range(len(lights))] == lights else False
    for i_ in range(index, len(wiring_schematics)):
        if solve(remaining - 1, i_ + 1, pressed + [wiring_schematics[i_]]):
            return True
    return False


total = 0
for machine in open(0):
    machine = machine.split(' ')
    lights = list(machine[0][1:-1])
    wiring_schematics = [[int(button) for button in wiring_schematic[1:-1].split(',')] for wiring_schematic in machine[1:-1]]
    for i in range(1, 32):
        if solve(i, 0, []):
            total += i
            break
print(total)
