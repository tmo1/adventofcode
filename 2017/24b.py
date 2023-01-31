# https://adventofcode.com/2017/day/24#part2

components, max_strength, max_length = [], 0, 0
for line in open(0):
    line = line.split('/')
    a, b = int(line[0]), int(line[1])
    components.append((a, b, a + b))


def add_component(pin, strength, length, remaining_components):
    global max_strength, max_length
    flag = False
    for i, component in enumerate(remaining_components):
        next_pin = None
        if component[0] == pin:
            next_pin = component[1]
        elif component[1] == pin:
            next_pin = component[0]
        if next_pin:
            flag = True
            add_component(next_pin, strength + component[2], length + 1, remaining_components[:i] + remaining_components[i + 1:])
    if not flag:
        if length > max_length:
            max_length = length
            max_strength = strength
        elif length == max_length and strength > max_strength:
            max_strength = strength


add_component(0, 0, 0, components)
print(max_strength)
