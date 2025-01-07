# https://adventofcode.com/2024/day/23#part2

connections = {}
for line in open(0).read().split():
    connections[line[:2]] = connections[line[:2]] | {line[3:5]} if line[:2] in connections else {line[3:5]}
    connections[line[3:5]] = connections[line[3:5]] | {line[:2]} if line[3:5] in connections else {line[:2]}

def find_party(current_lan, remaining_computers):
    global lan_party
    if not remaining_computers:
        if len(current_lan) > len(lan_party): lan_party = current_lan
    elif len(current_lan) + len(remaining_computers) > len(lan_party):
        find_party(current_lan + [remaining_computers[0]], [computer for computer in remaining_computers[1:] if computer in connections[remaining_computers[0]]])
        find_party(current_lan, remaining_computers[1:])

lan_party = []
find_party([], [computer for computer in connections.keys()])
print(','.join(sorted(lan_party)))
