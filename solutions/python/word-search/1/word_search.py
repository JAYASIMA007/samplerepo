class Point:
    def __init__(self, x, y):
        self.x = None
        self.y = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    # Directions: right, left, down, up, diagonals
    DIRECTIONS = [
        (1, 0),   # right
        (-1, 0),  # left
        (0, 1),   # down
        (0, -1),  # up
        (1, 1),   # diag down-right
        (1, -1),  # diag up-right
        (-1, 1),  # diag down-left
        (-1, -1)  # diag up-left
    ]

    def __init__(self, puzzle):
        self.grid = puzzle
        self.height = len(puzzle)
        self.width = len(puzzle[0]) if self.height else 0

    def search(self, word):
        wlen = len(word)

        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] != word[0]:
                    continue

                # Try all directions
                for dx, dy in self.DIRECTIONS:
                    nx, ny = x, y
                    match = True

                    for i in range(wlen):
                        if not (0 <= nx < self.width and 0 <= ny < self.height):
                            match = False
                            break
                        if self.grid[ny][nx] != word[i]:
                            match = False
                            break

                        nx += dx
                        ny += dy

                    if match:
                        start = Point(x, y)
                        end = Point(x + dx * (wlen - 1), y + dy * (wlen - 1))
                        return start, end

        return None
