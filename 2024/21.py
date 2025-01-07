# https://adventofcode.com/2024/day/21

numpad = {'7': (0, 0), '8': (1, 0), '9': (2, 0), '4': (0, 1), '5': (1, 1), '6': (2, 1), '1': (0, 2), '2': (1, 2), '3': (2, 2), '0': (1, 3), 'A': (2, 3)}
dirpad = {'^': (1, 0), 'A': (2, 0), '<': (0, 1), 'v': (1, 1), '>': (2, 1)}
keypad_dirs = {}
for num1, loc1 in numpad.items():
    for num2, loc2 in numpad.items():
        num_pair = (num1, num2)
        if loc1[0] == loc2[0]: keypad_dirs[num_pair] = ('v' if loc1[1] < loc2[1] else '^') * abs(loc1[1] - loc2[1])
        elif loc1[1] == loc2[1]: keypad_dirs[num_pair] = ('>' if loc1[0] < loc2[0] else '<') * abs(loc1[0] - loc2[0])
        else:
            if loc1[0] == 0 and loc2[1] == 3: keypad_dirs[num_pair] = '>' * (loc2[0] - loc1[0]) + 'v' * (loc2[1] - loc1[1])
            elif loc1[1] == 3 and loc2[0] == 0: keypad_dirs[num_pair] = '^' * (loc1[1] - loc2[1]) + '<' * (loc1[0] - loc2[0])
            else: keypad_dirs[num_pair] = [('v' if loc1[1] < loc2[1] else '^') * abs(loc1[1] - loc2[1]), ('>' if loc1[0] < loc2[0] else '<') * abs(loc1[0] - loc2[0])]
for dir1, loc1 in dirpad.items():
    for dir2, loc2 in dirpad.items():
        dir_pair = (dir1, dir2)
        if loc1[0] == loc2[0]: keypad_dirs[dir_pair] = ('v' if loc1[1] < loc2[1] else '^') * abs(loc1[1] - loc2[1])
        elif loc1[1] == loc2[1]: keypad_dirs[dir_pair] = ('>' if loc1[0] < loc2[0] else '<') * abs(loc1[0] - loc2[0])
        else:
            if loc1[0] == 0 and loc2[1] == 0: keypad_dirs[dir_pair] = '>' * (loc2[0] - loc1[0]) + '^'
            elif loc1[1] == 0 and loc2[0] == 0: keypad_dirs[dir_pair] = 'v' + (loc1[0] - loc2[0]) * '<'
            else: keypad_dirs[dir_pair] = [('v' if loc1[1] < loc2[1] else '^') * abs(loc1[1] - loc2[1]), ('>' if loc1[0] < loc2[0] else '<') * abs(loc1[0] - loc2[0])]

def keypress(i, new_sequence):
    if i == len(sequence):
        sequences.append(new_sequence)
    else:
        presses = keypad_dirs[('A' if i == 0 else sequence[i - 1], sequence[i])]
        if isinstance(presses, list):
            keypress(i + 1, new_sequence + presses[0] + presses[1] + 'A')
            keypress(i + 1, new_sequence + presses[1] + presses[0] + 'A')
        else:
            keypress(i + 1, new_sequence + presses + 'A')

total = 0
for robot1 in open(0).read().split():
    sequences, sequence = [], robot1
    keypress(0, '')
    old_sequences, sequences = sequences, []
    for robot2 in old_sequences:
        sequence = robot2
        keypress(0, '')
    old_sequences, sequences = sequences, []
    for robot3 in old_sequences:
        sequence = robot3
        keypress(0, '')
    total += min([len(sequence) for sequence in sequences]) * int(robot1[:-1])
print(total)
