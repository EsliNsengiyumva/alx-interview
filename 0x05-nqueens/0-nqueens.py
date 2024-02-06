#!/usr/bin/env python3
"""
N queens
"""

import sys

def solve_nqueens(n):
    '''Returns all possible solutions for placing n queens on an n×n chessboard'''
    if n == 0:
        return [[]]
    inner_solutions = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_q)
            for solution in inner_solutions
            if is_safe((n, i + 1), solution)]

def is_safe(square, queens):
    '''Checks if placing a queen in the given square is safe'''
    (row1, col1) = square
    for (row2, col2) in queens:
        if row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2):
            return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        n_q = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n_q < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = solve_nqueens(n_q)
    for answer in reversed(solutions):
        print([[i - 1 for i in p] for p in answer])

    
    
    