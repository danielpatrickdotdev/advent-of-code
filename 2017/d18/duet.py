#!/usr/bin/env python3

import string
from collections import deque


def get_input(path):
    with open(path) as infile:
        return infile.read().split('\n')


class Duet:

    def __init__(self, instructions_list):
        self.register = {}
        self.last_played = None
        self.instructions = []
        for instruction in instructions_list:
            instruction = instruction.split()
            keyword = instruction[0]
            register = instruction[1]
            if len(instruction) > 2:
                try:
                    y = int(instruction[2])
                except ValueError:
                    y = instruction[2]
                self.instructions.append((keyword, register, y))
            else:
                self.instructions.append((keyword, register, None))

    def execute(self):
        n = 0
        while n < len(self.instructions):
            keyword, x, y = self.instructions[n]
            if keyword == "snd":
                self.snd(x)
            elif keyword == "set":
                self.set(x, y)
            elif keyword == "add":
                self.add(x, y)
            elif keyword == "mul":
                self.mul(x, y)
            elif keyword == "mod":
                self.mod(x, y)
            elif keyword == "rcv":
                rcv = self.rcv(x)
                if rcv is not None:
                    return rcv
            elif keyword == "jgz":
                n += self.jgz(x, y)
            n += 1

    def lookup(self, x):
        if str(x) in string.ascii_lowercase:
            return self.register.get(x, 0)
        else:
            return x

    def snd(self, x):
        self.last_played = self.lookup(x)

    def set(self, x, y):
        self.register[x] = self.lookup(y)

    def add(self, x, y):
        self.register[x] = self.lookup(x) + self.lookup(y)

    def mul(self, x, y):
        self.register[x] = self.lookup(x) * self.lookup(y)

    def mod(self, x, y):
        self.register[x] = self.lookup(x) % self.lookup(y)

    def rcv(self, x):
        if self.lookup(x) != 0:
            return self.last_played

    def jgz(self, x, y):
        if self.lookup(x) > 0:
            return self.lookup(y) - 1
        else:
            return 0


class Duet2:

    def __init__(self, instructions_list, p):
        self.register = {}
        self.set("p", p)

        self.instructions = []
        for instruction in instructions_list:
            instruction = instruction.split()
            keyword = instruction[0]
            register = instruction[1]
            if len(instruction) > 2:
                try:
                    y = int(instruction[2])
                except ValueError:
                    y = instruction[2]
                self.instructions.append((keyword, register, y))
            else:
                self.instructions.append((keyword, register, None))
        self.pos = 0
        self.queue = deque()
        print("initialised")

    def is_awaiting_message(self):
        return self.instructions[self.pos][0] == "rcv" and len(self.queue) == 0

    def is_exhausted(self):
        return self.pos >= len(self.instructions) or self.is_awaiting_message()

    def enqueue(self, x):
        self.queue.append(x)

    def execute(self):
        keyword, x, y = self.instructions[self.pos]
        #print(self.register["p"], keyword, x, y)
        if keyword == "snd":
            self.pos += 1
            return self.snd(x)
        elif keyword == "set":
            self.set(x, y)
        elif keyword == "add":
            self.add(x, y)
        elif keyword == "mul":
            self.mul(x, y)
        elif keyword == "mod":
            self.mod(x, y)
        elif keyword == "rcv":
            self.rcv(x)
        elif keyword == "jgz":
            self.pos += self.jgz(x, y)
        self.pos += 1

    def lookup(self, x):
        if str(x) in string.ascii_lowercase:
            return self.register.get(x, 0)
        else:
            return int(x)

    def snd(self, x):
        return self.lookup(x)

    def set(self, x, y):
        self.register[x] = self.lookup(y)

    def add(self, x, y):
        self.register[x] = self.lookup(x) + self.lookup(y)

    def mul(self, x, y):
        self.register[x] = self.lookup(x) * self.lookup(y)

    def mod(self, x, y):
        self.register[x] = self.lookup(x) % self.lookup(y)

    def rcv(self, x):
        self.register[x] = self.queue.popleft()

    def jgz(self, x, y):
        if self.lookup(x) > 0:
            return self.lookup(y) - 1
        else:
            return 0

def duet2(instructions):
    a = Duet2(instructions, 0)
    b = Duet2(instructions, 1)
    count = 0
    while True:
        if not a.is_exhausted():
            for_b = a.execute()
            if for_b is not None:
                b.enqueue(for_b)
        elif not b.is_exhausted():
            for_a = b.execute()
            if for_a is not None:
                count += 1
                a.enqueue(for_a)
        else:
            break
    return count


if __name__ == '__main__':
    instructions = get_input("input.txt")
    duet = Duet(instructions)
    print(duet.execute())
    #duet2(instructions)
    print(duet2(instructions))
