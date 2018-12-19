#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from collections import Counter

DEBUG = False#True


class Program:
    opcode_list = [
        "addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori",
        "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr",
    ]

    def __init__(self, lines_to_parse, register=[0, 0, 0, 0, 0, 0]):
        self.register = register
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

        self.log = []
        self.counts = Counter()
        self.step_count = 0

    def execute(self):
        while self.can_execute():
            self.step()
            self.step_count += 1
            self.next_instruction += 1

        print("Executed {} instructions".format(len(self.log)))
        for i, c in sorted(self.counts.items()):
            print("Executed instruction {} {} times".format(i, c))

        print("\nFirst 30 instructions:")
        for entry in self.log[:30]:
            print(entry)

        print("\nLast 30 instructions:")
        for entry in self.log[-30:]:
            print(entry)

    def step(self):
        self.register[self.ip] = self.next_instruction
        opcode, a, b, c = self.instructions[self.next_instruction]
        getattr(self, opcode)(a, b, c)

        self.counts[self.next_instruction] += 1
        log_entry = "{} - {:2d}: {}({:2d}, {:2d}, {:2d}) ".format(
            self.step_count, self.next_instruction, opcode, a, b, c
        )

        log_entry += "[{} {} {} {} {} {}]".format(*self.register)
        self.log.append(log_entry)
        if self.next_instruction == 7:
            print(log_entry)

        if DEBUG:
            print(log_entry)
            time.sleep(1)

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
