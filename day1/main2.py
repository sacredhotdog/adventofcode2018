#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

with open("input") as fd:
    seen = set()
    state = 0
    while True:
        for line in fd:
            num = int(line.strip())
            state += num
            if state in seen:
                print(state)
                sys.exit(0)
            else:
                seen.add(state)
        fd.seek(0)
