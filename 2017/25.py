# https://adventofcode.com/2017/day/25

blueprint, tape, states, i = open(0), set(), {}, 0
current_state = blueprint.readline().split()[3][0]
steps = int(blueprint.readline().split()[5])
while True:
    if blueprint.readline() == '':
        break
    state = blueprint.readline().split()[2][0]
    blueprint.readline()
    write_val = blueprint.readline().split()[4][0]
    move_val = 1 if blueprint.readline().split()[6][0] == 'r' else -1
    next_state = blueprint.readline().split()[4][0]
    states[state] = [{'write': write_val, 'move': move_val, 'next': next_state}]
    blueprint.readline()
    write_val = blueprint.readline().split()[4][0]
    move_val = 1 if blueprint.readline().split()[6][0] == 'r' else -1
    next_state = blueprint.readline().split()[4][0]
    states[state].append({'write': write_val, 'move': move_val, 'next': next_state})
for j in range(steps):
    instructions = states[current_state][1 if i in tape else 0]
    if instructions['write'] == '1':
        tape.add(i)
    else:
        tape.discard(i)
    i += instructions['move']
    current_state = instructions['next']
print(len(tape))
