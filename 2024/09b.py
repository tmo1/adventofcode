# https://adventofcode.com/2024/day/9#part2

line, disk, free_spaces, files = open(0).read().strip() + '0', [], [], []
for i in range(len(line) // 2):
    n, m = int(line[i * 2]), int(line[i * 2 + 1])
    files.append((len(disk), n))
    if m > 0: free_spaces.append([len(disk) + n, m])
    disk += [i for j in range(n)] + [-1 for j in range(m)]
for file in files[::-1]:
    for free_space in free_spaces:
        if free_space[0] >= file[0]: break
        if file[1] <= free_space[1]:
            for i in range(file[1]): disk[free_space[0] + i], disk[file[0] + i] = disk[file[0] + i], -1
            free_space[0], free_space[1] = free_space[0] + file[1], free_space[1] - file[1]
            break
print(sum([i * n for i, n in enumerate(disk) if n > 0]))
