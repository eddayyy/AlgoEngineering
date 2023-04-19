# Authors: Eduardo Nunez | Juan Gonzalez
# Authors emails: eduardonunez@csu.fullerton.edu | gonzalez.juanant524@csu.fullerton.edu 
import time
import random

# ============= SOCCEER ALGORITHM O(n^2) =============
def soccer_dyn_prog(F):
    # Get the number of rows and columns in the grid
    r = len(F)
    c = len(F[0])

    # Check if the starting position is an obstacle, return 0 if it is
    if F[0][0] == 'X':
        return 0

    # Initialize the 2D list to store the number of ways to reach each position
    A = [[0] * c for _ in range(r)]
    # Set the value of the starting position to 1
    A[0][0] = 1

    # Loop through each position in the grid
    for i in range(r):
        for j in range(c):
            # Check if the current position is an obstacle, skip if it is
            if F[i][j] == 'X':
                A[i][j] = 0
                continue
            # Calculate the number of ways to reach the current position
            # by summing the number of ways to reach the position above and
            # the position to the left (if they are open spaces)
            above = A[i - 1][j] if i > 0 and F[i - 1][j] == '.' else 0
            left = A[i][j - 1] if j > 0 and F[i][j - 1] == '.' else 0

            # Store the total number of ways to reach the current position in the list
            A[i][j] += above + left

    # Return the number of ways to reach the bottom-right corner of the grid
    return A[r - 1][c - 1]


# ============= RANDOM GRID =============
def create_random_grid(n):
    grid = [['.' for _ in range(n)] for _ in range(n)]  # Create an empty n x n grid filled with '.'

    for i in range(n):
        for j in range(n):
            if random.random() < 0.2:  # 20% chance to place 'X' in a cell
                grid[i][j] = 'X'

    grid[0][0] = '.'      # Ensure the starting point is not blocked
    grid[n-1][n-1] = '.'  # Ensure the end point is not blocked

    return grid

# ============= MAIN IMPLEMENTATION =============
def main():
    ns = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # Varying sizes of n
    timings = []
    
    for n in ns: # Create an r x c grid for each n value in ns
        grid = create_random_grid(n)    # Use our random grid generator to get random valid and invalid points

        start_time = time.time()            # Get the start time
        num_paths = soccer_dyn_prog(grid)   # Call the Soccer Avoidance DP Solution
        end_time = time.time()              # Get the end time

        runtime = (end_time - start_time)  * 1000 # Calculate runtime in milliseconds
        timings.append(runtime)             # Add the runtime of the Soccer Avoidance Algorithm for the nth element in ns

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