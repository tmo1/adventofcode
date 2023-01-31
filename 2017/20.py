# https://adventofcode.com/2017/day/20

asymptotic_distances = []
for i, line in enumerate(open(0)):
    line = line.strip().split(', ')
    asymptotic_distances.append([sum([abs(int(x)) for x in y[3:-1].split(',')]) for y in line])
particles_a, asymptotic_a = [], 1000000
for i in range(len(asymptotic_distances)):
    if asymptotic_distances[i][2] < asymptotic_a:
        particles_a = [i]
        asymptotic_a = asymptotic_distances[i][2]
    elif asymptotic_distances[i][2] == asymptotic_a:
        particles_a.append(i)
particles_v, asymptotic_v = [], 1000000
for i in particles_a:
    if asymptotic_distances[i][1] < asymptotic_v:
        particles_v = [i]
        asymptotic_v = asymptotic_distances[i][1]
    elif asymptotic_distances[i][1] == asymptotic_v:
        particles_v.append(i)
particles_p, asymptotic_p = [], 1000000
for i in particles_v:
    if asymptotic_distances[i][0] < asymptotic_p:
        particles_p = [i]
        asymptotic_p = asymptotic_distances[i][0]
    elif asymptotic_distances[i][0] == asymptotic_p:
        particles_p.append(i)
print(asymptotic_p)
