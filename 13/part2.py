import json
import sys
from functools import total_ordering
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


@total_ordering
class Packet(list):
    def __lt__(self, other):
        return compare(self, other)

    def __eq__(self, other):
        return compare(self, other) is None


if __name__ == "__main__":
    packets = [Packet(json.loads(l)) for l in sys.stdin.readlines() if l[:-1]]
    packets += [Packet([[2]]), Packet([[6]])]
    packets.sort()
    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
