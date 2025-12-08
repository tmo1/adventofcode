# https://adventofcode.com/2025/day/7

manifold = open(0).readlines()
beams, counter = {manifold[0].index('S')}, 0
for level in manifold[1:]:
    new_beams = set()
    for beam in beams:
        if level[beam] == '^': new_beams, counter = new_beams | {beam - 1, beam + 1}, counter + 1
        else: new_beams.add(beam)
    beams = new_beams
print(counter)
