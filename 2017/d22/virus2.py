#!/usr/bin/env python3

import sys


def get_input(path):
    with open(path) as infile:
        return [list(line) for line in infile.read().split('\n')]

class Grid:

    DIRECTIONS = ["^", ">", "v", "<"]
    STATES = [".", "W", "#", "F"]
    EXPAND_BY = 5

    def __init__(self, initial_data):
        self._grid = self.read(initial_data)
        self.x = self.width // 2
        self.y = self.height // 2
        self.direction = 0


    def read(self, data):
        rows = []
        for row in data:
            rows.append(
                [self.STATES.index(c) for c in row]
            )
        return rows

    @property
    def state(self):
        return self.STATES[self.get()]

    @property
    def height(self):
        return len(self._grid)

    @property
    def width(self):
        if len(self._grid) > 0:
            return len(self._grid[0])
        else:
            return 0

    def move(self):
        if self.direction == 0:
            self.y -= 1
            if self.y == 0:
                self.expand_up(self.EXPAND_BY)
                self.y += self.EXPAND_BY
        elif self.direction == 1:
            self.x += 1
            if self.x >= self.width:
                self.expand_right(self.EXPAND_BY)
        elif self.direction == 2:
            self.y += 1
            if self.y >= self.height:
                self.expand_down(self.EXPAND_BY)
        elif self.direction == 3:
            self.x -= 1
            if self.x == 0:
                self.expand_left(self.EXPAND_BY)
                self.x += self.EXPAND_BY
        else:
            raise Exception

    def get(self):
        return self._grid[self.y][self.x]

    def set(self, char):
        self._grid[self.y][self.x] = char

    def evolve(self):
        self.set((self.get() + 1) % 4)

    def turn_right(self):
        self.direction += 1
        self.direction %= 4

    def turn_left(self):
        self.direction -= 1
        self.direction %= 4

    def turn_around(self):
        self.turn_left()
        self.turn_left()

    def expand_left(self, n):
        for i in range(self.height):
            self._grid[i] = [0] * n + self._grid[i]

    def expand_right(self, n):
        for i in range(self.height):
            self._grid[i] += [0] * n

    def expand_up(self, n):
        new_rows = [[0] * self.width for x in range(n)]
        self._grid = new_rows + self._grid

    def expand_down(self, n):
        new_rows = [[0] * self.width for x in range(n)]
        self._grid += new_rows

    def __repr__(self):
        return '\n'.join(
            [''.join(
                [self.STATES[n] for n in row]
            ) for row in self._grid]
        )


class Virus:

    def __init__(self, grid_data):
        self.grid = Grid(grid_data)
        self.new_infection_count = 0

    def act(self, num_bursts):
        for n in range(num_bursts):
            if self.grid.state == '.':
                self.grid.turn_left()
                self.grid.evolve()
                self.grid.move()
            elif self.grid.state == 'W':
                self.grid.evolve()
                self.grid.move()
                self.new_infection_count += 1
            elif self.grid.state == '#':
                self.grid.turn_right()
                self.grid.evolve()
                self.grid.move()
            elif self.grid.state == 'F':
                self.grid.turn_around()
                self.grid.evolve()
                self.grid.move()
            else:
                raise Exception


if __name__ == '__main__':
    n = int(sys.argv[1])
    starting_map = get_input("input.txt")
    v = Virus(starting_map)
    v.act(n)
    print("New infections", v.new_infection_count)
