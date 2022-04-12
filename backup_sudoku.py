
#!/bin/python
# Joe Bussard
# All code after the line that says "ORIGINAL WORK" is Copyright Joe Bussard 2022
# and licensed under GPL v2

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
############# ORIGINAL WORK ##################
############### TESTING ###################
        self.staticRow = self.generateRowHash(board)
        self.staticCol = self.generateColHash(board)
        self.miniHash  = self.generateMiniTileHashAsRows(self.staticRow, self.staticCol)
        self.prettyPrintMiniHash(self.miniHash)
        self.prettyPrintMiniHash(self.miniHash, columns=3)
        
        if self.checkIfValueInMiniTile(6, 0):
            print("found 6 in tile 0")

        return None
        # print(self.board, self.tiles)
        
# Main function pseudocode
# 1. Load the data structures for the board.
# 2. Fill in all tiles with a trivial solution
# 3. Fill in remaining tiles
#
# Trivial Solution tiles pseudocode
# 1. for each minibox:
# 2.   for number in (0,9):
# 3.     if number is not in minibox:
# 4.       
#
#
#
        
    def generateRowHash(self, givenLists):
        rowHash = {}
        for row in range(9):
            rowHash[row] = []
            for col in range(9):
                rowHash[row] += givenLists[row][col]
        return rowHash

    def prettyPrintRows(self, rowHash):
        for row in sorted(list(rowHash.keys())):
            print("Row number:", row)
            print([x for x in rowHash[row]])
        return True
        
    def generateColHash(self, givenLists):
        colHash = {}
        for row in range(9):
            colHash[row] = []
            for col in range(9):
              colHash[row] += givenLists[col][row]
        return colHash

    def prettyPrintCols(self, colHash):
        for row in sorted(list(colHash.keys())):
            print("Col number:", row)
            print([x for x in colHash[row]])
        return True
        
    def generateMiniTileHash(self, staticRow, staticCol):
        miniHash = {}
        for mini in range(9):
            miniHash[mini] = []
            miniHash[0] = [x for x in staticRow[0][0:3]] + [x for x in staticRow[1][0:3]] + [x for x in staticRow[2][0:3]]
            miniHash[1] = [x for x in staticRow[0][3:6]] + [x for x in staticRow[1][3:6]] + [x for x in staticRow[2][3:6]]
            miniHash[2] = [x for x in staticRow[0][6:9]] + [x for x in staticRow[1][6:9]] + [x for x in staticRow[2][6:9]]
 
        miniHash[0]= [x for x in staticRow[0][0:3]] + [x for x in staticRow[1][0:3]] + [x for x in staticRow[2][0:3]]
        miniHash[1] = [x for x in staticRow[0][3:6]] + [x for x in staticRow[1][3:6]] + [x for x in staticRow[2][3:6]]
        miniHash[2] = [x for x in staticRow[0][6:9]] + [x for x in staticRow[1][6:9]] + [x for x in staticRow[2][6:9]]

        miniHash[3] = [x for x in staticRow[3][0:3]] + [x for x in staticRow[4][0:3]] + [x for x in staticRow[5][0:3]]
        miniHash[4] = [x for x in staticRow[3][3:6]] + [x for x in staticRow[4][3:6]] + [x for x in staticRow[5][3:6]]
        miniHash[5] = [x for x in staticRow[3][6:9]] + [x for x in staticRow[4][6:9]] + [x for x in staticRow[5][6:9]]
 
        miniHash[6] = [x for x in staticRow[6][0:3]] + [x for x in staticRow[7][0:3]] + [x for x in staticRow[8][0:3]]
        miniHash[7] = [x for x in staticRow[6][3:6]] + [x for x in staticRow[7][3:6]] + [x for x in staticRow[8][3:6]]
        miniHash[8] = [x for x in staticRow[6][6:9]] + [x for x in staticRow[7][6:9]] + [x for x in staticRow[8][6:9]]
        
        return miniHash

    def generateMiniTileHashAsRows(self, staticRow, staticCol):
        miniHash = {}
        for mini in range(9):
            miniHash[mini] = [[],[],[]]

        miniHash[0][0], miniHash[0][1], miniHash[0][2] = [x for x in staticRow[0][0:3]] , [x for x in staticRow[1][0:3]] , [x for x in staticRow[2][0:3]]
        miniHash[1][0], miniHash[1][1], miniHash[1][2] = [x for x in staticRow[0][3:6]] , [x for x in staticRow[1][3:6]] , [x for x in staticRow[2][3:6]]
        miniHash[2][0], miniHash[2][1], miniHash[2][2] = [x for x in staticRow[0][6:9]] , [x for x in staticRow[1][6:9]] , [x for x in staticRow[2][6:9]]

        miniHash[3][0], miniHash[3][1], miniHash[3][2] = [x for x in staticRow[3][0:3]] , [x for x in staticRow[4][0:3]] , [x for x in staticRow[5][0:3]]
        miniHash[4][0], miniHash[4][1], miniHash[4][2] = [x for x in staticRow[3][3:6]] , [x for x in staticRow[4][3:6]] , [x for x in staticRow[5][3:6]]
        miniHash[5][0], miniHash[5][1], miniHash[5][2] = [x for x in staticRow[3][6:9]] , [x for x in staticRow[4][6:9]] , [x for x in staticRow[5][6:9]]
 
        miniHash[6][0], miniHash[6][1], miniHash[6][2] = [x for x in staticRow[6][0:3]] , [x for x in staticRow[7][0:3]] , [x for x in staticRow[8][0:3]]
        miniHash[7][0], miniHash[7][1], miniHash[7][2] = [x for x in staticRow[6][3:6]] , [x for x in staticRow[7][3:6]] , [x for x in staticRow[8][3:6]]
        miniHash[8][0], miniHash[8][1], miniHash[8][2] = [x for x in staticRow[6][6:9]] , [x for x in staticRow[7][6:9]] , [x for x in staticRow[8][6:9]]

        return miniHash


    def prettyPrintMiniHash(self, miniHash, columns=1):
        if columns == 1:
            for tile in range(9):
                print(miniHash[tile][0])
                print(miniHash[tile][1])
                print(miniHash[tile][2])
                print("_______________")
            return True
        elif columns == 3:
            for tile in range(0,9,3):
                print(miniHash[tile+0][0], miniHash[tile+1][0], miniHash[tile+2][0])
                print(miniHash[tile+0][1], miniHash[tile+1][1], miniHash[tile+2][1])
                print(miniHash[tile+0][2], miniHash[tile+1][2], miniHash[tile+2][2])
                print("______________________________________________")
            return True
        print("You only need to print 1 or 3 columns at a time...")
        return False

            

    def checkIfValueInMiniTile(self, value, tileNumber):
      if str(value) in self.miniHash[tileNumber][0] or str(value) in self.miniHash[tileNumber][1] or str(value) in self.miniHash[tileNumber][2]:
          return True
      return False

        




          

                
