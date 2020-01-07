#stephany yipchoy
#im so sorry it's slightly out of order bc i was getting like an indent error idk im vvvvvvvvvv sorry


class Board:
    """a data type for a connect4 board w arbitrary dimenstions"""


    def __init__(self, height, width):
        """initializes the parameters"""
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string

            # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        hyphens = '-' * self.width * 2 + '-'
        s += hyphens
        s += '\n'
        # and the numbers underneath it.
        count = 0
        s += ' '
        for x in range(self.width):
            
            if count > 9:
                count = 0
                s += str(count)
                s += ' '
                count += 1
            else:
                s += str(count)
                s += ' '
                count += 1

        return s

    def add_checker(self, checker, col):
        """adds a checker to the designated spot"""
        assert(checker == 'X' or checker == 'O')
        assert(0 <= int(col) < int(self.width))

        row = 0
        while row < self.height - 1:
            if self.slots[row+1][col] != ' ':
                #print ('made it')
                row = row
                break 
            elif self.slots[row][col] == ' ':
                row += 1
                #print ('fuck')
            
        self.slots[row][col] = checker

    def reset(self):
        """resets the board object by setting all slots to an open space character"""
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ returns true if it's valid to place a checker in col"""
        if col > self.width - 1 or col < 0:
            return False
        elif self.slots[0][col] != ' ':
            return False
        else:
            return True

    def remove_checker(self, col):
        """removes top checker from column col"""
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """returns true if it's a vertical win"""
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """returns true if it's a down diagonal win"""
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False
    
    def is_up_diagonal_win(self, checker):
        """returns true if it's an up diagonal win"""
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        return False

    def is_win_for(self, checker):
        """accepts either x or o and returns true if that parameter wins"""
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False 

    def is_full(self):
        """returns true if board is full of checkers, false otherwise"""
        for row in range(self.height):
            for col in range(self.width):
                if self.can_add_to(col) == True:
                    return False
        return True


                


