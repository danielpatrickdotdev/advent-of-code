#!/usr/bin/env python
# -*- coding: utf-8 -*-


from operator import itemgetter


class Node:
    def __init__(self, x=0, y=0, distance=0, root=False):
        self.x = x
        self.y = y
        self.distance = distance
        self.children = []

        if root:
            self.directory = {
                (0, 0): self,
            }

    def update_distance(self, n):
        if self.distance > n:
            self.distance = n
            for child in self.children:
                child.update_distance(n + 1)

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
    directions = {
        "N": (0, -1),
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0),
    }

    def __init__(self, path_regex="^$"):
        self.tree = Node(root=True)
        self.parse(self.tree, path_regex)

    def parse(self, node, path_regex, start=1):
        parent_node = node

        while path_regex[start] not in ")$":
            if path_regex[start] == "(":
                start = self.parse(node, path_regex, start + 1)
            elif path_regex[start] in "NSEW":
                x, y = self._translate(*node.location, path_regex[start])
                node = node.create_child(x, y)
            else:
                node = parent_node

            start += 1

        if path_regex[start] != "$":
            return start

    def _translate(self, x, y, d):
        dx, dy = self.directions[d]
        return (x + dx, y + dy)

    def get_farthest_room(self):
        return sorted(
            (node.distance for node in self.tree.directory.values()),
            reverse=True
        )[0]

    def get_rooms_n_doors_away(self, n):
        return sum(
            1 for node in self.tree.directory.values()
            if node.distance >= n
        )

    def __str__(self):
        # This monstrosity is basically only here to make the constructor easier
        # to test!
        if self.tree is not None:
            coords = sorted(self.tree.directory.keys())
            min_x = coords[0][0]
            max_x = coords[-1][0]

            coords = sorted(self.tree.directory.keys(), key=itemgetter(1))
            min_y = coords[0][1]
            max_y = coords[-1][1]

            width = (max_x - min_x + 1) * 2 + 1
            height = (max_y - min_y + 1) * 2 + 1

            grid = [["#" for y in range(height)] for x in range(width)]

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

                if grid[x][y] == "#":
                    grid[x][y] = "."

                for child in node.children:
                    x1, y1 = get_door_xy(x, y, *get_xy(child.location))

                    if x1 == x:
                        grid[x1][y1] = "—"
                    else:
                        grid[x1][y1] = "|"

            # Place X at origin
            x, y = get_xy(self.tree.location)
            grid[x][y] = "X"

        return "\n".join(
            "".join(
                str(grid[x][y]) for x in range(width)
            ) for y in range(height)
        )
