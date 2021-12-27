import main
import ai
import random

def todo():
    """
    To-do:
    separate get_move()                                     o
    implement has_won(), returns bool                       o
    implement is_full(), returns bool                       o
    rename 'display_board' to 'print_board'                 O
    implement print-result()                                o
    remove get_player()                                     o
    implement tictactoe_game(), 2 player,x starts           o

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

cor_vals = {'A':0,'B':1,'C':2,'1':0,'2':1,'3':2}

def init_board():
    return [[".",".","."],[".",".","."],[".",".","."]]

def get_move(board):
    inp=input("Input:").upper()
    if check_move(board,inp)==False:
        print("Incorrect format, try again!")
        return get_move(board)
    val=ret_val(inp)
    if check_board(board,val)==False:
        print("Incorrect format, try again!")
        return get_move(board)
    return val
def check_move(board,inp):
    if len(inp)!=2:
        return False
    if (inp[0]!='A' and inp[0]!='B' and inp[0]!='C') or (inp[1]!='1' and inp[1]!='2' and inp[1]!='3'):
        return False
    return True
def check_board(board,move):
    if board[move[0]][move[1]]=='.':
        return True
    return False
def ret_val(move):
    return (cor_vals[move[0]],cor_vals[move[1]])

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
    if (board[0][0]==player and board[0][1]==player and board[0][2]==player)or(board[1][0]==player and board[1][1]==player and board[1][2]==player)or(board[2][0]==player and board[2][1]==player and board[2][2]==player):
        return True
    elif (board[0][0]==player and board[1][0]==player and board[2][0]==player)or(board[0][1]==player and board[1][1]==player and board[2][1]==player)or(board[0][2]==player and board[1][2]==player and board[2][2]==player):
        return True
    elif (board[0][0]==player and board[1][1]==player and board[2][2]==player)or(board[0][2]==player and board[1][1]==player and board[2][0]==player):
        return True
    else:
        return False
def is_full(board):
    for row in range(3):
        for column in range(3):
            if board[row][column]=='.':
                return False
    return True
def print_result(full,win,player):
    if win==True:
        print(f"{player} has won!")
    elif full==True:
        print("It's a tie!")
    else:
        print(f"{change_player(player)} has won!")          
def change_player(player):
    return 'X' if player=='O' else 'O'


def tictactoe(human1=True,human2=True):         #True if human player, human1=x
    board=init_board()
    player='O'
    full=False
    win=False
    while win==False and full==False:
        print_board(board)
        player=change_player(player)
        if (human1==True and player=='X') or (human2==True and player=='O'):
            print(f"Player {player} move:")
            move=get_move(board)
        else:
            move=ai.findBestMove(board,player)
        board=mark(board,move,player)
        win=has_won(board,player)
        full=is_full(board)
    print_board(board)
    print_result(full,win,player)
    pass
    




if __name__ == "__main__":
    tictactoe()
    
    """main.main_menu()
    board=init_board()
    player="X"
    print_board(board)
    move=get_move(board)
    board=mark(board,move,player)
    print_board(board)"""