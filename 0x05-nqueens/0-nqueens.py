#!/usr/bin/python3
"""
N Queens Problem Solver

This program solves the N Queens puzzle using backtracking algorithm.
The N Queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard.

Usage: nqueens N
Where N is an integer >= 4
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    
    Args:
        board: Current board state
        row: Row to check
        col: Column to check
        n: Size of the board
    
    Returns:
        True if safe to place queen, False otherwise
    """
    # Check this column on upper rows
    for i in range(row):
        if board[i] == col:
            return False
    
    # Check upper diagonal on left side
    for i in range(row):
        if board[i] == col - (row - i):
            return False
    
    # Check upper diagonal on right side
    for i in range(row):
        if board[i] == col + (row - i):
            return False
    
    return True


def solve_nqueens(board, row, n, solutions):
    """
    Solve N Queens problem using backtracking
    
    Args:
        board: Current board state (list where board[i] = column of queen in row i)
        row: Current row being processed
        n: Size of the board
        solutions: List to store all valid solutions
    """
    # Base case: if all queens are placed
    if row == n:
        # Convert board representation to required format
        solution = [[i, board[i]] for i in range(n)]
        solutions.append(solution)
        return
    
    # Try placing queen in each column of current row
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen
            board[row] = col
            
            # Recursively place queens in remaining rows
            solve_nqueens(board, row + 1, n, solutions)
            
            # Backtrack - remove queen (not strictly necessary as we overwrite)
            board[row] = -1


def main():
    """Main function to handle command line arguments and solve N Queens"""
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Check if N is a valid integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Initialize board and solutions list
    board = [-1] * n  # board[i] represents column of queen in row i
    solutions = []
    
    # Solve the N Queens problem
    solve_nqueens(board, 0, n, solutions)
    
    # Print all solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
