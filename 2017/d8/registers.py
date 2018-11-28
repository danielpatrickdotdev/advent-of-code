#!/usr/bin/env python3


import operator

class Registers:
    TESTS = {
        '>':  operator.gt,
        '>=': operator.ge,
        '==': operator.eq,
        '<=': operator.le,
        '<':  operator.lt,
        '!=': operator.ne
    }

    def __init__(self, path):
        self._registers = {}
        self._instructions = []
        self._max = None

        with open(path, encoding='utf-8') as infile:
            for line in infile:
                reg = line.split()
                name = reg[0]
                instruction = int(reg[2])
                if reg[1] == "dec":
                    instruction *= -1

                if len(reg) == 7 and reg[5] in self.TESTS:
                    test = (reg[4], reg[5], int(reg[6]))
                else:
                    raise Exception("oops")
                self._instructions.append((name, instruction, test))

        self.run_instructions()


    def run_instructions(self):
        for (register, instruction,
             (test_reg, test_op, test_val)) in self._instructions:
            if not register in self._registers:
                self._registers[register] = 0
            if not test_reg in self._registers:
                self._registers[test_reg] = 0
            if self.TESTS[test_op](self._registers[test_reg], test_val):
                self._registers[register] += instruction
            if self._max == None or self._registers[register] > self._max:
                self._max = self._registers[register]

    @property
    def largest(self):
        largest = max(self._registers, key=self._registers.get)
        return (largest, self._registers[largest])

    @property
    def max(self):
        return self._max


regs = Registers("input.txt")
print(regs.largest)
print(regs.max)
