#!/usr/bin/python3
"""The N-queens puzzle"""


import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for _ in range(n)]
    [row.append(0) for _ in range(n) for row in board]
    return board


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, n):
    """Recursively solve the N-Queens puzzle."""
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n)
            board[row][col] = 0


def print_solution(board):
    """Print a solution as a list of coordinates."""
    solution = []
    for row in board:
        for col, cell in enumerate(row):
            if cell == 1:
                solution.append([len(board) - 1 - board.index(row), col])
    print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(n)
    solve_nqueens(board, 0, n)
