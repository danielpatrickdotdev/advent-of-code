#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Program:
    opcode_list = [
        "addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori",
        "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr",
    ]

    def __init__(self, lines_to_parse):
        self.register = [0] * 6
        self.instructions = []
        self.next_instruction = 0

        for line in lines_to_parse:
            parts = line.split()
            if parts[0][0] == "#":
                self.ip = int(parts[1])
            else:
                if parts[0] not in self.opcode_list:
                    raise Exception("Sneaky")
                self.instructions.append(
                    [parts[0], int(parts[1]), int(parts[2]), int(parts[3])]
                )

    def execute(self):
        while self.can_execute():
            self.step()
            self.next_instruction += 1

    def step(self):
        opcode, a, b, c = self.instructions[self.next_instruction]

        self.register[self.ip] = self.next_instruction
        getattr(self, opcode)(a, b, c)
        self.next_instruction = self.register[self.ip]

    def can_execute(self):
        return self.next_instruction < len(self.instructions)

    def addr(self, a, b, c):
        self.register[c] = self.register[a] + self.register[b]

    def addi(self, a, b, c):
        self.register[c] = self.register[a] + b

    def mulr(self, a, b, c):
        self.register[c] = self.register[a] * self.register[b]

    def muli(self, a, b, c):
        self.register[c] = self.register[a] * b

    def banr(self, a, b, c):
        self.register[c] = self.register[a] & self.register[b]

    def bani(self, a, b, c):
        self.register[c] = self.register[a] & b

    def borr(self, a, b, c):
        self.register[c] = self.register[a] | self.register[b]

    def bori(self, a, b, c):
        self.register[c] = self.register[a] | b

    def setr(self, a, b, c):
        self.register[c] = self.register[a]

    def seti(self, a, b, c):
        self.register[c] = a

    def gtir(self, a, b, c):
        self.register[c] = int(a > self.register[b])

    def gtri(self, a, b, c):
        self.register[c] = int(self.register[a] > b)

    def gtrr(self, a, b, c):
        self.register[c] = int(self.register[a] > self.register[b])

    def eqir(self, a, b, c):
        self.register[c] = int(a == self.register[b])

    def eqri(self, a, b, c):
        self.register[c] = int(self.register[a] == b)

    def eqrr(self, a, b, c):
        self.register[c] = int(self.register[a] == self.register[b])
