#!/usr/bin/env python3

import string


def get_input(path):
    with open(path) as infile:
        return [[c.strip() for c in line] for line in infile.read().split('\n')]


class Route:
    TUBES = ('|', '-', '+')

    def __init__(self, network_diagram):
        self.diagram = network_diagram
        self.x = self.diagram[0].index('|')
        self.y = 0
        self.last_tube = ('|')
        self.letters = []
        self.dir = 1
        self.move_count = 0

    def move(self):
        tube = self.get_square(self.x, self.y)
        #print(self.x, self.y, tube)
        if not tube:
            return ''.join(self.letters)
        elif tube in self.TUBES:
            self.move_tube(tube)
        elif tube in string.ascii_uppercase:
            self.letters.append(tube)
            self.move_tube(self.last_tube)
        else:
            raise Exception
        self.move_count += 1

    def move_tube(self, tube):
        if tube == '+':
            self.last_tube = self.change_dir()
        if self.last_tube == '|':
            self.y += self.dir
            self.last_tube = '|'
        elif self.last_tube == '-':
            self.x += self.dir
            self.last_tube = '-'

    def change_dir(self):
        if self.last_tube == '|':
            if self.get_square(self.x - 1, self.y):
                #print("going left")
                self.dir = -1
            elif self.get_square(self.x + 1, self.y):
                #print("going right")
                self.dir = 1
            else:
                raise Exception
            return '-'
        if self.last_tube == '-':
            if self.get_square(self.x, self.y - 1):
                #print("going up")
                self.dir = -1
            elif self.get_square(self.x, self.y + 1):
                #print("going down")
                self.dir = 1
            else:
                raise Exception
            return '|'

    def get_square(self, x, y):
        return self.diagram[y][x]


if __name__ == '__main__':
    diagram = get_input("input.txt")
    route = Route(diagram)
    answer = None
    while answer is None:
        answer = route.move()
    print(answer)
    print(route.move_count)
