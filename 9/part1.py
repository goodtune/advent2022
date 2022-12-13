import sys


class Grid:
    def __init__(self):
        self.rows = [
            ["s"],
        ]
        self.head_x = 0
        self.head_y = 0
        self.tail_x = 0
        self.tail_y = 0

    def __str__(self):
        return "\n".join(["".join(row) for row in self.rows])

    def move(self, direction, distance):
        for _ in range(int(distance)):
            getattr(self, direction.lower())()
            if self.rows[self.tail_y][self.tail_x] == ".":
                self.rows[self.tail_y][self.tail_x] = "#"

    def tail_visited(self):
        res = 0
        for row in self.rows:
            for cell in row:
                if cell != ".":
                    res += 1
        return res

    def u(self):
        if self.head_y == 0:
            row = ["."] * len(self.rows[0])
            self.rows.insert(0, row)
            self.tail_y += 1
        else:
            self.head_y -= 1
        if self.tail_y - self.head_y > 1:
            self.tail_y -= 1
            self.tail_x = self.head_x

    def d(self):
        if self.head_y > self.tail_y:
            self.tail_y += 1
            self.tail_x = self.head_x
        self.head_y += 1
        if self.head_y >= len(self.rows):
            row = ["."] * len(self.rows[-1])
            self.rows.append(row)

    def l(self):
        if self.head_x == 0:
            for row in self.rows:
                row.insert(0, ".")
            self.tail_x += 1
        else:
            self.head_x -= 1
        if self.tail_x - self.head_x > 1:
            self.tail_x -= 1
            self.tail_y = self.head_y

    def r(self):
        if self.head_x > self.tail_x:
            self.tail_x += 1
            self.tail_y = self.head_y
        self.head_x += 1
        if self.head_x >= len(self.rows[self.head_y]):
            for row in self.rows:
                row.append(".")


g = Grid()

for line in sys.stdin:
    g.move(*line.split())

print(g.tail_visited())
