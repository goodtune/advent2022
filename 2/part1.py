import sys
from functools import total_ordering


@total_ordering
class RPS:
    __lt__ = lambda self, other: NotImplemented
    __eq__ = lambda self, other: isinstance(other, self.__class__)

class Rock(RPS):
    score = 1
    __lt__ = lambda self, other: isinstance(other, Paper)


class Paper(RPS):
    score = 2
    __lt__ = lambda self, other: isinstance(other, Scissors)


class Scissors(RPS):
    score = 3
    __lt__ = lambda self, other: isinstance(other, Rock)


translate = {
    "A": Rock(), "X": Rock(),
    "B": Paper(), "Y": Paper(),
    "C": Scissors(), "Z": Scissors(),
}

score = 0

for line in sys.stdin:
    opponent, me = (translate[l] for l in line.split())
    score += me.score
    if me > opponent:
        score += 6  # for the win
    elif me == opponent:
        score += 3  # for the draw

print(score)
