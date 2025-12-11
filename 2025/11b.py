# https://adventofcode.com/2025/day/11#part2

def traverse(node):
    if node[0] == 'out': return 1 if node[1] and node[2] else 0
    if node in memos: return memos[node]
    memos[node] = sum([traverse((next_device, node[1] or node[0] == 'dac', node[2] or node[0] == 'fft')) for next_device in network[node[0]]])
    return memos[node]

network, memos = {}, {}
for line in open(0):
    device, outputs = line.strip().split(': ')
    network[device] = outputs.split()
print(traverse(('svr', False, False)))
