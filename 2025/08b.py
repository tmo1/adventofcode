# https://adventofcode.com/2025/day/8#part2

boxes = [tuple([int(n) for n in line.split(',')]) for line in open(0)]
pairs = sorted([[box1, box2] for i, box1 in enumerate(boxes) for box2 in boxes[i + 1:]], key=lambda x: sum([(x[0][n] - x[1][n]) ** 2 for n in range(3)]) ** .5, reverse=True)
circuits = [{box} for box in boxes]
while True:
    pair = pairs.pop()
    circuit_pair = []
    for i, circuit in enumerate(circuits):
        if pair[0] in circuit: circuit_pair.append(i)
        if pair[1] in circuit: circuit_pair.append(i)
        if len(circuit_pair) == 2: break
    if circuit_pair[0] != circuit_pair[1]:
        circuits[circuit_pair[0]] |= circuits[circuit_pair[1]]
        if len(circuits[circuit_pair[0]]) == len(boxes):
            print(pair[0][0] * pair[1][0])
            quit()
        circuits[circuit_pair[1]] = set()
