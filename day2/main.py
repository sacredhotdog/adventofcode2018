#!/usr/bin/env python

from collections import Counter


class SummableDict(dict):
    def __iadd__(self, other):
        for key, value in other.items():
            if key in self:
                self[key] += value
            else:
                self[key] = value
        return self


with open("input") as fd:
    seen = SummableDict()
    for line in fd:
        uid = line.strip()
        counts = {k: 1 for k in Counter(uid).values()}
        seen += counts
    print(seen[2] * seen[3])
