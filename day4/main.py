#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import datetime as dt
from collections import namedtuple, defaultdict, Counter


parser1 = re.compile("^\[(\d+)\-(\d+)\-(\d+)\ (\d+):(\d+)] ([\w #]+)$")

Entry = namedtuple(
    "Entry", ("year", "month", "day", "hour", "minute", "action")
)


class Entry:
    action_parser = re.compile("^Guard #(\d+) begins shift$")

    def __init__(self, year, month, day, hour, minute, action):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.hour = int(hour)
        self.minute = int(minute)
        self.action = action

    def as_dt(self):
        return dt.datetime(
            self.year, self.month, self.day, self.hour, self.minute
        )

    def __lt__(self, other):
        return self.as_dt() < other.as_dt()

    def __sub__(self, other):
        return self.as_dt() - other.as_dt()

    @property
    def guard_id(self):
        try:
            return int(self.action_parser.match(self.action).groups()[0])
        except (AttributeError, ValueError):
            pass


class GuardLog:
    def __init__(self):
        self._state = defaultdict(list)

    def add(self, guard_id, start, end):
        self._state[guard_id].append((start, end))

    def get_top_sleeper(self):
        top_guard = None
        top_sleep = 0
        for guard, times in self._state.items():
            sleep = sum((rec[1] - rec[0]).seconds for rec in times)
            if sleep > top_sleep:
                top_guard = guard
                top_sleep = sleep

        return (top_guard, top_sleep)

    def get_best_minute(self, guard_id):
        c = Counter()
        for start, end in self._state[guard_id]:
            c.update(range(start.minute, end.minute))
        return c.most_common()[0][0]

    def __getitem__(self, item):
        return self._state[item]


with open("input") as fd:
    entries = sorted([Entry(*parser1.match(ln.strip()).groups()) for ln in fd])
    log = GuardLog()
    current_guard = None
    sleep_start = None
    for entry in entries:
        if entry.action == "falls asleep":
            sleep_start = entry
        elif entry.action == "wakes up":
            log.add(current_guard, sleep_start, entry)
        else:
            current_guard = entry.guard_id
    uid, _ = log.get_top_sleeper()
    minute = log.get_best_minute(uid)
    print(uid * minute)
