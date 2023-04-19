# Authors: Eduardo Nunez | Juan Gonzalez
# Authors emails: eduardonunez@csu.fullerton.edu | gonzalez.juanant524@csu.fullerton.edu 
import random
import time

# ============= SOCCEER ALGORITHM O(n * 2^n) =============
# This function checks if a given candidate path is valid, given a field with obstacles
def is_valid(candidate, field):
    # Get the dimensions of the field
    rows, cols = len(field), len(field[0])
    # Set the starting row and column to (0, 0)
    row, col = 0, 0

    # Loop through each move in the candidate path
    for move in candidate:
        # Update the row and column based on the move
        if move == 'R':
            col += 1
        else:
            row += 1

        # Check if the candidate path goes out of bounds or hits an obstacle
        if row >= rows or col >= cols or field[row][col] == 'X':
            return False

    # Check if the candidate path reaches the bottom-right corner of the field
    return row == rows - 1 and col == cols - 1


# This function counts the number of valid paths from the top-left to bottom-right corner of the field,
# by generating all possible paths and checking their validity
def count_paths_exhaustive(field):
    # Get the dimensions of the field
    rows, cols = len(field), len(field[0])
    # Calculate the length of the path needed to traverse the field
    path_length = rows + cols - 2
    # Initialize a counter for the number of valid paths
    counter = 0

    # Loop through all possible binary strings of length path_length
    for bits in range(0, 2 ** path_length):
        candidate = []
        # Convert each binary digit to a move in the candidate path
        for k in range(path_length):
            bit = (bits >> k) & 1
            if bit == 1:
                candidate.append('R')
            else:
                candidate.append('D')

        # Check if the candidate path is valid, and increment the counter if it is
        if is_valid(candidate, field):
            counter += 1

    # Return the number of valid paths
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
