#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parse(input_data):
    depth_str = input_data[0].split()[1]

    x_str, y_str = input_data[1].split()[1].split(",")

    return (int(depth_str), int(x_str), int(y_str))

