import time as time

class SudokuBoard(object):
    """Class representation of our sudoku board"""

    def __init__(self, board):
        """ a 2-D array of 9x9 represents our board"""
        self.board = board
        self.counter = 0

    def get_counter(self):
        return self.counter

    def print_board(self):
        """ print out a string representation of the board"""
        for i in range(len(self.board)):
            if ((i % 3) == 0) and i != 0:
                print("- - - - - - - - - - - ")
            for j in range(len(self.board[0])):
                if (j % 3) == 0 and j != 0:
                    print("| ", end="")
                print(str(self.board[i][j]) + ' ', end="")
                if j == 8:
                    print()

    def is_valid(self, row, column, number):
        """Checks if the newly entered number does not invalidate the board"""
        #check row
        for i in range(len(self.board[0])):
            if self.board[row][i] == number and column != i:
                return False
        #check column
        for i in range(len(self.board)):
            if self.board[i][column] == number and row != i:
                return False
        #check square
        x = row // 3 * 3
        y = column // 3 * 3
        for i in range(3):
            for j in range(3):
                if self.board[x+i][y+j] == number and row != x+i and column != y+i:
                    return False
        # if all conditions passed return True
        return True

    def next_empty(self):
        """ returns the next empty square in the board"""
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return i, j
        return -1, -1

    def find_previous(self, original, x, y):
        """ find the previous altered value """
        # move to the item before in the column
        if x == 0 and y == 0:
            return -1, -1
        if y == 0:
            y = 8
            x -= 1
        else:
            y -= 1
        while original[x][y] != 0:
            # if the one before cant be altered, move again to the one before
            if x == 0 and y == 0:
                return -1, -1
            if y == 0:
                y = 8
                x -= 1
            else:
                y -= 1
        return x, y

    def copy(self):
        """ copy the original array so that it is not altered"""
        original = []
        for i in range(len(self.board)):
            arr = []
            for j in range(len(self.board)):
                arr.append(self.board[i][j])
            original.append(arr)
        return original

    def insert(self, row, column, condition):
        """ return true if the best number is inserted, false otherwise"""
        if condition == 9:
            return False
        for i in range(condition+1, 10):
            self.counter += 1
            if self.is_valid(row, column, i):
                self.board[row][column] = i
                return True
        return False

    def solve(self):
        """ solve the board"""
        original = self.copy()
        while self.next_empty()[0] != -1:
            x, y = self.next_empty()
            while not self.insert(x, y, self.board[x][y]):
                self.board[x][y] = 0
                x, y = self.find_previous(original, x, y)

                if x == -1:
                    print("Not Valid")
                    return 0


board_start = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

puzzle = SudokuBoard(board_start)
puzzle.print_board()
print()
print()
start = time.time()
puzzle.solve()
stop = time.time()
print("Solution found in: " + str(round(stop-start, 4)) + "seconds after checking " + str(puzzle.get_counter()) +
      " board configurations")
puzzle.print_board()
