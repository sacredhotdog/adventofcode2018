#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string as S
import math


_ns = dict(zip(S.ascii_lowercase, S.ascii_uppercase))
_ns2 = dict(zip(S.ascii_uppercase, S.ascii_lowercase))
_ns.update(_ns2)

with open("input") as fd:
    line = fd.readline().strip()
    best = math.inf
    for a, b in _ns2.items():
        curline = line.replace(a, "")
        curline = list(curline.replace(b, ""))
        idx = 0
        try_again = True
        while try_again:
            try_again = False
            while True:
                try:
                    ch1, ch2 = curline[idx], curline[idx+1]
                except IndexError:
                    break
                else:
                    if ch2 == _ns[ch1] or ch1 == _ns[ch2]:
                        del(curline[idx])
                        del(curline[idx])
                        try_again = True
                    idx += 1
            idx = 0
        best = min(best, len(curline))

print(best)
