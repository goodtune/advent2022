import string
import sys


def priority(l):
    if l in string.ascii_lowercase:
        return ord(l) - 96
    elif l in string.ascii_uppercase:
        return ord(l) - 38


total = 0

for line in sys.stdin:
    size = int(len(line) / 2)
    a, b = set(line[:size]), set(line[size:-1])
    common = a.intersection(b)
    p = priority(*common)
    total += p

print(total)
