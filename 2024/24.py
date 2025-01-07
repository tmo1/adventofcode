# https://adventofcode.com/2024/day/24

wires, gates = open(0).read().split('\n\n')
wires, gates = {wire[:3]: True if wire[5] == '1' else False for wire in wires.split('\n')}, [gate.split() for gate in gates.strip().split('\n')]
flag = True
while flag:
    flag = False
    for gate in gates:
        if gate[4] not in wires and gate[0] in wires and gate[2] in wires:
            wires[gate[4]] = True if ((gate[1] == 'AND' and wires[gate[0]] and wires[gate[2]]) or (gate[1] == 'OR' and (wires[gate[0]] or wires[gate[2]])) or (gate[1] == 'XOR' and (wires[gate[0]] != wires[gate[2]]))) else False
            flag = True
print(int(''.join([x[1] for x in sorted([(k, '1' if v else '0') for k, v in wires.items() if k[0] == 'z'], key=lambda x: x[0], reverse=True)]), 2))
