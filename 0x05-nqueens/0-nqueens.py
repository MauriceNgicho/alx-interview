#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def is_safe(queens, row, col):
    for r, c in queens:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve(row, queens, solutions):
    if row == N:
        solutions.append(queens[:])
        return

    for col in range(N):
        if is_safe(queens, row, col):
            queens.append([row, col])
            solve(row + 1, queens, solutions)
            queens.pop()


solutions = []
solve(0, [], solutions)

for sol in solutions:
    print(sol)
