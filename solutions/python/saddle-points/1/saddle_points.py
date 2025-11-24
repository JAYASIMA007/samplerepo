def saddle_points(matrix):
    if not matrix:
        return []

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise ValueError("irregular matrix")

    results = []

    for r, row in enumerate(matrix):
        max_in_row = max(row)

        for c, value in enumerate(row):

            if value != max_in_row:
                continue

            column_values = [matrix[i][c] for i in range(len(matrix))]
            min_in_col = min(column_values)

            if value == min_in_col:
                results.append({"row": r + 1, "column": c + 1})

    return results
