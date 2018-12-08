#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Tree:
    def __init__(self, data, start=0):
        self.children, self.meta = self.parse_node(data, start)

    def parse_node(self, data, start):
        num_children = data[start]
        num_metas = data[start + 1]

        children = []
        meta = []

        start += 2

        if num_children > 0:
            for _ in range(num_children):
                new_child = Tree(data, start)
                start += len(new_child)
                children.append(new_child)

        if num_metas > 0:
            end = start + num_metas
            meta = data[start: end]

        return children, meta

    def __len__(self):
        return sum(len(child) for child in self.children) + len(self.meta) + 2
