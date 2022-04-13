#!/bin/python
# Joe Bussard
# GPL v2

class Solution:
    def __init__(self):
        self.board_pointer = None
        self.mini_board_array = None
        self.back_up_linear_list = None
        self.linear_list = None

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Original work:

        # Setting up data structures
        self.linear_list            = self.generate_linear_list(board)
        self.back_up_linear_list    = self.generate_linear_list(board)
        self.mini_board_array       = self.generate_complete_mini_board_array(board)
        self.board_pointer          = board

        # Main function - returns False if no solution available.
        return self.backtrack(0)

    # Backtrack function
    def backtrack(self, linear_pos):
        """Backtrack function. The main loop for the Sudoku Solver.
        We start in the top-left corner of the Sudoku puzzle. We move left to right,
        then top to bottom.  We always skip boxes that were filled in when we received
        the puzzle.  For each empty box, we check if every number from 1 to 9 inclusive would
        be a legal move.  When a legal move is found, we backtrack by starting the process
        over again with the next box.  There is only one solution, so if we reach the solution
        for the last box, we are finished, and can slowly exit the function."""

        if linear_pos > 80:
            # Puzzle is complete.
            return True
        if self.back_up_linear_list[linear_pos] != '.':
            return self.backtrack(linear_pos + 1)
        else:
            for new_value in range(1, 10):
                if self.is_valid_move(linear_pos, new_value):
                    self.place_number(linear_pos, new_value)
                    if self.backtrack(linear_pos + 1):
                        return True
                    self.place_number(linear_pos, '.')
                else:
                    self.place_number(linear_pos, '.')
            return False

    # Helper functions
    def is_valid_move(self, linear_pos, new_value):
        """Checks if placing this value would break the Sudoku rules.
        Recall that each number must be present in its row, column, and box exactly once each.
        If that number that already exists in a given row, column, and box, return False.
        If that number can be added to the given row, column, and box, return True. """

        str_of_value = str(new_value)

        board_row = linear_pos // 9
        if str_of_value in self.board_pointer[board_row]:
            return False
        board_col = linear_pos - (board_row * 9)
        if any(str_of_value in x[board_col] for x in self.board_pointer):
            return False
        mini_row = board_row // 3
        mini_col = board_col // 3
        if str_of_value in self.mini_board_array[mini_row][mini_col]:
            return False
        return True

    def place_number(self, linear_pos, new_value):
        """Places a value in each of the data structures used to store the Sudoku data.
        - board (the given array)
        - miniArray (the array used to track the 9 mini-boards)
        - linear_list (the list that represents the entire board stretched to 1 dimension)"""

        str_of_value      = str(new_value)
        board_row         = linear_pos // 9
        board_col         = linear_pos - (board_row * 9)
        mini_row          = board_row // 3
        mini_col          = board_col // 3
        mini_linear_pos   = (board_row % 3) * 3 + (board_col %3)

        self.board_pointer[board_row][board_col] = str_of_value
        self.mini_board_array[mini_row][mini_col][mini_linear_pos] = str_of_value
        self.linear_list[linear_pos] = str_of_value

    # Generating the data types

    def generate_linear_list(self, list_array):
        """This flattens the sudoku board into one long string of numbers. The first element is
        the top-left corner of the board. The last element is the bottom-right corner of the board."""

        big_list = []
        for x in range(9):
            for y in range(9):
                big_list.append(list_array[x][y])
        return big_list

    def generate_complete_mini_board_array(self, board):
        """This is mainly just used once, but I separated it to be less confusing.
        It returns an array representing the 3x3 grid of mini-boards on the board.
        Each mini board just gets an ordered list of the numbers inside it.
        I used magic to map the 3D array of mini-boards to the main board itself."""

        mini_board_array = [  [ [],[],[] ], [ [],[],[] ], [ [],[],[] ]  ]
        for board_row in range(9):
            for board_col in range(9):
                mini_row = board_row // 3
                mini_col = board_col // 3
                mini_board_array[mini_row][mini_col].append(board[board_row][board_col])
        return mini_board_array
 
