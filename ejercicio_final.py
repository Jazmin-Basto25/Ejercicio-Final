# -*- coding: utf-8 -*-
"""Ejercicio Final

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OM6SZIkXRe3NxmyLfXUV8rZ63jP7IqF6
"""

import time

def is_valid(board, row, col, num):
   
    if num in board[row]:
        return False

    if num in [board[i][col] for i in range(9)]:
        return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def print_board(board):
   
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

start_time = time.time()
if solve_sudoku(sudoku_board):
    print("Sudoku resuelto:")
    print_board(sudoku_board)
else:
    print("No se encontró solución.")
end_time = time.time()
print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
