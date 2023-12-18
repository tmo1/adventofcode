# https://adventofcode.com/2023/day/13

pattern = []
fh = open(0)
total = 0
while True:
    line = fh.readline()
    if line == '\n' or line == '':
        found = False
        for i in range(1, len(pattern)):
            reflect_range = min(i, len(pattern) - i)
            for j in range(1, reflect_range + 1):
                if pattern[i - j] != pattern[i + j - 1]:
                    break
            else:
                found = True
                total += 100 * i
                break
        if not found:
            for i in range(1, len(pattern[0])):
                reflect_range = min(i, len(pattern[0]) - i)
                for j in range(1, reflect_range + 1):
                    if [pattern[n][i - j] for n in range(len(pattern))] != [pattern[n][i + j - 1] for n in range(len(pattern))]:
                        break
                else:
                    total += i
        if line == '':
            print(total)
            quit()
        pattern = []
    else:
        pattern.append(line.strip())
