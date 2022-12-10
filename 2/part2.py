import sys
from functools import total_ordering


@total_ordering
class RPS:
    __lt__ = lambda self, other: NotImplemented
    __eq__ = lambda self, other: isinstance(other, self.__class__)
    win = lambda self: NotImplemented
    lose = lambda self: NotImplemented

class Rock(RPS):
    score = 1
    __lt__ = lambda self, other: isinstance(other, Paper)
    win = lambda self: Paper()
    lose = lambda self: Scissors()


class Paper(RPS):
    score = 2
    __lt__ = lambda self, other: isinstance(other, Scissors)
    win = lambda self: Scissors()
    lose = lambda self: Rock()


class Scissors(RPS):
    score = 3
    __lt__ = lambda self, other: isinstance(other, Rock)
    win = lambda self: Rock()
    lose = lambda self: Paper()


translate = {
    "A": Rock(),
    "B": Paper(),
    "C": Scissors(),
    "X": lambda o: o.lose(),
    "Y": lambda o: o,
    "Z": lambda o: o.win(),
}

score = 0

for line in sys.stdin:
    parts = line.split()
    opponent = translate[parts[0]]
    me = translate[parts[1]](opponent)
    score += me.score
    if me > opponent:
        score += 6  # for the win
    elif me == opponent:
        score += 3  # for the draw

print(score)
