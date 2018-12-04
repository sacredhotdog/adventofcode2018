from collections import namedtuple


class Result:
    def __init__(self):
        self.same = []
        self.different = []


def compare(uid1, uid2):
    assert len(uid1) == len(uid2)
    result = Result()
    for ch1, ch2 in zip(uid1, uid2):
        if ch1 == ch2:
            result.same += [(ch1)]
        else:
            result.different += [(ch1, ch2)]
    return result


with open("input") as fd:
    ids = [line.strip() for line in fd]
    for uid1 in ids:
        for uid2 in ids:
            result = compare(uid1, uid2)
            if len(result.different) == 1:
                print("".join(result.same))

