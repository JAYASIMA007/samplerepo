def convert(input_grid):
    # Normalize input to list of lines
    if isinstance(input_grid, str):
        lines = input_grid.splitlines()
    else:
        lines = input_grid

    # Validate number of rows
    if len(lines) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    # Validate number of columns
    for line in lines:
        if len(line) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

    digits_map = {
        " _ "
        "| |"
        "|_|"
        "   ": "0",

        "   "
        "  |"
        "  |"
        "   ": "1",

        " _ "
        " _|"
        "|_ "
        "   ": "2",

        " _ "
        " _|"
        " _|"
        "   ": "3",

        "   "
        "|_|"
        "  |"
        "   ": "4",

        " _ "
        "|_ "
        " _|"
        "   ": "5",

        " _ "
        "|_ "
        "|_|"
        "   ": "6",

        " _ "
        "  |"
        "  |"
        "   ": "7",

        " _ "
        "|_|"
        "|_|"
        "   ": "8",

        " _ "
        "|_|"
        " _|"
        "   ": "9",
    }

    output = []

    for row in range(0, len(lines), 4):
        block = lines[row:row + 4]
        digits = []

        for col in range(len(block[0]) // 3):
            pattern = "".join(
                line[col * 3:(col + 1) * 3] for line in block
            )
            digits.append(digits_map.get(pattern, "?"))

        output.append("".join(digits))

    return ",".join(output)
