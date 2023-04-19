import time
import random
import numpy as np  
import matplotlib.pyplot as plt


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
    ns = [2000, 3000, 4000]  # Varying sizes of n
    timings = []

    for n in ns:
        grid = create_random_grid(n)
        
        start_time = time.time()
        num_paths = soccer_dyn_prog(grid)
        end_time = time.time()

        runtime = end_time - start_time  # Calculate runtime in seconds
        timings.append(runtime)

        print(f"Size: {n}x{n}, Number of different paths: {num_paths}, Runtime: {runtime:.2f} seconds")  # Output in seconds
    # Use the ns and timings from the previous code
    plt.scatter(ns, timings, label="Data Points")
    plt.xlabel("Grid Size (n)")
    plt.ylabel("Elapsed Time (seconds)")  # Update ylabel to seconds
    plt.title("Timing Data for Soccer Dynamic Programming")

    # Fit a line to the data
    coefficients = np.polyfit(ns, timings, 1)  # 1 means a linear fit
    fit_line = np.poly1d(coefficients)
    plt.plot(ns, fit_line(ns), label="Fit Line", color="red")
    plt.legend()
    plt.savefig("timing_data_plot.png")

    return ns, timings

if __name__ == "__main__":
    ns, timings = main()
