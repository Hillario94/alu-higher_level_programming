#!/usr/bin/python3
"""Solves the N queens problem and prints every solution."""
import sys


def solve(n, row, cols, diag1, diag2, placed, solutions):
    """Place queens row by row with backtracking and collect solutions."""
    if row == n:
        solutions.append([[r, c] for r, c in enumerate(placed)])
        return
    for col in range(n):
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            continue
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)
        placed.append(col)
        solve(n, row + 1, cols, diag1, diag2, placed, solutions)
        placed.pop()
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = []
    solve(n, 0, set(), set(), set(), [], solutions)
    for solution in solutions:
        print(solution)
