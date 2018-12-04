#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


parser = re.compile("^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)\n")


class Matrix:
    def __init__(self, size):
        self._state = [["."] * size for _ in range(size)]

    def add_box(self, x, y, w, h):
        for yg in range(y, y + h):
            for xg in range(x, x + w):
                self._state[yg][xg] = "#"
        return self

    def render(self):
        for row in self._state:
            for cell in row:
                print(cell, end="")
            print("")
        return self

    @property
    def size(self):
        return max(len(row) for row in self._state)

    def __getitem__(self, item):
        return self._state[item]


class Cube:
    def __init__(self):
        self._stack = []
        self._size = 0

    def add_matrix(self, matrix: Matrix):
        self._stack.append(matrix)
        self._size = max(self._size, matrix.size)
        return self

    @property
    def size(self):
        return (self._size, self._size, len(self._stack))

    def render(self):
        for layer in self._stack:
            layer.render()
        return self

    def get_intersections(self):
        w, h, l = self.size
        stack = self._stack
        intersections = []
        for x in range(w):
            for y in range(h):
                found = set()
                for z in range(l):
                    layer = stack[z]
                    if layer[y][x] == "#":
                        found.add(z)
                if len(found) > 1:
                    intersections.append(found)
        return intersections


with open("input") as fd:
    cube = Cube()
    for line in fd:
        _, x, y, w, h = (int(num) for num in parser.match(line).groups())
        cube.add_matrix(Matrix(1000).add_box(x, y, w, h))
    results = [item for item in cube.get_intersections() if len(item) > 1]
    print(len(results))
