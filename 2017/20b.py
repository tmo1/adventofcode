# https://adventofcode.com/2017/day/20#part2
# This solution gives the right answer (at least for my input), but is not really legitimate - we just simulate 1000
# ticks, and assume that there will be no further collisions. A more rigorous (but much more complicated and slower)
# solution might alternate between simulating some number of ticks and using quadratic equations to definitively
# ascertain whether any given pair of particles will ever collide in the future.

particles = []
for i, line in enumerate(open(0)):
    line = line.strip().split(', ')
    particles.append([[int(x) for x in y[3:-1].split(',')] for y in line])
for i in range(1000):
    particles_next, collided_particles = {}, set()
    for j, particle in enumerate(particles):
        for k in range(3):
            particle[1][k] += particle[2][k]
            particle[0][k] += particle[1][k]
        position = tuple(particle[0])
        if position in collided_particles:
            continue
        if position in particles_next:
            del particles_next[position]
            collided_particles.add(position)
            continue
        particles_next[position] = j
    particles = [particles[j] for j in particles_next.values()]
print(len(particles))
