#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from pathlib import Path


def addr(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a] + reg[b]
    return reg


def addi(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a] + b
    return reg

def mulr(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a] * reg[b]
    return reg


def muli(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a] * b
    return reg


def banr(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a] & reg[b]
    return reg


def bani(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a] & b
    return reg


def borr(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a] | reg[b]
    return reg


def bori(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a] | b
    return reg


def setr(a, b, c, reg):
    reg = reg[:]
    reg[c] = reg[a]
    return reg


def seti(a, b, c, reg):
    reg = reg[:]
    reg[c] = a
    return reg


def gtir(a, b, c, reg):
    reg = reg[:]
    reg[c] = int(a > reg[b])
    return reg


def gtri(a, b, c, reg):
    reg = reg[:]
    reg[c] = int(reg[a] > b)
    return reg


def gtrr(a, b, c, reg):
    reg = reg[:]
    reg[c] = int(reg[a] > reg[b])
    return reg


def eqir(a, b, c, reg):
    reg = reg[:]
    reg[c] = int(a == reg[b])
    return reg


def eqri(a, b, c, reg):
    reg = reg[:]
    reg[c] = int(reg[a] == b)
    return reg


def eqrr(a, b, c, reg):
    reg = reg[:]
    reg[c] = int(reg[a] == reg[b])
    return reg


def parse(input_text):
    instructions = []
    current_instruction = []
    last_line = None

    parse_program = False
    program = []

    for line in input_text:
        if parse_program:
            if line:
                program.append([int(c) for c in line.split()])
        elif not line:
            if not last_line:
                parse_program = True
            else:
                instructions.append(current_instruction)
                current_instruction = []

        elif line.split()[0] in ["Before:", "After:"]:
            current_instruction.append([
                int(c) for c in line[9: -1].split(", ")
            ])
        else:
            current_instruction.append([int(c) for c in line.split()])

        last_line = line

    return instructions, program


def solve(input_text):
    opcodes = [
        addr, addi, mulr, muli, banr, bani, borr, bori,
        setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr
    ]
    instructions, program = parse(input_text)

    potentials = defaultdict(set)

    for before, (op, a, b, c), after in instructions:
        working = []
        for opcode in opcodes:
            try:
                reg = opcode(a, b, c, before)
            except IndexError:
                pass
            else:
                if reg == after:
                    working.append(opcode)

        potentials[op].update(working)

    opcodes_to_assign = opcodes[:]
    opcode_numbers = {}

    loops = 0

    while opcodes_to_assign and loops < 1000:
        for key in sorted(potentials.keys()):
            if len(potentials[key]) == 1:
                opcode = potentials[key].pop()
                opcodes_to_assign.remove(opcode)
                opcode_numbers[key] = opcode
                for value in potentials.values():
                    value.discard(opcode)
        loops += 1

    if loops == 1000:
        raise Exception("Something's up")

    reg = [0, 0, 0, 0]
    for op, a, b, c in program:
        reg = opcode_numbers[op](a, b, c, reg)

    return reg[0]


if __name__ == '__main__':
    from shared.utils import get_input
    from timeit import default_timer as timer

    start = timer()

    input_path = Path(__file__).parent.joinpath("input.txt")
    input_text = get_input(input_path)
    solution = solve(input_text)
    print(solution)

    end = timer()
    print()
    print("-" * 80)
    print("Time elapsed: {:.3f}s".format(end - start))
