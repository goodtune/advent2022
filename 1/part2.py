import sys
from collections import defaultdict

elf = 1
table = defaultdict(lambda: 0)

for line in sys.stdin:
    try:
        calories = int(line)
        table[elf] += calories
    except ValueError:
        elf += 1

print(sum(sorted(table.values())[-3:]))
