import sys


def series(lower, upper):
    return {x for x in range(lower, upper + 1)}


total = 0

for line in sys.stdin:
    a, b = [series(*[int(n) for n in p.split("-")]) for p in line.split(",")]
    if b.intersection(a):
        total += 1

print(total)
