
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
 #       self.prettyPrintMiniHash(self.miniHash)
 #       self.prettyPrintMiniHash(self.miniHash, columns=3)
        
        self.compareRowAndCol()
#        self.placeValue(100, 0, 0)
#        self.placeValue(100, 3, 4)
#        self.placeValue(100, 8, 8)
#        self.placeValue(100, 2, 7)
#        self.removeValue(0,0)
#        self.removeValue(0,1)
#        self.removeValue(8,8)
#        self.placeValue(100, 8, 8)
#        if self.checkIfValueInMiniTile(6, 0):
#            print("found 6 in tile 0")
#        
        self.prettyPrintMiniHash(self.miniHash, columns=3)
       # self.prettyPrintRows(self.staticRow)
       # self.prettyPrintCols(self.staticCol)
        self.tempRow, self.tempCol = None, None
        
        self.removeTrivialTiles()
        self.prettyPrintMiniHash(self.miniHash, columns=3)

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
# 3a.    if number is in minibox: continue
# 3.     if number is not in minibox:
# 4.       if an empty tile exists:
# 5.         if empty location is valid (i.e. not in row, not in col)
#              if tempRow is set:
#                remove(tempRow). i++. Backtrack
#              else:
#                place i, set temprow.
#            else:
#          else:
#            keep going


    def removeTrivialTiles(self):
        self.tempRow, self.tempCol = None, None
        #for i in range(1,2): # minis are labelled 0 to 8
        self.tempExists = False
        self.backtrackTrivials(1, 1)

    def backtrackTrivials(self, whichMini, i):
        for symbol in range(i, 10):
          #print("I am looking if I can put", symbol, "in box", whichMini)
          if self.checkIfValueInMiniTile(symbol, whichMini) == False:
            #print("Mini tile", whichMini, "is missing a", symbol)
            miniRow, miniCol = None, None
            exitRowLoop = False
            for rowNum in range(3):#rowNum in sorted(list(self.miniHash[whichMini].keys())):
              if exitRowLoop: break
              for colNum in range(3):
                checkSquare = self.miniHash[whichMini][rowNum][colNum]
                #print(checkSquare)
                if checkSquare == '.':
                  emptySpace = checkSquare
                  bigRow, bigCol = self.getLocationInBig(whichMini, rowNum, colNum)
                 # print("DEBUGGGGGGGGGGGGGGGGGG", bigRow, bigCol)
                  if self.checkIfValueInRow(symbol, bigRow) == True:
                    pass 
                  #dont = ("I can't put", symbol, "in row", bigRow)
                  else:
                      if self.checkIfValueInCol(symbol, bigCol) == True:
                        pass
                #          #print("I can't put", symbol, "in col", bigCol)
                      else:
                          
                          print("I can put", symbol, "in box", whichMini, "at", bigRow, bigCol)
                #          print(self.tempRow, self.tempCol)
                          if self.tempExists:
                          #    print("But there's already a", symbol, "in box", whichMini, "at", self.tempRow, self.tempCol)
                              print("Giving up on", symbol, "in box", whichMini)
                #              print("I will remove it and start again, this time looking for", symbol+1)
           #                   self.removeValue(self.tempRow, self.tempCol)
                              self.tempRow, self.tempCol = None, None
                              self.tempExists = False
                              self.backtrackTrivials(whichMini, symbol + 1)
                              exitRowLoop = True
                              break
                          else:
           #                   self.placeValue(symbol, bigRow, bigCol)
                              self.tempRow, self.tempCol = bigRow, bigCol
                              self.tempExists = True
          if self.tempExists:
            print("I have determined that I can add something to box", whichMini)
            self.placeValue(symbol, bigRow, bigCol)
          self.tempRow, self.tempCol = None, None
          self.tempExists = False



#
#
    def compareRowAndCol(self):
        #print(self.staticRow[5])
        for row in sorted(list(self.staticCol.keys())):
          pass
        #    print(self.staticCol[row][5])
        #print(self.staticRow[0][8])
       # print(self.staticCol[8][0])
        
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
 
        miniHash[0] = [x for x in staticRow[0][0:3]] + [x for x in staticRow[1][0:3]] + [x for x in staticRow[2][0:3]]
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
        print(type(miniHash[0][0]))
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

    def getLocationInBig(self, miniNum, miniRow, miniCol):
        col = (miniNum % 3) * 3 + miniCol
        row = (miniNum // 3) * 3 + miniRow
        #print("DEBUGGGGGG", col, miniNum, miniNum // 3, miniNum * 3, miniRow)
        return row, col

    def getLocationInMini(self, row, col): 
        if row < 3:
            miniRow = row
            if col < 3:
              miniNum = 0
              miniCol = col
            elif col < 6:
              miniNum = 1
              miniCol = col -3
            elif col < 9:
              miniNum = 2
              miniCol = col - 6
        elif row < 6:
            miniRow = row - 3
            if col < 3:
              miniNum = 3
              miniCol = col
            elif col < 6:
              miniNum = 4
              miniCol = col -3
            elif col < 9:
              miniNum = 5
              miniCol = col - 6
        elif row < 9:
            miniRow = row - 6
            if col < 3:
              miniNum = 6
              miniCol = col
            elif col < 6:
              miniNum = 7
              miniCol = col -3
            elif col < 9:
              miniNum = 8
              miniCol = col - 6

        return miniNum, miniRow, miniCol 

    def checkIfValueInMiniTile(self, value, tileNumber):
        #print("Debug!", tileNumber)
        if str(value) in self.miniHash[tileNumber][0] or str(value) in self.miniHash[tileNumber][1] or str(value) in self.miniHash[tileNumber][2]:
            return True
        return False

    def checkIfValueInRow(self, value, row):
        if str(value) in self.staticRow[row]:
            return True
        return False

    def checkIfValueInCol(self, value, col):
        if str(value) in self.staticCol[col]:
            return True
        return False

    

    def placeTempValueInMiniTile(self, value, tileNumber):
        row, col = 0, 0
        tempRow, tempCol = None, None
        for row in range(3):
            for col in range(3): 
                if self.miniTiles[tileNumber][row][col] == value:
                    #print(value, "is already in tile", tileNumber)
                    return False
                else:
                    if not tempRow and not tempCol:
                        tempRow, tempCol = row, col
        return tempRow, tempCol
        pass
        
    def placeValue(self, value, row, col):
        if self.staticRow[row][col] != str('.'): 
            #print("value already there")
            return False
        if self.staticRow[col][row] != str('.'): 
            #print("value already there")
            return False
        self.staticRow[row][col] = str(value)
        self.staticCol[col][row] = str(value)

        if row < 3:
            if col < 3:
              self.miniHash[0][row][col] = str(value)
            elif col < 6:
              self.miniHash[1][row][col-3] = str(value)
            elif col < 9:
              self.miniHash[2][row][col-6] = str(value)
        elif row < 6:
            if col < 3:
              self.miniHash[3][row-3][col] = str(value)
            elif col < 6:
              self.miniHash[4][row-3][col-3] = str(value)
            elif col < 9:
              self.miniHash[5][row-3][col-6] = str(value)
        elif row < 9:
            if col < 3:
              self.miniHash[6][row-6][col] = str(value)
            elif col < 6:
              self.miniHash[7][row-6][col-3] = str(value)
            elif col < 9:
              self.miniHash[8][row-6][col-6] = str(value)
        #print("Inserted", value, "into all tables.")


    def removeValue(self, row, col):
        #if self.staticRow[row][col] == str('.'): 
        #    print("No value at", row, col)
        #    return False
        #if self.staticRow[col][row] == str('.'): 
        #    print("No value at", row, col)
        #    return False
        popped = self.staticRow[row][col]
        self.staticRow[row][col] = str('.')
        self.staticCol[col][row] = str('.')

        if row < 3:
            if col < 3:
              self.miniHash[0][row][col] = str('.')
            elif col < 6:
              self.miniHash[1][row][col-3] = str('.')
            elif col < 9:
              self.miniHash[2][row][col-6] = str('.')
        elif row < 6:
            if col < 3:
              self.miniHash[3][row-3][col] = str('.')
            elif col < 6:
              self.miniHash[4][row-3][col-3] = str('.')
            elif col < 9:
              self.miniHash[5][row-3][col-6] = str('.')
        elif row < 9:
            if col < 3:
              self.miniHash[6][row-6][col] = str('.')
            elif col < 6:
              self.miniHash[7][row-6][col-3] = str('.')
            elif col < 9:
              self.miniHash[8][row-6][col-6] = str('.')
        #print("Inserted", '.', "into all tables.")
        return popped







          

               
