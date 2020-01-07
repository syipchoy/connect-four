#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the Player class or a subclass of Player).
          One player should use 'X' checkers and the other should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

def process_move(p, b):
    """processes a single move by player p on board b"""
    
    print(p , "'s turn")
    
    move = int(p.next_move(b))

    if str(p) == 'Player X':
        b.add_checker('X', move)
    else:
        b.add_checker('O', move)

    print()
    print(b)

    if b.is_win_for('X')== True and b.is_win_for('O')== True:
        print("It's a tie!")
        return True
    elif b.is_win_for('X')== False and b.is_win_for('O')== False:
        return False
    else:
        print(p, 'wins in', p.num_moves, 'moves.')
        print('Congratulations!')
        return True

    

class RandomPlayer(Player):
    """class that creates a player that makes random moves"""
    def __init__(self,checker):
        """initializes random player attributes"""
        super().__init__(checker)

    def __repr__(self):
        """random player class will be represented in the same way as the player class"""
        s = super().__repr__()
        return s

    def next_move(self, b):
        """overrides next_move method inheritted from player
        at random chooses from not full columns in b"""
        not_full = []

        if b.is_full() == True:
            print("Oops! This board is full.")
            halt
        else:
            for col in range(b.width):
                if b.can_add_to(col)== True:
                    not_full += str(col)
        self.num_moves += 1
        choice = int(random.choice(not_full))
        return choice 
        
