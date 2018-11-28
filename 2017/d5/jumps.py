#!/usr/bin/env python3

from operator import eq as isequal

def import_input(path):
    with open(path, encoding='utf-8') as infile:
        return [int(line) for line in infile]


instructions = import_input("input.txt")


class Jumper:
    def __init__(self, instructions):
        self.instructions = instructions

    def solve(self):
        steps = 0
        i = 0

        while 0 <= i < len(self.instructions):
            jump = self.instructions[i]
            if self.instructions[i] >= 3:
                self.instructions[i] -= 1
            else:
                self.instructions[i] += 1
            i += jump
            steps += 1

        return steps

jump = Jumper(instructions)
print(jump.solve())
