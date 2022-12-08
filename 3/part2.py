import string
import sys


def priority(l):
    if l in string.ascii_lowercase:
        return ord(l) - 96
    elif l in string.ascii_uppercase:
        return ord(l) - 38


class Group:
    def __init__(self, initial=None):
        self.rucksacks = []
        if initial is not None:
            self.add(initial)

    def __repr__(self):
        return f"<Group: {self.common()!r}>"

    def add(self, rucksack):
        if len(self.rucksacks) >= 3:
            raise ValueError
        self.rucksacks.append(set(rucksack))

    def common(self):
        return self.rucksacks[0].intersection(*self.rucksacks[1:])

    def priority(self):
        return priority(*self.common())


class Processor:
    def __init__(self):
        self.groups = [Group()]

    def __repr__(self):
        return f"<Processor: {self.groups!r}>"

    def add(self, rucksack):
        try:
            self.groups[-1].add(rucksack)
        except ValueError:
            self.groups.append(Group(rucksack))

    def priority(self):
        return sum([g.priority() for g in self.groups])


p = Processor()

for line in sys.stdin:
    p.add(line[:-1])

print(p.priority())
