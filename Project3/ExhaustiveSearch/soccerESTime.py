import time
import random
import matplotlib.pyplot as plt
import numpy as np

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


def create_random_grid(n):
    grid = [['.' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if random.random() < 0.2:  # 20% chance to place 'X' in a cell
                grid[i][j] = 'X'

    grid[0][0] = '.'  # Ensure the starting point is not blocked
    grid[n-1][n-1] = '.'  # Ensure the end point is not blocked

    return grid


def main():
    ns = [10, 12, 14 ]  # Varying sizes of n
    timings = []

    for n in ns:
        grid = create_random_grid(n)

        start_time = time.time()
        num_paths = count_paths_exhaustive(grid)
        end_time = time.time()

        runtime = end_time - start_time  # Calculate runtime in seconds
        timings.append(runtime)

        print(f"Size: {n}x{n}, Number of different paths: {num_paths}, Runtime: {runtime:.2f} s")

    # Plot the data
    plt.scatter(ns, timings, label="Data Points")
    plt.xlabel("Grid Size (n)")
    plt.ylabel("Elapsed Time (seconds)")  # Update ylabel to seconds
    plt.title("Timing Data for count_paths_exhaustive")

    # Fit a line to the data
    coefficients = np.polyfit(ns, timings, 1)  # 1 means a linear fit
    fit_line = np.poly1d(coefficients)
    plt.plot(ns, fit_line(ns), label="Fit Line", color="red")
    plt.legend()
    plt.savefig("timing_data_plot_exhaustive.png")

    return ns, timings


if __name__ == "__main__":
    ns, timings = main()
