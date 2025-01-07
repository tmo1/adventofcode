# https://adventofcode.com/2024/day/23

connections = [{connection[:2], connection[3:]} for connection in open(0).read().split()]
total = 0
for i in range(len(connections) - 2):
    for j in range(i + 1, len(connections) - 1):
        lan = connections[i] | connections[j]
        if len(lan) == 3:
            for k in range(j + 1, len(connections)):
                if connections[k].issubset(lan) and 't' in {computer[0] for computer in connections[i] | connections[j] | connections[k]}:
                    total += 1
print(total)
