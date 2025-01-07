# https://adventofcode.com/2024/day/24#part2

wires, gates = open(0).read().split('\n\n')
wires, gates = {wire[:3]: True if wire[5] == '1' else False for wire in wires.split('\n')}, [gate.split() for gate in gates.strip().split('\n')]
for gate in gates:
    if gate[0][0] > gate[2][0]: gate[0], gate[2] = gate[2], gate[0]
level1_gates = sorted([gate for gate in gates if gate[0][0] == 'x'])
level2_xor_gates = [gate for gate in gates if gate[1] == 'XOR' and gate not in level1_gates]
and_gates = [gate for gate in gates if gate[1] == 'AND']
or_gates = [gate for gate in gates if gate[1] == 'OR']
final_gates = sorted([gate for gate in gates if gate[4][0] == 'z'], key=lambda x: x[4])
wrong = set()
for i in range(45):
    xor_gate, and_gate, final_gate, final_wires = level1_gates[i * 2 + 1], level1_gates[i * 2], final_gates[i], [final_gates[i][0], final_gates[i][2]]
    if i == 0:
        if xor_gate != final_gate: wrong |= {xor_gate[4], final_gate[4]}
        carry_in = and_gate[4]
    else:
        xor_ab = xor_gate[4]
        xor2_operands = (xor_gate[4], carry_in) if xor_gate[4] < carry_in else (carry_in, xor_gate[4])
        if final_gate not in level2_xor_gates:
            for gate in level2_xor_gates:
                if (gate[0], gate[2]) == xor2_operands:
                    wrong |= {final_gate[4], gate[4]}
                    final_gate = gate
                    break
        if carry_in not in final_wires and xor_gate[4] in final_wires:
            wrong |= {carry_in, final_gate[0] if final_gate[0] != xor_gate[4] else final_gate[2]}
        elif xor_gate[4] not in final_wires and carry_in in final_wires:
            xor_ab = final_gate[0] if final_gate[0] != carry_in else final_gate[2]
            wrong |= {xor_gate[4], xor_ab}
        and_operands = (final_gate[0], final_gate[2]) if final_gate[0] < final_gate[2] else (final_gate[2], final_gate[0])
        for gate in and_gates:
            if (gate[0], gate[2]) == and_operands:
                or_operand = gate[4]
                break
        or_operands = (and_gate[4], or_operand) if and_gate[4] < or_operand else (or_operand, and_gate[4])
        for gate in or_gates:
            if (gate[0], gate[2]) == or_operands:
                break
            if or_operand in gate:
                wrong |= {and_gate[4], gate[0] if gate[0] != or_operand else gate[2]}
                break
            if and_gate[4] in gate:
                wrong |= {or_operand, gate[0] if gate[0] != and_gate[4] else gate[2]}
                break
        carry_in = gate[4]
print(','.join(sorted(wrong)))
