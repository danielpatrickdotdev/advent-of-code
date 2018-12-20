#!/usr/bin/env python
# -*- coding: utf-8 -*-


from operator import itemgetter


class Node:
    directions = {
        "N": (0, -1),
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0),
    }

    def __init__(self, x=0, y=0, distance=0):
        self.x = x
        self.y = y
        self.distance = distance
        self.children = []

        if x == y == distance == 0:
            self.directory = {
                (0, 0): self,
            }

    def update_distance(self, n):
        if self.distance > n:
            for child in self.children:
                child.update_distance(n + 1)

        self.distance = min(self.distance, n)

    def add_child(self, child_node):
        self.children.append(child_node)

    def create_child(self, x, y):
        if (x, y) in self.directory:
            child_node = self.directory[(x, y)]
            child_node.update_distance(self.distance + 1)
        else:
            child_node = Node(x, y, self.distance + 1)
            self.directory[(x, y)] = child_node
            child_node.directory = self.directory

        self.add_child(child_node)
        return child_node

    @property
    def location(self):
        return (self.x, self.y)

    def __str__(self):
        return "{}, {}".format(self.x, self.y)


class FacilityMap:
    def __init__(self, path_regex="^$"):
        self.instructions = self.parse(path_regex)
        if self.instructions:
            self.create_tree()
            self.create_grid()

    def parse(self, path_regex, start=1):
        path = []

        while start < len(path_regex) and path_regex[start] not in ")$":
            if path_regex[start] == "(":
                subpath, start = self.parse(path_regex, start + 1)
                path.append(subpath)
            elif path_regex[start] in "NSEW|":
                path.append(path_regex[start])

            start += 1

        if path_regex[start] == "$":
            return path
        else:
            return (path, start)

    def _translate(self, x, y, d):
        dx, dy = Node.directions[d]
        return (x + dx, y + dy)

    def parse_node(self, node, instructions):
        parent_node = node

        for i in instructions:
            if type(i) is list:
                self.parse_node(node, i)
            elif i in "NSEW":
                x, y = self._translate(*node.location, i)
                node = node.create_child(x, y)
            else:
                node = parent_node

    def create_tree(self):
        self.tree = Node()
        self.parse_node(self.tree, self.instructions)

    def create_grid(self):
        coords = sorted(self.tree.directory.keys(), key=itemgetter(0, 1))
        min_x = coords[0][0]
        max_x = coords[-1][0]

        coords = sorted(self.tree.directory.keys(), key=itemgetter(1, 0))
        min_y = coords[0][1]
        max_y = coords[-1][1]

        width = (max_x - min_x + 1) * 2 + 1
        height = (max_y - min_y + 1) * 2 + 1

        self.grid = [["#" for y in range(height)] for x in range(width)]

        def get_xy(coord):
            return (
                (coord[0] - min_x) * 2 + 1,
                (coord[1] - min_y) * 2 + 1
            )

        def get_door_xy(x1, y1, x2, y2):
            return ((x1 + x2) // 2, (y1 + y2) // 2)

        for coord in coords:
            node = self.tree.directory[coord]
            x, y = get_xy(coord)

            if self.grid[x][y] == "#":
                self.grid[x][y] = "."

            for child in node.children:
                x1, y1 = get_door_xy(x, y, *get_xy(child.location))

                if x1 == x:
                    self.grid[x1][y1] = "—"
                else:
                    self.grid[x1][y1] = "|"

        # Place X at origin
        x, y = get_xy(self.tree.location)
        self.grid[x][y] = "X"

    def __str__(self):
        return "\n".join(
            "".join(
                str(self.grid[x][y]) for x in range(len(self.grid))
            ) for y in range(len(self.grid[0]))
        )
