
#!/bin/python
# Joe Bussard
# All code after the line that says "Original Work" is Copyright Joe Bussard 2022
# and licensed under GPL v2

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

# Original work:

        # Setting up data structures
        self.linearList        = self.generateLinear(board)
        self.backUpLinear      = self.generateLinear(board)
        self.miniBoardArray    = self.generateCompleteMiniBoardArray(board)
        self.boardPointer      = board

        # Main function - returns False if no solution available.
        return self.backtrack(0)

# Backtrack function
    def backtrack(self, linearPos):
      """Backtrack function. The main loop for the Sudoku Solver.
      We start at the top-left corner of the Sudoku puzzle. We move left to right,
      then top to bottom.  We always skip boxes that were filled in when we recieved
      the puzzle.  For each empty box, we check if every number from 1 to 9 inclusive would
      be a legal move.  When a legal move is found, we backtrack by starting the process
      over again with the next box.  There is only one solution, so if we reach the solution
      for the last box, we are finished, and can slowly exit the function."""

      if linearPos > 80:
        # Puzzle is complete.
        return True
      if self.backUpLinear[linearPos] != '.':
        return self.backtrack(linearPos + 1)
      else: 
        for newValue in range(1, 10): 
          if self.isValidMove(linearPos, newValue):
            self.placeNumber(linearPos, newValue)
            if self.backtrack(linearPos + 1):
              return True
            self.placeNumber(linearPos, '.')
          else: 
            self.placeNumber(linearPos, '.')
        return False

# Helper functions
    def isValidMove(self, linearPos, newValue):
      """Checks if placing this value would break the Sudoku rules.
      Recall that each number must be present in its row, column, and box exactly once each.
      If that number that already exists in a given row, column, and box, return False.
      If that number can be added to the given row, column, and box, return True. """

      strValue = str(newValue)
      boardRow = linearPos // 9
      boardCol = linearPos - (boardRow * 9)
      miniRow = boardRow // 3
      miniCol = boardCol // 3

      if strValue in self.boardPointer[boardRow]:
          return False
      elif any(strValue in x[boardCol] for x in self.boardPointer):
          return False
      elif strValue in self.miniBoardArray[miniRow][miniCol]:
          return False
      return True
 
    def placeNumber(self, linearPos, newValue):
        """Places a value in each of the data structures used to store the Sudoku data.
        - board (the given array)
        - miniArray (the array used to track the 9 mini-boards
        - linearList (the list that represents the entire board stretched to 1 dimension."""

        strValue = str(newValue)
        boardRow = linearPos // 9
        boardCol = linearPos - (boardRow * 9)
        miniRow = boardRow // 3
        miniCol = boardCol // 3
        miniPos = (boardRow % 3) * 3 + (boardCol %3)

        self.boardPointer[boardRow][boardCol] = strValue
        self.miniBoardArray[miniRow][miniCol][miniPos] = strValue
        self.linearList[linearPos] = strValue
 
 # Generating the data types

    def generateLinear(self, listArray):
        """This flattens the sudoku board into one long string of numbers. The first element is
        the top-left corner of the board. The last element is the bottom-right corner of the board."""

        bigList = []
        for x in range(9):
          for y in range(9):
            bigList.append(listArray[x][y])
        return bigList

    def generateCompleteMiniBoardArray(self, board):
        """This is mainly just used once, but I separated it to be less confusing.
        It returns an array represeting the 3x3 grid of mini-boards on the board.
        Each mini board just gets an ordered list of the numbers inside of it.
        I used magic to map the 3D array of mini-boards to the main board itself."""

        miniBoardArray = [  [ [],[],[] ] , [ [],[],[] ] , [ [],[],[] ]  ]
        for boardRow in range(9):
          for boardCol in range(9):
              miniRow = boardRow // 3
              miniCol = boardCol // 3
              miniBoardArray[miniRow][miniCol].append(board[boardRow][boardCol])
        return miniBoardArray
 
