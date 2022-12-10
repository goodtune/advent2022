import sys
import re

stacks = {}

for line in sys.stdin:
    if not line[:-1]:
        break
    crates = line[1::4]
    for stack, crate in enumerate(crates, 1):
        if re.search(r"[ \d]", crate):
            continue
        stacks.setdefault(stack, []).insert(0, crate)


for line in sys.stdin:
    n, source, dest = [int(d) for d in re.findall(r"\d+", line)]
    stacks[dest] += stacks[source][-n:]
    stacks[source] = stacks[source][:-n]


print("".join([stacks[i][-1] for i in sorted(stacks)]))
