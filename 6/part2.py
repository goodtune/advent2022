import sys

for line in sys.stdin:
    pos = 0
    while len(set(line[pos : pos + 14])) < 14:
        pos += 1
    print(pos + 14)
