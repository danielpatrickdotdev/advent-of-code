#!/usr/bin/env python3

import string


def get_input(path):
    with open(path) as infile:
        return [tuple([int(n) for n in line.split('/')]
                                ) for line in infile.read().split('\n')]


class BridgeComponent:
    LEFT = 1
    RIGHT = 2

    def __init__(self, a, b, a_attached=None, b_attached=None):
        self.a = a
        self.b = b
        self.a_attached = a_attached
        self.b_attached = b_attached

    def get_unattached(self):
        if self.a_attached is None and self.b_attached is None:
            raise Exception
        elif self.a_attached is None:
            return self.a
        elif self.b_attached is None:
            return self.b
        else:
            return None

    def copy(self):
        return BridgeComponent(self.a, self.b, self.a_attached, self.b_attached)

    def attach_left(self, n):
        if self.a_attached is None and self.a == n:
            self.a_attached = self.LEFT
        elif self.b_attached is None and self.b == n:
            self.b_attached = self.LEFT
        else:
            raise Exception

    def detach_left(self):
        if self.a_attached == self.LEFT:
            self.a_attached = None
        elif self.b_attached == self.LEFT:
            self.b_attached = None
        else:
            raise Exception

    def attach_right(self, n):
        if self.a_attached is None and self.a == n:
            self.a_attached = self.RIGHT
        elif self.b_attached is None and self.b == n:
            self.b_attached = self.RIGHT
        else:
            raise Exception

    def detach_right(self):
        if self.a_attached == self.RIGHT:
            self.a_attached = None
        elif self.b_attached == self.RIGHT:
            self.b_attached = None
        else:
            raise Exception

    def a_is_spare(self, n):
        return self.a == n and self.a_attached is None

    def b_is_spare(self, n):
        return self.b == n and self.b_attached is None

    def has_spare(self, n):
        return self.a_is_spare(n) or self.b_is_spare(n)

    def _repr_helper(self, value, is_attached):
        if is_attached:
            return "[{}]".format(value)
        else:
            return "({})".format(value)

    def __repr__(self):
        rep = ""
        if self.b_attached is self.LEFT:
            rep += self._repr_helper(self.b, True)
            rep += self._repr_helper(self.a, self.a_attached is not None)
        else:
            rep += self._repr_helper(self.a, self.a_attached is not None)
            rep += self._repr_helper(self.b, self.b_attached is not None)
        return rep

    def __eq__(self, other):
        return ((self.a + self.b) == (other.a + other.b))

    def __ne__(self, other):
        return ((self.a + self.b) != (other.a + other.b))

    def __lt__(self, other):
        return ((self.a + self.b) < (other.a + other.b))

    def __le__(self, other):
        return ((self.a + self.b) <= (other.a + other.b))

    def __gt__(self, other):
        return ((self.a + self.b) > (other.a + other.b))

    def __ge__(self, other):
        return ((self.a + self.b) >= (other.a + other.b))


class BridgeComponents:

    def __init__(self, data):
        self._components = [BridgeComponent(*c) for c in data]

    def locate(self, n):
        return [c for c in self._components if c.has_spare(n)]

    def locate_best(self, n):
        return max(self.locate(n))

    def __repr__(self):
        return '-'.join([str(c) for c in self._components])


class Bridge:

    def __init__(self, components=None):
        self._components = components or []

    def append(self, component):
        self._components.append(component)

    def pop(self):
        self._components.pop()

    def score(self):
        return sum([c.a + c.b for c in self._components])

    def copy(self):
        return Bridge([c.copy() for c in self._components])

    @property
    def last(self):
        return self._components[-1]

    def __len__(self):
        return len(self._components)

    def __repr__(self):
        return '='.join([str(c) for c in self._components])


class BridgeBuilder:

    def __init__(self, components):
        self._components = components
        self._bridges = None

    def get_longest_bridge(self):
        if self._bridges is None:
            self._bridges = self.make_bridges()
        longest_length = None
        bridges = []
        for bridge in self._bridges:
            length = len(bridge)
            if not bridges:
                longest_length = length
            if length > longest_length:
                longest_length = length
                bridges = [bridge]
            elif length == longest_length:
                bridges.append(bridge)

        return self.get_highest_score_and_bridge(bridges)

    def make_bridges(self):
        bridges = []
        self.extend(bridges, Bridge(), 0)
        self._bridges = bridges[:]
        return bridges

    def extend(self, bridges, bridge, next_n):
        if bridge:
            bridge.last.attach_right(next_n)
        options = self._components.locate(next_n)
        if not options:
            bridges.append(bridge.copy())
        for component in options:
            bridge.append(component)
            component.attach_left(next_n)
            self.extend(bridges, bridge, component.get_unattached())
            component.detach_left()
            bridge.pop()
        if bridge:
            bridge.last.detach_right()

    def get_highest_scoring_bridge(self):
        if self._bridges is None:
            self._bridges = self.make_bridges()
        return self.get_highest_score_and_bridge(self._bridges)

    def get_highest_score_and_bridge(self, bridges):
        best_score = None
        best_bridge = None
        for bridge in bridges:
            score = bridge.score()
            if best_score is None or score > best_score:
                best_score = score
                best_bridge = bridge
        return (best_score, best_bridge)

    @property
    def components(self):
        return self._components

    @property
    def bridge(self):
        return self._bridge.copy()



if __name__ == '__main__':
    components = BridgeComponents(get_input("input.txt"))
    b = BridgeBuilder(components)
    print("Finding highest scoring bridge")
    score, bridge = b.get_highest_scoring_bridge()
    print(bridge)
    print("Score:", score)
    print("Finding longest bridge")
    score, bridge = b.get_longest_bridge()
    print(bridge)
    print("Score:", score)
