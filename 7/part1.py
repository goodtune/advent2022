import pathlib
import re
import sys

files = {}
cwd = pathlib.Path("/")

for line in sys.stdin:
    if line.startswith("$ cd"):
        cwd = (cwd / line[5:-1]).resolve()
        continue
    f = re.match(r"^(\d+) (.+)", line)
    if f:
        size, filename = f.groups()
        for p in (cwd / filename).parents:
            files.setdefault(p, []).append(size)

total = 0

for path in sorted(files):
    size = sum([int(s) for s in files[path]])
    if size <= 100000:
        total += size

print(total)
