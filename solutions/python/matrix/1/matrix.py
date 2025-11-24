class Matrix:
    def __init__(self, matrix_string):
        self.rows = []
        for line in matrix_string.split("\n"):
            numbers = [int(n) for n in line.split()]
            self.rows.append(numbers)

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        col_index = index - 1

        return [row[col_index] for row in self.rows]
