# https://adventofcode.com/2017/day/21
# solution for both parts - see comment toward the end of the program

rules = {}


def rotate(pi, po):
    global rules
    for ii in range(4):
        # https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
        pi = list(zip(*pi[::-1]))
        rules[''.join([y for x in pi for y in x])] = po


for line in open(0):
    pattern_in, pattern_out = line.split(' => ')
    pattern_in = [[pattern_in[x] for x in range(y, y + 2)] for y in range(0, 6, 3)] if len(
        pattern_in) == 5 else [[pattern_in[x] for x in range(y, y + 3)] for y in range(0, 12, 4)]
    pattern_out = [[pattern_out[x] for x in range(y, y + 3)] for y in range(0, 12, 4)] if len(
        pattern_out) == 12 else [[pattern_out[x] for x in range(y, y + 4)] for y in
                                 range(0, 20, 5)]
    rotate(pattern_in, pattern_out)
    pattern_in.reverse()
    rotate(pattern_in, pattern_out)
    for x in pattern_in:
        x.reverse()
    rotate(pattern_in, pattern_out)
art = [['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]


def replace(n):
    global art
    z, m = len(art) // n, n + 1
    new_art = [[' ' for _ in range(z * m)] for _ in range(z * m)]
    for j in range(z):
        jj, jjj = j * n, j * m
        for k in range(z):
            square = []
            kk, kkk = k * n, k * m
            for y in range(jj, jj + n):
                for x in range(kk, kk + n):
                    square.append(art[y][x])
            square = rules[''.join(square)]
            for y in range(m):
                for x in range(m):
                    new_art[jjj + y][kkk + x] = square[y][x]
    art = new_art


# range(5) for part 1, range(18) for part 2
for i in range(18):
    replace(2 if len(art) % 2 == 0 else 3)
print(sum([1 for j in art for i in j if i == '#']))
