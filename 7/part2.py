import pathlib
import re
import sys

files = {}
root = cwd = pathlib.Path("/")

for line in sys.stdin:
    if line.startswith("$ cd"):
        cwd = (cwd / line[5:-1]).resolve()
        continue
    f = re.match(r"^(\d+) (.+)", line)
    if f:
        size, filename = f.groups()
        for p in (cwd / filename).parents:
            files.setdefault(p, []).append(size)

smallest = sum([int(s) for s in files[root]])
free = 70000000 - smallest
require = 30000000 - free

for path in sorted(files):
    size = sum([int(s) for s in files[path]])
    if size >= require and size < smallest:
        smallest = size

print(smallest)
