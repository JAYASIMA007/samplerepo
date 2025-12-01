class Matrix:
    def __init__(self, matrix_string):
        self.rows = [
            [int(n) for n in line.split()]
            for line in matrix_string.split("\n")
        ]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        col_index = index - 1
        return [row[col_index] for row in self.rows]
