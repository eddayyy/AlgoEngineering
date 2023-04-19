def is_valid(candidate, field):
    rows, cols = len(field), len(field[0])
    row, col = 0, 0

    for move in candidate:
        if move == 'R':
            col += 1
        else:
            row += 1

        if row >= rows or col >= cols or field[row][col] == 'X':
            return False

    return row == rows - 1 and col == cols - 1


def count_paths_exhaustive(field):
    rows, cols = len(field), len(field[0])
    path_length = rows + cols - 2
    counter = 0

    for bits in range(0, 2 ** path_length):
        candidate = []
        for k in range(path_length):
            bit = (bits >> k) & 1
            if bit == 1:
                candidate.append('R')
            else:
                candidate.append('D')

        if is_valid(candidate, field):
            counter += 1

    return counter


def main():
    grid = [
        ['.', '.', '.', '.', '.', '.', 'X', '.', 'X'],
        ['X', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', 'X', '.', '.', '.', 'X', '.'],
        ['.', '.', 'X', '.', '.', '.', '.', 'X', '.'],
        ['.', 'X', '.', '.', '.', '.', 'X', '.', '.'],
        ['.', '.', '.', '.', 'X', '.', '.', '.', '.'],
        ['.', '.', 'X', '.', '.', '.', '.', '.', 'X'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    ]

    num_paths = count_paths_exhaustive(grid)
    print("\nNumber of different paths (exhaustive search):", num_paths)  # Output: 102


if __name__ == "__main__":
    main()
