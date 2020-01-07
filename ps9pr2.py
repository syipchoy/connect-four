#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below

class Player:
    """a data type to be able to like actually play the game w someone"""

    def __init__(self, checker):
        """initializes attribute checker and num moves"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """indicates which checker the player object is using"""
        return 'Player ' + self.checker

    def opponent_checker(self):
        """returns the checker of the player object's opponent"""
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        """takes Board object as a parameter and returns the col where the player wants to make the next move"""
        col = input('Enter a column: ')
        while b.can_add_to(int(col)) == False:
            print('Try again!')
            col = input('Enter a column: ')
        if b.can_add_to(int(col)) == True:
            self.num_moves += 1
        return col
