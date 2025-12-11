# https://adventofcode.com/2025/day/11

def traverse(device_):
    if device_ in memos: return memos[device_]
    memos[device_] = sum([traverse(next_device) for next_device in network[device_]])
    return memos[device_]

network, memos = {}, {'out': 1}
for line in open(0):
    device, outputs = line.strip().split(': ')
    network[device] = outputs.split()
print(traverse('you'))
