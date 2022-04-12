class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.createMapFromGiven(board)
        self.createTilesFromBoard(board)
        print(self.board, self.tiles)
        
    def createMapFromGiven(self, lists):
        boardMap = {
            1: {}
            }
        for i in range(1, 10):
           boardMap[i] = {}
           for j in range(1, 10):
               boardMap[i][j] = lists[i][j]
        self.board = boardMap

    def createTilesFromBoard(self, board):
        tiles = {
            1: []
            }
        counter = 0
        for i in range(0, 9, 3):
          top_row = list[i]
          second_row = list[i+1]
          third_row = list[i+2]
          tiles[i]     = top_row[0:3] + second_row[0:3] + third_row[0:3]
          tiles[i + 1] = top_row[3:6] + second_row[3:6] + third_row[3:6]
          tiles[i + 2] = top_row[6:9] + second_row[6:9] + third_row[6:9]
        self.tiles = tiles
       

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #elf.createMapFromGiven(board)
        self.createTilesFromBoard(board)
        print(self.board, self.tiles)
        
    def createMapFromGiven(self, lists):
        boardMap = {
            1: {}
            }
        for i in range(1, 10):
           boardMap[i] = {}
           for j in range(1, 10):
               boardMap[i][j] = lists[i][j]
        self.board = boardMap

    def createTilesFromBoard(self, board):
        tiles = {
            1: []
            }
        counter = 0
        for i in range(0, 9, 3):
          top_row = board[i]
          second_row = board[i+1]
          third_row = board[i+2]
          tiles[i]     = top_row[0:3] + second_row[0:3] + third_row[0:3]
          tiles[i + 1] = top_row[3:6] + second_row[3:6] + third_row[3:6]
          tiles[i + 2] = top_row[6:9] + second_row[6:9] + third_row[6:9]
        self.tiles = tiles
       

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #self.createMapFromGiven(board)
        self.createTilesFromBoard(board)
        print(self.board, self.tiles)
        
    def createMapFromGiven(self, lists):
        boardMap = {
            1: {}
            }
        for i in range(1, 10):
           boardMap[i] = {}
           for j in range(1, 10):
               boardMap[i][j] = lists[i][j]
        self.board = boardMap




class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.createMapFromGiven(board)
        self.createTilesFromBoard(self.board)
        print(self.board, self.tiles)
        
    def createMapFromGiven(self, lists):
        boardMap = {
            1: {}
            }
        for i in range(1, 10):
           boardMap[i] = {}
           for j in range(1, 10):
               print(i,j)
               boardMap[i][j] = lists[i-1][j-1]
        self.board = boardMap

    def createTilesFromBoard(self, board):
        tiles = {
            1: {1:'', 2:'', 3:''},
            2: {1:'', 2:'', 3:''},
            3: {1:'', 2:'', 3:''}
            }
        counter = 0
        i = 0
        for starting_point in range(1, 10, 3):
          for small_row in range(0,3):
            tiles[small_row+1][1] = board[starting_point+small_row][starting_point]
            tiles[small_row+1][2] = board[starting_point+small_row][starting_point+1]
            tiles[small_row+1][3] = board[starting_point+small_row][starting_point+2]


        all_tiles = {}
        for i in range(0,3):
          tiles = {
            1: {1:'', 2:'', 3:''},
            2: {1:'', 2:'', 3:''},
            3: {1:'', 2:'', 3:''}
            } 
          tiles[small_row+1][1] = board[starting_point+small_row][starting_point]
          tiles[small_row+1][2] = board[starting_point+small_row][starting_point+1]
          tiles[small_row+1][3] = board[starting_point+small_row][starting_point+2]




          pass


        for i in range(0, 9, 3):
          top_row = board[i]
          second_row = board[i+1]
          third_row = board[i+2]

          tiles[i][1]  = top_row[0:3]
          tiles[i][2]  = second_row[0:3]
          tiles[i][3]  = third_row[0:3]

          tiles[i][1]  = top_row[0:3]
          tiles[i][2]  = second_row[0:3]
          tiles[i][3]  = third_row[0:3]



          tiles[i]     = top_row[0:3] + second_row[0:3] + third_row[0:3]
          tiles[i + 1] = top_row[3:6] + second_row[3:6] + third_row[3:6]
          tiles[i + 2] = top_row[6:9] + second_row[6:9] + third_row[6:9]
        self.tiles = tiles
       


