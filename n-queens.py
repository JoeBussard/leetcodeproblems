class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        self.resize_board(n)
        self.n = n
        ans = self.backtrack_queens()
        return ans
    
    board = {}
    queens = {}
    count = 0
    
    def resize_board(self, n):
        for i in range(0, n):
            for j in range(0, n):
                self.board[(str(i)+str(j))] = 'O'
        
    def is_not_under_attack(self, row, col):
        rowColStr = self.board[str(row) + str(col)]
        if rowColStr == 'O':
            return True
        else:
            return False
    
    def update_board(self):
      # could change this to True / False
        for square in self.board.keys():
            self.board[square] = 'O'
        for queen in self.queens.keys():
            for square in self.board.keys():
                if square in self.queens[queen]:
                    if self.queens[queen][square] == True:
                        self.board[square] = 'X'
        
    def place_queen(self, row, col):
        rowColStr = str(row) + str(col)
        queens_attacks = {}
        queens_attacks[rowColStr] = True
        diagonalStrs = []
        for i in range(self.n):
            queens_attacks[str(i) + str(col)] = True
            queens_attacks[str(row) + str(i)] = True

            if i > 0: # diagonals
                diagonalStrs.append(str(row-i) + str(col-i))
                diagonalStrs.append(str(row+i) + str(col+i))
                diagonalStrs.append(str(row-i) + str(col+i))
                diagonalStrs.append(str(row+i) + str(col-i))
                                
        for diagonalStr in diagonalStrs:
            if diagonalStr in self.board:
                queens_attacks[diagonalStr] = True
                
        self.queens[rowColStr] = queens_attacks
        self.update_board()
    
    def remove_queen(self, row, col):
        rowColStr = str(row) + str(col)
        if rowColStr in self.queens.keys():
            self.queens.pop(rowColStr)
        self.update_board()
    
    def pretty_print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[(str(i)+str(j))], end=" ")
            print("")
        return None
        
                                
    def backtrack_queens(self,row = 0, count = 0):
        for col in range(self.n):
            # iterate through columns at the curent row.
            if self.is_not_under_attack(row, col):
                # explore this partial candidate solution, and mark the attacking zone
                self.place_queen(row, col)
                if row + 1 == self.n:
                    # we reach the bottom, i.e. we find a solution!
                    self.count += 1
                else:
                    # we move on to the next row
                    self.count = self.backtrack_queens(row + 1, self.count)
                # backtrack, i.e. remove the queen and remove the attacking zone.
                self.remove_queen(row, col)
        return self.count        
