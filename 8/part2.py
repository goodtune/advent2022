import sys

grid = []
for line in sys.stdin:
    grid.append([int(t) for t in line[:-1]])

cols, rows = len(grid[0]), len(grid)


def scenic(trees, height):
    score = 0
    for t in trees:
        if t >= height:
            score += 1
            break
        else:
            score += 1
    return score


prime = 0

for row in range(1, rows - 1):
    for col in range(1, cols - 1):
        t = grid[row][col]
        left = scenic(grid[row][col - 1 :: -1], t)
        right = scenic(grid[row][col + 1 :], t)
        up = scenic([grid[r][col] for r in range(row - 1, -1, -1)], t)
        down = scenic([grid[r][col] for r in range(row + 1, rows)], t)
        score = left * right * up * down
        if score > prime:
            prime = score

print(prime)
