#!/usr/bin/env python3

class BaseDisc:
    def __init__(self, name, weight, programs):
        self._name = name
        self._weight = weight
        self._programs = programs

    @property
    def name(self):
        return self._name

    def __repr__(self):
        text = "Disc {} ({})".format(self._name, self._weight)
        if self.num_programs:
            text += " -> " + ", ".join(self._programs)
        return text


class Disc(BaseDisc):
    @property
    def num_programs(self):
        return len(self._programs)

    def has_program(self, prog):
        return prog in self._programs

    def set_programs(self, discs):
        self._programs = {p: discs[p] for p in self._programs}


class DiscNode:
    def __init__(self, disc, parent, discs):
        self._disc = disc
        self._parent = parent
        self._weight = disc._weight
        self._name = disc._name
        self._children = {}
        self.init_children(disc._programs, discs)


    def init_children(self, programs, discs):
        for disc_name in programs:
            disc = discs.get(disc_name)
            self._children[disc_name] = DiscNode(disc, self, discs)

    @property
    def parent(self):
        return self._parent

    @property
    def children(self):
        return self._children.values()

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    def __repr__(self):
        return repr(self._disc)


class DiscSet:
    def __init__(self):
        self._list = {}

    def get(self, disc_name):
        return self._list[disc_name]

    def add(self, disc):
        self._list[disc.name] = disc

    def get_all(self):
        return self._list.values()

    def get_base(self):
        disc = next(iter(self._list.values()))
        found_base = False

        while not found_base:
            found_base = True
            for d in self._list.values():
                if d.has_program(disc.name):
                    disc = d
                    found_base = False
                    break
        return disc


def import_input(path):
    discs = DiscSet()
    with open(path, encoding='utf-8') as infile:
        for line in infile:
            disc_info = line.split()
            key = disc_info[0]
            weight = int(disc_info[1].strip("()"))
            programs = []
            if len(disc_info) > 2:
                for i in range(3, len(disc_info)):
                    programs.append(disc_info[i].strip(","))

            discs.add(Disc(key, weight, programs))

    return discs


def create_tree():
    discs = import_input("input.txt")
    root_disc = discs.get_base()
    root_node = DiscNode(root_disc, None, discs)

    return root_node


def find_odd_one_out(numbers):
    if len(set(numbers)) == 1 or len(numbers) <=2:
        return None
    first = numbers.pop()
    numbers = set(numbers)
    try:
        numbers.remove(first)
    except:
        return first
    else:
        return numbers.pop()


def tower_weight(disc):
    return disc.weight + sum([tower_weight(d) for d in disc.children])


def find_problem(disc):
    children = list(disc.children)
    if not children:
        return disc
    weights = [tower_weight(d) for d in children]
    odd_weight = find_odd_one_out(weights.copy())
    if not odd_weight:
        return disc
    odd_disc = children[weights.index(odd_weight)]
    return find_problem(odd_disc) or disc


root = create_tree()
print(root)
print("Solution 1:", root.name)

problem = find_problem(root)
for disc in problem.parent.children:
    print(tower_weight(disc), disc)


def get_diff(problem):
    correct_tower_weight = 0
    for disc in problem.parent.children:
        dtw = tower_weight(disc)
        ptw = tower_weight(problem)

        if dtw != ptw:
            correct_tower_weight = dtw
            break

    return dtw - ptw

diff = get_diff(problem)
print(diff)
print(problem.weight)
print("Solution 2:", problem.weight + diff)
