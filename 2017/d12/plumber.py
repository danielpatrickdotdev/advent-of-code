#!/usr/bin/env python3


def get_input(path):
    with open(path) as infile:
        return [line.rstrip('\n') for line in infile]


class Plumber:

    def __init__(self, pipes_text):
        self.pipes = {}
        for pipe_text in pipes_text:
            pipe_from, pipe_to = pipe_text.split('<->')
            self.pipes[int(pipe_from)] = [int(p) for p in pipe_to.split(',')]

    def count_network(self, program_id):
        return len(self.get_network(program_id, []))

    def get_network(self, program_id, acc):
        if program_id in acc:
            return acc
        else:
            acc.append(program_id)

        for p in self.pipes[program_id]:
            self.get_network(p, acc)

        return acc

    def count_groups(self):
        group_count = 0
        programs_left = set(self.pipes.keys())
        while programs_left:
            program_id = programs_left.pop()
            network = self.get_network(program_id, [])
            programs_left -= set(network)
            group_count += 1

        return group_count


if __name__ == '__main__':
    pipes_text = get_input("input.txt")
    plumber = Plumber(pipes_text)
    print("0 is connected to", plumber.count_network(0), "programs")
    print("There are", plumber.count_groups(), "groups")
