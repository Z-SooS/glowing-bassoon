import random

def init_board():
    return [[".",".","."],[".",".","."],[".",".","."]]
def get_move(board):
    inp=input("Input:").upper()
    if len(inp)==2:
        if inp[0]=='A':
            if inp[1]=="1":
                if board[0][0]!='.':
                    print("Already occupied")
                    return get_move(board)
                else:
                    return (0,0)
            elif inp[1]=="2":
                if board[0][1]!='.':
                    print("Already occupied")
                    return get_move(board)
                else:
                    return (0,1)    
            elif inp[1]=="3":
                if board[0][2]!='.':
                    print("Already occupied")
                    return get_move(board)
                else:
                    return (0,2)
            else:
                print("Incorrect format!")
                return get_move(board)
        if inp[0]=='B':
            if inp[1]=="1":
                if board[1][0]!='.':
                    print("Already occupied")
                    return get_move(board)
                else:
                    return (1,0)
            elif inp[1]=="2":
                if board[1][1]!='.':
                    print("Already occupied")
                    return get_move(board)
                else:
                    return (1,1)
            elif inp[1]=="3":
                if board[1][2]!='.':
                    print("Already occupied")
                    return get_move(board)
                else:
                    return (1,2)
            else:
                print("Incorrect format!")
                return get_move(board)
        if inp[0]=='C':
            if inp[1]=="1":
                if board[2][0]!='.':
                    print("Already occupied")
                    return get_move(board)
                else:
                    return (2,0)
            elif inp[1]=="2":
                if board[2][1]!='.':
                    print("Already occupied")
                    return get_move(board)
                else:
                    return (2,1)
            elif inp[1]=="3":
                if board[2][2]!='.':
                    print("Already occupied")
                    return get_move(board)
                else:
                    return (2,2)
            else:
                print("Incorrect format!")
                return get_move(board)
        else:
            print("Incorrect format!")
            return get_move(board)
    else:
        print("Incorrect lenght!")
        return get_move(board)
def mark(board,move,player):
    board[move[0]][move[1]]=player
    return board
def display_board(board):
    print("# 1 | 2 | 3 ")
    print(f"A {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(f"B {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(f"C {board[2][0]} | {board[2][1]} | {board[2][2]}")
    pass
def get_player():
    player=input("What player would you like to be?(X,O)?").upper()
    return charcheck(player)
def charcheck(player):
    if len(player)==1 and (player=="X" or player=="O"):
        return player
    else:
        print("Incorrect character!")
        return get_player()


board=init_board()
player="X"
display_board(board)
move=get_move(board)
board=mark(board,move,player)
display_board(board)