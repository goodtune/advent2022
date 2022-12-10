import sys


def series(lower, upper):
    return {x for x in range(lower, upper + 1)}


total = 0

for line in sys.stdin:
    a, b = [series(*[int(n) for n in p.split("-")]) for p in line.split(",")]
    if not b.difference(a) or not a.difference(b):
        total += 1

print(total)
