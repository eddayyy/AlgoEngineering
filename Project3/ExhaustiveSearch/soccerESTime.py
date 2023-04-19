# Authors: Eduardo Nunez | Juan Gonzalez
# Authors emails: eduardonunez@csu.fullerton.edu | gonzalez.juanant524@csu.fullerton.edu 
import random
import time

# ============= SOCCEER ALGORITHM =============
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


# ============= RANDOM GRID =============
def create_random_grid(n):
    grid = [['.' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if random.random() < 0.2:  # 20% chance to place 'X' in a cell
                grid[i][j] = 'X'

    grid[0][0] = '.'  # Ensure the starting point is not blocked
    grid[n-1][n-1] = '.'  # Ensure the end point is not blocked

    return grid

# ============= MAIN IMPLEMENTATION =============
def main():
    ns = [2, 4, 5, 6, 7, 8, 9, 10] # Varying sizes of n
    timings = []

    for n in ns:
        grid = create_random_grid(n)

        start_time = time.time()
        num_paths = count_paths_exhaustive(grid)
        end_time = time.time()

        runtime = (end_time - start_time) * 1000 # Calculate runtime in milliseconds
        timings.append(runtime)

        print(f"Size: {n}x{n}, Number of different paths: {num_paths}, Runtime: {runtime:.2f} ms")

    # ============= EXAMPLE INPUT IMPLEMENTATION =============
    #
    # TO RUN THIS CORRECTLY, COMMENT OUT ALL OTHER LINES IN THE MAIN FUNCTION & UNCOMMENT THIS SECTION
    #
    # grid = [
    #     ['.', '.', '.', '.', '.', '.', 'X', '.', 'X'],
    #     ['X', '.', '.', '.', '.', '.', '.', '.', '.'],
    #     ['.', '.', '.', 'X', '.', '.', '.', 'X', '.'],
    #     ['.', '.', 'X', '.', '.', '.', '.', 'X', '.'],
    #     ['.', 'X', '.', '.', '.', '.', 'X', '.', '.'],
    #     ['.', '.', '.', '.', 'X', '.', '.', '.', '.'],
    #     ['.', '.', 'X', '.', '.', '.', '.', '.', 'X'],
    #     ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    # ]
    # num_paths = count_paths_exhaustive(grid)
    # print("Number of different paths (exhaustive search):", num_paths)  # Output: 102


if __name__ == "__main__":
    main()
