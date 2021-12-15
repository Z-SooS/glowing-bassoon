import random

def init_board():
    return [[".",".","."],[".",".","."],[".",".","."]]

def get_input():
    inp=input("Input:").upper()
    if len(inp)==2:
        if inp[0]=='A':
            if inp[1]=="1":
                return (0,0)
            elif inp[1]=="2":
                return (0,1)
            elif inp[1]=="3":
                return (0,2)
            else:
                print("Incorrect format!")
                return get_input()
        if inp[0]=='B':
            if inp[1]=="1":
                return (1,0)
            elif inp[1]=="2":
                return (1,1)
            elif inp[1]=="3":
                return (1,2)
            else:
                print("Incorrect format!")
                return get_input()
        if inp[0]=='C':
            if inp[1]=="1":
                return (2,0)
            elif inp[1]=="2":
                return (2,1)
            elif inp[1]=="3":
                return (2,2)
            else:
                print("Incorrect format!")
                return get_input()
        else:
            print("Incorrect format!")
            return get_input()
    else:
        print("Incorrect lenght!")
        return get_input()

def get_move(board):
    inp=get_input()
    if board[inp[0]][inp[1]]!='.':
        print("Already occupied")
        return get_move(board)
    else:
        board[inp[0]][inp[1]]="X"
        return board

def display_board(board):
    print("# 1 | 2 | 3 ")
    print(f"A {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(f"B {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(f"C {board[2][0]} | {board[2][1]} | {board[2][2]}")
    pass


board=init_board()
#print(init_board())
display_board(board)
board=get_move(board)
display_board(board)