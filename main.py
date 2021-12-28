import tac
import sys


def getplayer():
    player=input().lower()
    if player=="quit":
        return "quit"
    if player=="1" or player=="human":
        return True
    if player=="2" or player=="ai":
        return False
    print("'HUMAN' or 'AI' (1 or 2)")
    return getplayer()

def main_menu():
    print("Tic-Tac-Toe")
    print("Human or ai(1 or 2)\nPlayer 1:")
    p1=getplayer()
    if p1=="quit":
        print("Bye!")
        return
    print("Player 2:")
    p2=getplayer()
    if p2=="quit":
        print("Bye!")
        return
    tac.tictactoe(p1,p2)    
    
    












if __name__ == "__main__":
    print(len(sys.argv))
    if len(sys.argv)==1:
        main_menu()
    elif len(sys.argv)==2 or len(sys.argv)>3:
        raise Exception ("Not enough arguments")
    else:
        if sys.argv[1]=='human':
            p1=True
        elif sys.argv[1]=='ai':
            p1=False
        else:
            raise Exception ("Incorrect argument")
        if sys.argv[2]=='human':
            p2=True
        elif sys.argv[2]=='ai':
            p2=False
        else:
            raise Exception ("Incorrect argument")
        tac.tictactoe(p1,p2)