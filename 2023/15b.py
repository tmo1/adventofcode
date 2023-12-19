# https://adventofcode.com/2023/day/15#part2


def aoc_hash(s):
    v = 0
    for char in s:
        v += ord(char)
        v *= 17
        v %= 256
    return v


boxes = [[] for i in range(256)]
for step in open(0).readline().strip().split(','):
    operation = step.find('-')
    if step[-1] == '-':
        label = step[:-1]
        box = aoc_hash(label)
        for n, lens in enumerate(boxes[box]):
            if lens[0] == label:
                boxes[box] = boxes[box][:n] + boxes[box][n + 1:]
                break
    else:
        operation = step.find('=')
        label = step[:operation]
        box = boxes[aoc_hash(label)]
        focal_length = int(step[operation + 1])
        for n, lens in enumerate(box):
            if lens[0] == label:
                box[n] = (label, focal_length)
                break
        else:
            box.append((label, focal_length))
print(sum([(n + 1) * (m + 1) * boxes[n][m][1] for n in range(256) for m in range(len(boxes[n]))]))
