#!/usr/bin/env python3

import string


def get_input(path):
    with open(path) as infile:
        return [line for line in infile.read().split('\n')]

class Particle:

    def __init__(self, p, v, a):
        self.p = [n for n in p]
        self.v = [n for n in v]
        self.a = [n for n in a]

    def tick(self):
        for n in range(3):
            self.v[n] += self.a[n]
            self.p[n] += self.v[n]

    @property
    def distance_from_origin(self):
        return sum([abs(n) for n in self.p])

    @property
    def acceleration(self):
        return sum([abs(n) for n in self.a])

    def __repr__(self):
        return ' '.join([str(attrib) for attrib in (self.p, self.v, self.a)])


class Swarm:
    def __init__(self, buffer_text_lines):
        self.particles = []
        for particle_text in buffer_text_lines:
            self.particles.append(
                Particle(*self.get_particle_attribs(particle_text))
            )

    def get_particle_attribs(self, text):
        def get_attrib_values(attrib_text):
            return tuple(int(n) for n in attrib_text[3:-1].split(','))

        return tuple(get_attrib_values(attrib) for attrib in text.split(', '))

    def get_lowest_accel_particles(self):
        lowest = None
        particles = []
        for n in range(len(self.particles)):
            particle = self.particles[n]
            accel = particle.acceleration
            if lowest is None:
                lowest = accel
                particles = [n]
            elif accel < lowest:
                lowest = accel
                particles = [n]
            elif accel == lowest:
                particles.append(n)
        return particles

    def simulate(self):
        ticks = 1000
        while self.particles and ticks > 0:
            if ticks < 1000 and ticks % 100 == 0:
                print(str(ticks) + ":", len(self.particles))
            for particle in self.particles:
                particle.tick()
            collisions = self.get_collided_particles()
            collision_count = 0
            for c in collisions:
                self.particles.pop(c - collision_count)
                collision_count += 1
            ticks -= 1
        return len(self.particles)

    def get_collided_particles(self):
        positions = [p.p for p in self.particles]
        collisions = []
        particles = self.particles[:]
        for n in range(len(particles)):
            if positions.count(particles[n].p) > 1:
                collisions.append(n)
        return collisions

    def __repr__(self):
        return '\n'.join([str(particle) for particle in self.particles])


if __name__ == '__main__':
    starting_buffer = get_input("input.txt")
    swarm = Swarm(starting_buffer)
    print(swarm.get_lowest_accel_particles())
    print(swarm.simulate())
