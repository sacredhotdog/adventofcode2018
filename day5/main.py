#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string as S


_ns = dict(zip(S.ascii_lowercase, S.ascii_uppercase))
_ns.update(zip(S.ascii_uppercase, S.ascii_lowercase))

with open("input") as fd:
    line = list(fd.readline().strip())
    idx = 0
    try_again = True
    while try_again:
        try_again = False
        while True:
            try:
                ch1, ch2 = line[idx], line[idx+1]
            except IndexError:
                break
            else:
                if ch2 == _ns[ch1] or ch1 == _ns[ch2]:
                    del(line[idx])
                    del(line[idx])
                    try_again = True
                idx += 1
        idx = 0

print(len(line))
