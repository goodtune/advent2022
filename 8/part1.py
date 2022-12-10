import sys

grid = []
for line in sys.stdin:
    grid.append([int(t) for t in line[:-1]])

cols, rows = len(grid[0]), len(grid)
visible = len(grid[0]) + len(grid[-1]) + 2 * (len(grid) - 2)

for row in range(1, rows - 1):
    for col in range(1, cols - 1):
        t = grid[row][col]
        if t > max(grid[row][:col]):  # look left
            visible += 1
        elif t > max(grid[row][col + 1 :]):  # look right
            visible += 1
        elif t > max([grid[r][col] for r in range(row)]):  # look up
            visible += 1
        elif t > max([grid[r][col] for r in range(row + 1, rows)]):  # look down
            visible += 1

print(visible)
