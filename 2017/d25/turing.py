#!/usr/bin/env python3

from collections import defaultdict


def get_input(path):
    with open(path) as infile:
        return [line for line in infile.read().split('\n')]


class Blueprint:

    def __init__(self, lines):
        self.tape = defaultdict(int)
        self.pos = 3
        self.rules = {}

        self.state = lines[0].split()[-1].strip('.')

        self.steps = int(lines[1].split()[-2])
        if self.steps < 0:
            raise Exception

        for n in range(2, len(lines) - 2, 10):
            self.create_state_rule(lines[n:n+10])

        if self.state not in self.rules:
            raise Exception

    def debug_print(self):
        tape = ""
        for n in range(len(self.tape)):
            if self.pos == n:
                tape += "[{}]".format(self.tape[n])
            else:
                tape += " {} ".format(self.tape[n])
        return tape

    def count_ones(self):
        return sum(self.tape.values())

    def run(self):
        while self.steps > 0:
            rule = self.rules[self.state]
            self.apply_rule(rule)
            self.steps -= 1
            if self.steps % 100000 == 0:
                print("Remaining:", self.steps, self.count_ones())
                # if self.steps % 300000 == 0:
            # if 12034000 < self.steps < 12034040:
            #     print(self.steps, self.count_ones())
            #     print(self.debug_print())
            # if self.count_ones() == 0:
            #     print(self.steps, 0)

    def apply_rule(self, rule):
        n = self.read()
        self.write(rule[n][0])
        self.move(rule[n][1])
        self.state = rule[n][2]

    def read(self):
        return self.tape[self.pos]

    def write(self, n):
        self.tape[self.pos] = n

    def move(self, n):
        self.pos += n
        #if self.pos < 0:
        #    self.tape.insert(0, 0)
        #elif self.pos >= len(self.tape):
        #    self.tape.append(0)

    def create_state_rule(self, lines):
        state_name = self.get_state(lines[1])

        zero_write = self.get_write(lines[3])
        zero_move = self.get_move(lines[4])
        zero_state = self.get_state(lines[5])

        one_write = self.get_write(lines[7])
        one_move = self.get_move(lines[8])
        one_state = self.get_state(lines[9])

        self.rules[state_name] = ((zero_write, zero_move, zero_state),
                                  (one_write, one_move, one_state))

    def get_state(self, line):
        return self.get_last_word(line)

    def get_write(self, line):
        return int(self.get_last_word(line))

    def get_move(self, line):
        return 1 if self.get_last_word(line) == 'right' else -1

    def get_last_word(self, line):
        return line.split()[-1][:-1]


if __name__ == '__main__':
    blueprint = Blueprint(get_input('input.txt'))
    print(blueprint.state)
    print(blueprint.steps)
    print(blueprint.debug_print())
    blueprint.run()
    print(blueprint.count_ones())
