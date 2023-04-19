# Authors: Eduardo Nunez | Juan Gonzalez
# Authors emails: eduardonunez@csu.fullerton.edu | gonzalez.juanant524@csu.fullerton.edu 
import time
import random

# ============= SOCCEER ALGORITHM =============
def soccer_dyn_prog(F):
    r = len(F)
    c = len(F[0])

    if F[0][0] == 'X':
        return 0

    A = [[0] * c for _ in range(r)]
    A[0][0] = 1

    for i in range(r):
        for j in range(c):
            if F[i][j] == 'X':
                A[i][j] = 0
                continue
            above = A[i - 1][j] if i > 0 and F[i - 1][j] == '.' else 0
            left = A[i][j - 1] if j > 0 and F[i][j - 1] == '.' else 0

            A[i][j] += above + left

    return A[r - 1][c - 1]

# ============= RANDOM GRID =============
def create_random_grid(n):
    grid = [['.' for _ in range(n)] for _ in range(n)]  # Create an empty n x n grid filled with '.'

    for i in range(n):
        for j in range(n):
            if random.random() < 0.2:  # 20% chance to place 'X' in a cell
                grid[i][j] = 'X'

    grid[0][0] = '.'  # Ensure the starting point is not blocked
    grid[n-1][n-1] = '.'  # Ensure the end point is not blocked

    return grid

# ============= MAIN IMPLEMENTATION =============
def main():
    ns = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # Varying sizes of n
    timings = []

    for n in ns:
        grid = create_random_grid(n)

        start_time = time.time()
        num_paths = soccer_dyn_prog(grid)
        end_time = time.time()

        runtime = (end_time - start_time)  * 1000 # Calculate runtime in milliseconds
        timings.append(runtime)

        print(f"Size: {n}x{n}, Number of different paths: {num_paths}, Runtime: {runtime:.2f} ms")
        
    # ============= EXAMPLE INPUT IMPLEMENTATION =============
    #
    # TO RUN THIS CORRECTLY, COMMENT OUT ALL OTHER LINES IN THE MAIN FUNCTION & UNCOMMENT THE CODE BELOW SECTION
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
    
    # num_paths = soccer_dyn_prog(grid)
    # print("Number of different paths (exhaustive search):", num_paths)  # Output: 102

if __name__ == "__main__":
    main()