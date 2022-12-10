import sys

for line in sys.stdin:
    pos = 0
    while len(set(line[pos : pos + 4])) < 4:
        pos += 1
    print(pos + 4)
