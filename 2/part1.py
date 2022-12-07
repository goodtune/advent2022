import sys
from functools import total_ordering


@total_ordering
class RPS:
    score = 0

    def __lt__(self, other):
        return NotImplemented

    def __eq__(self, other):
        return self.score == other.score


class Rock(RPS):
    score = 1

    def __lt__(self, other):
        """Paper (2) defeats Rock"""
        return other.score == 2


class Paper(RPS):
    score = 2

    def __lt__(self, other):
        """Scissors (3) defeats Paper"""
        return other.score == 3


class Scissors(RPS):
    score = 3

    def __lt__(self, other):
        """Rock (1) defeats Scissors"""
        return other.score == 1


translate = {
    "A": Rock(),
    "X": Rock(),
    "B": Paper(),
    "Y": Paper(),
    "C": Scissors(),
    "Z": Scissors(),
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
