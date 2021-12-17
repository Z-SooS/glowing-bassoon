import main
import random

def todo():
    """
    To-do:
    separate get_move()                                 x
    implement has_won(), returns bool                   x
    implement is_full(), returns bool                   x
    rename 'display_board' to 'print_board'                 O
    implement print-result()                            x
    remove get_player()                                     o
    implement tictactoe_game(), 2 player,x starts       x

    AI:                                         
    'HUMAN-AI' and 'AI-HUMAN' arguments                 x
    OPT - 'AI-AI' possible                              x
    get_ai_move()                                       x
    OPT - easy win,avoid losing                         x
    OPT - unbeatable AI                                 x
    implement main_menu()                               x


    OPT-typing 'quit' exits the game anytime            x
    """
    pass


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
def print_board(board):
    print("# 1 | 2 | 3 ")
    print(f"A {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(f"B {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(f"C {board[2][0]} | {board[2][1]} | {board[2][2]}")
    pass

def has_won(board,player):
    return False

def is_full(board):
    return False

def print_result(full,win,player):
    if full==True:
        print("It's a tie!")
    elif win==True:
        print(f"{player} has won!")
    else:
        pass
            
def change_player(player):
    return 'X' if player=='O' else 'O'

def tictactoe(human1=True,human2=True):         #True if human player, human1=x
    board=init_board()
    player='O'
    full=False
    win=False
    while win==False and full==False:
        if player=='O':
            player='X'
        else:
            player='O'
        print(f"Player {player} move:")
        move=get_move(board)
        board=mark(board,move,player)
        win=has_won(board,player)
        full=is_full(board)
    print_result(full,win,player)
    pass
    




if __name__ == "__main__":
    print(change_player('O'))
    main.main_menu()
    board=init_board()
    player="X"
    print_board(board)
    move=get_move(board)
    board=mark(board,move,player)
    print_board(board)