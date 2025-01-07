# https://adventofcode.com/2024/day/21#part2
# This is a more efficient and concise solution to part 1 as well, with the appropriate modification to the 'next_robot' procedure

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
known_sequences = {}

def next_robot(new_sequence, level):
    if (new_sequence, level) in known_sequences: return known_sequences[(new_sequence, level)]
    if level == 26:
    #for part 1, just change '26' to '3'
        n = len(new_sequence)
    else:
        n = 0
        for i, c in enumerate(new_sequence):
            presses = keypad_dirs[('A' if i == 0 else new_sequence[i - 1], c)]
            n += min(next_robot(presses[0] + presses[1] + 'A', level + 1), next_robot(presses[1] + presses[0] + 'A', level + 1)) if isinstance(presses, list) else next_robot(presses + 'A', level + 1)
    known_sequences[(new_sequence, level)] = n
    return n

print(sum([next_robot(code, 0) * int(code[:-1]) for code in open(0).read().split()]))
