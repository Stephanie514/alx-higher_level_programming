#!/usr/bin/python3
"""Solve the N-Queens puzzle"""

import sys

def init_board(size):
    """Initialize an empty chessboard of size N x N"""
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return board

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check the column above
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 'Q':
            return False
    
    return True

def solve_nqueens(board, row):
    """Recursively solve the N-Queens puzzle"""
    if row == len(board):
        print_solution(board)
        return
    
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            solve_nqueens(board, row + 1)
            board[row][col] = ' '

def print_solution(board):
    """Print a solution as a list of coordinates"""
    solution = []
    for row in board:
        for col, cell in enumerate(row):
            if cell == 'Q':
                solution.append([len(board) - 1 - board.index(row), col])
    print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    board = init_board(n)
    solve_nqueens(board, 0)

