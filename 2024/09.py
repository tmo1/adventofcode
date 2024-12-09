# https://adventofcode.com/2024/day/9

def check_if_done():
    if a == b:
        print(sum([i * n for i, n in enumerate(disk[:a])]))
        quit()

disk, line = [], open(0).read().strip() + '0'
for i in range(len(line) // 2): disk += [i for j in range(int(line[i * 2]))] + [-1 for j in range(int(line[i * 2 + 1]))]
a, b = 0, len(disk) - 1
while True:
    while disk[a] != -1:
        a += 1
        check_if_done()
    while disk[b] == -1:
        b -= 1
        check_if_done()
    disk[a], disk[b] = disk[b], -1
