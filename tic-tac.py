import random

def init_board():
    return [["A",".","."],[".",".","."],[".",".","."]]

def get_move(board):
    inp=input("Input:").upper()
    if len(inp)!=2:
        print("Incorrect lenght!")
        return get_move(board)
    else:
        if inp[0]=='A' or inp[0]=='B' or inp[0]=='C' and inp[1]=="1" or inp[1]=="2" or inp[1]=="3":
            if board[inp[0]][inp[1]]!='.':
                print("Already occupied")
                return get_move(board)
            else:
                board[inp[0]][inp[1]]='X'
                return board
        else:
            print("Incorrect format!")
            return get_move(board)
    

def display_board(board):
    print("# 1 | 2 | 3 ")
    print(f"A {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(f"B {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(f"C {board[2][0]} | {board[2][1]} | {board[2][2]}")
    pass


board=init_board()
#print(init_board())
display_board(board)
get_move(board)