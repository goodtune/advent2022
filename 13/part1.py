import json
import sys
from itertools import zip_longest


def compare(left, right):
    """
    >>> compare([1,1,3,1,1],[1,1,5,1,1])
    True
    >>> compare([[1],[2,3,4]],[[1],4])
    True
    >>> compare([9],[[8,7,6]])
    False
    >>> compare([[4,4],4,4],[[4,4],4,4,4])
    True
    >>> compare([7,7,7,7],[7,7,7])
    False
    >>> compare([], [3])
    True
    >>> compare([[[]]],[[]])
    False
    >>> compare([1,[2,[3,[4,[5,6,7]]]],8,9],[1,[2,[3,[4,[5,6,0]]]],8,9])
    False
    """
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return
        return left < right
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, list):
        for lhs, rhs in zip_longest(left, right):
            if lhs is None:
                return True
            if rhs is None:
                return False
            result = compare(lhs, rhs)
            if result is not None:
                return result


class Group:
    def __init__(self, initial=None):
        self.lists = []
        if initial is not None:
            self.add(initial)

    def __repr__(self):
        return f"<Group: {self.lists!r}>"

    def add(self, line):
        if len(self.lists) >= 2:
            raise ValueError
        self.lists.append(json.loads(line))

    def __bool__(self):
        return compare(*self.lists)


class Processor:
    def __init__(self):
        self.groups = [Group()]

    def __repr__(self):
        return f"<Processor: {self.groups!r}>"

    def add(self, line):
        if not line:
            return
        try:
            self.groups[-1].add(line)
        except ValueError:
            self.groups.append(Group(line))


if __name__ == "__main__":
    p = Processor()

    for line in sys.stdin:
        p.add(line[:-1])

    print(sum([i for i, g in enumerate(p.groups, 1) if g]))
