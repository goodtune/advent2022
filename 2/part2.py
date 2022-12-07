import sys
from functools import total_ordering


@total_ordering
class RPS:
    score = 0

    def __lt__(self, other):
        return NotImplemented

    def __eq__(self, other):
        return self.score == other.score

    def win(self):
        return NotImplemented

    def lose(self):
        return NotImplemented


class Rock(RPS):
    score = 1

    def __lt__(self, other):
        """Paper (2) defeats Rock"""
        return other.score == 2

    def win(self):
        return Paper()

    def lose(self):
        return Scissors()


class Paper(RPS):
    score = 2

    def __lt__(self, other):
        """Scissors (3) defeats Paper"""
        return other.score == 3

    def win(self):
        return Scissors()

    def lose(self):
        return Rock()


class Scissors(RPS):
    score = 3

    def __lt__(self, other):
        """Rock (1) defeats Scissors"""
        return other.score == 1

    def win(self):
        return Rock()

    def lose(self):
        return Paper()


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
