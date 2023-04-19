import time

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

    start_time = time.time()
    num_paths = soccer_dyn_prog(grid)
    end_time = time.time()

    print("Number of different paths (dynamic programming):", num_paths)  # Output: 102
    print("Runtime of the soccer_dyn_prog function:", (end_time - start_time))

if __name__ == "__main__":
    main()
