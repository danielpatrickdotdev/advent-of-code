#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Tree:
    def __init__(self, data, start=0):
        self.children, self.meta, self._length = self.parse_node(data, start)

    def parse_node(self, data, start):
        length = -start

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
        else:
            end = start

        length += end

        return children, meta, length

    def __len__(self):
        return self._length
