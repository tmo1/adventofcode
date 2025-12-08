# https://adventofcode.com/2025/day/8

from math import prod

boxes = [tuple([int(n) for n in line.split(',')]) for line in open(0)]
pairs = sorted([[box1, box2] for i, box1 in enumerate(boxes) for box2 in boxes[i + 1:]], key=lambda x: sum([(x[0][n] - x[1][n]) ** 2 for n in range(3)]) ** .5)[:1000]
circuits = [[{box}, set()] for box in boxes]
done = False
while not done:
    done = True
    for circuit in circuits:
        circuit[1] = {pair[1] for pair in pairs if pair[0] in circuit[0] and pair[1] not in circuit[0]}
    for i, circuit1 in enumerate(circuits):
            for j, circuit2 in enumerate(circuits[i + 1:], start=i + 1):
                if (circuit1[1] & circuit2[0]) or (circuit1[0] & circuit2[1]):
                    circuits[i][0] |= circuit2[0]
                    circuits[i][1] = {pair[1] for pair in pairs if pair[0] in circuit1[0] and pair[1] not in circuit1[0]}
                    circuits[j] = [set(), set()]
                    done = False
print(prod(sorted([len(circuit[0]) for circuit in circuits])[-3:]))
