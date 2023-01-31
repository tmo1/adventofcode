# https://adventofcode.com/2017/day/24

components, max_strength = [], 0
for line in open(0):
    line = line.split('/')
    a, b = int(line[0]), int(line[1])
    components.append((a, b, a + b))


def add_component(pin, strength, remaining_components):
    global max_strength
    flag = False
    for i, component in enumerate(remaining_components):
        next_pin = None
        if component[0] == pin:
            next_pin = component[1]
        elif component[1] == pin:
            next_pin = component[0]
        if next_pin:
            flag = True
            add_component(next_pin, strength + component[2], remaining_components[:i] + remaining_components[i + 1:])
    if not flag:
        max_strength = max(max_strength, strength)


add_component(0, 0, components)
print(max_strength)
