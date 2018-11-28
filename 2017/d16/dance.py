#!/usr/bin/env python3

import string


def get_input(path):
    with open(path) as infile:
        return infile.read()


class Dancer:

    def __init__(self, text, num_programs):
        if num_programs > 26:
            raise Exception

        self._programs = list(string.ascii_lowercase[:num_programs])
        self._starting_programs = list(string.ascii_lowercase[:num_programs])
        self._moves = text.split(",")

    def get_swaps(self, move):
        return move[1:].split('/')

    def spin(self, n):
        self._programs = self._programs[-n:] + self._programs[:-n]

    def swap_pos(self, first, second):
        temp = self._programs[first]
        self._programs[first] = self._programs[second]
        self._programs[second] = temp

    def swap_prog(self, first, second):
        first = self._programs.index(first)
        second = self._programs.index(second)
        self.swap_pos(first, second)

    def move(self, move):
        if move[0] == "s":
            self.spin(int(move[1:]))
        elif move[0] == "x":
            first, second = self.get_swaps(move)
            self.swap_pos(int(first), int(second))
        elif move[0] == "p":
            first, second = self.get_swaps(move)
            self.swap_prog(first, second)
        else:
            raise Exception

    def dance(self):
        for move in self._moves:
            self.move(move)

    def multi_dance(self, num_times):
        n = 0
        while n < num_times:
            n += 1
            self.dance()
            if self._programs == self._starting_programs:
                mult = int(num_times // n)
                n *= mult

    @property
    def programs(self):
        return ''.join(self._programs)

if __name__ == '__main__':
    text = get_input("input.txt")
    dancer = Dancer(text, 16)
    dancer.dance()
    print(dancer.programs)

    dancer2 = Dancer(text, 16)
    dancer2.multi_dance(1000000000)
    print(dancer2.programs)
