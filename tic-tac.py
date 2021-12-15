import random

def init_board():
    return [[".",".","."],[".",".","."],[".",".","."]]

def display_board(board):
    print("# 1 | 2 | 3 ")
    print(f"A {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(f"B {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(f"C {board[2][0]} | {board[2][1]} | {board[2][2]}")
    pass


board=init_board()
print(init_board())
display_board(board)