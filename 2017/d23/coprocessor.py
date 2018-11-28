#!/usr/bin/env python3

import string


def get_input(path):
    with open(path) as infile:
        return [line.split() for line in infile.read().split('\n')]


class Instruction:

    def __init__(self, data):
        if len(data) != 3:
            raise Exception

        if data[0] not in ("set", "sub", "mul", "jnz"):
            raise Exception
        self._instruction = data[0]
        self._x = data[1]
        self._y = data[2]

    @property
    def instruction(self):
        return self._instruction

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class Coprocessor:

    def __init__(self, data):
        self._instructions = [Instruction(i) for i in data]
        self._registers = {}

    def process(self):
        count = 0
        n = 0
        while n < len(self._instructions):
            n = self.execute(n)
            n += 1
            count += 1

    def execute(self, n):
        instruction = self._instructions[n]
        i, x, y = instruction.instruction, instruction.x, instruction.y
        if i == "set":
            self.set_register(x, self.resolve(y))
        elif i == "sub":
            self.sub_register(x, self.resolve(y))
        elif i == "mul":
            self.mul_register(x, self.resolve(y))
        elif i == "jnz":
            n = self.jnz(n, self.resolve(x), self.resolve(y))
        else:
            raise Exception
        return n

    def resolve(self, y):
        if y in string.ascii_lowercase:
            return self.get_register(y)
        else:
            return int(y)

    def get_register(self, x):
        return self._registers.get(x, 0)

    def set_register(self, x, y):
        self._registers[x] = y

    def sub_register(self, x, y):
        self.set_register(x, self.get_register(x) - y)

    def mul_register(self, x, y):
        self.set_register(x, self.get_register(x) * y)

    def jnz(self, n, x, y):
        if x == 0:
            return n
        else:
            return n + y - 1

    @property
    def registers(self):
        return ' '.join(
            [a + ' ' + str(
                self._registers[a]) for a in sorted(self._registers.keys())]
        )


class Coprocessor1(Coprocessor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mul_count = 0

    def mul_register(self, x, y):
        self.mul_count += 1
        self.set_register(x, self.get_register(x) * y)


if __name__ == '__main__':
    instructions = get_input("input.txt")
    c1 = Coprocessor1(instructions)
    c1.process()
    print(c1.mul_count)
