
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
        self.rowHash = self.generateRowHash(board)
        self.colHash = self.generateColHash(board)
        self.miniHash = self.generateMiniTileHashAsRows(self.rowHash, self.colHash)
        self.linearList = self.generateLinear(board)
        self.miniArray = self.generateEmptyMiniArrayLists()
        self.fillMiniArrayListsFrom2D(self.miniArray, board)

        self.prettyPrintMiniHash(self.miniHash, columns=3)
        print(self.linearList)
        print(self.miniArray)
        miniArray = self.miniArray
        for row in miniArray:
          print(row[0])
          print(row[1])
          print(row[2])

        for firstTwo in range(2):
          self.testCheckers(firstTwo)

        for lastFive in range(75,81):
          self.testCheckers(lastFive)

        return None
        # print(self.board, self.tiles)


######### TESTING / DEBUGGING FUNCTIONS ################
    def compareRowAndCol(self):
        """This is useful if you want to check that your rows and cols were made properly."""
        #print(self.staticRow[5])
        for row in sorted(list(self.staticCol.keys())):
          pass
        #    print(self.staticCol[row][5])
        #print(self.staticRow[0][8])
       # print(self.staticCol[8][0])

    def testCheckers(self, linearPos):
        """ Testing if we can check if a number is not in a row,
        column, or miniboard."""
        boardRow = linearPos // 9
        boardCol = linearPos - (boardRow * 9)
        miniRow = boardRow // 3
        miniCol = boardCol // 3
        print("I am inspecting:")
        print("Linear:", linearPos)
        print("Board: [", boardRow, boardCol, "]")
        print("Mini: [", miniRow, miniCol, "]")
        print("[Linear] Current Value:", self.linearList[linearPos])
        print("[Row]  Current Value:", self.rowHash[boardRow][boardCol])
        print("[Column] Current Value:", self.colHash[boardCol][boardRow])
        
        

########## DATA TYPE GENERATING FUNCTIONS ##################
    def generateLinear(self, listArray):
        """This flattens the sudoku board into one long string of numbers. starting with row0, then row1."""
        bigList = []
        for x in range(9):
          for y in range(9):
            bigList.append(listArray[x][y])
        return bigList

    def generateRowHash(self, givenLists):
        """This generates an unordered hashMap of the ordered numbers in each row. 
        Useful when you just want to see if a number is in a row."""
        rowHash = {}
        for row in range(9):
            rowHash[row] = []
            for col in range(9):
                rowHash[row] += givenLists[row][col]
        return rowHash

    def generateColHash(self, givenLists):
        """This generates an unordered hashMap of the ordered numbers in each column.
        Useful when you just want to see if a number is in a column."""
        colHash = {}
        for row in range(9):
            colHash[row] = []
            for col in range(9):
              colHash[row] += givenLists[col][row]
        return colHash

    def generateEmptyMiniArrayLists(self):
        """This is mainly just used once, but I separated it to be less confusing.
        It returns an array represeting the 3x3 grid of mini-tiles on the board.
        Each mini board just gets an ordered list of the numbers inside of it.
        It does not know the placement of the numbers inside itself."""
        miniArray = [       [    [],    [],    []]   ,     [    [],    [],    []]   ,    [    [],    [],    []]   ]
        print(type(miniArray))
        for rowOfThree in range(3):
            for colOfThree in range(3):
                continue
                miniArray[rowOfThree][colOfThree].append( 'Hi')
        return miniArray
    
    def fillMiniArrayListsFromLinear(self, miniArray, linear):
        """Now we are getting more abstract... We take a miniArrayList data type,
        and fill it up with the numbers from Linear. We modify the given miniArrayList."""
        for num in range(len(linear)):
            if linear[num] == '.':
                continue
            row = num // 9
            miniRow = row // 3
            col = num % 9
            miniCol = col % 3
            miniArray[miniRow][miniCol].append(linear[num])

        return None
 
    def fillMiniArrayListsFrom2D(self, miniArray, board):
        """Now we are getting more abstract... We take a miniArrayList data type,
        and fill it up with the numbers from Linear. We modify the given miniArrayList."""
        for boardRow in range(9):
          for boardCol in range(9):
              #row = boardRow // 9
              miniRow = boardRow // 3
              #col = boardCol % 9
              miniCol = boardCol // 3
              miniArray[miniRow][miniCol].append(board[boardRow][boardCol])

        return None




       
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


######## PRETTY PRINT FUNCTIONS ###################

    def prettyPrintRows(self, rowHash):
        for row in sorted(list(rowHash.keys())):
            print("Row number:", row)
            print([x for x in rowHash[row]])
        return True
        
 
    def prettyPrintCols(self, colHash):
        for row in sorted(list(colHash.keys())):
            print("Col number:", row)
            print([x for x in colHash[row]])
        return True
 
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


############# ACCESS FUNCTIONS ###################

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


############## MODIFY FUNCTIONS ####################

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



######### BACKTRACK FUNCTIONS ##################

    def backtrackRobot(self, row, col, tryNumber, dynamic, static, rowHash, colHash, linear):
        row = linear // 9
        col = linear % 9
        linearPos = row * 9 + col
        for guess in range(1,10):
            if guess in rowHash[row]:
                continue
            if guess in colHash[col]:
                continue
            dynamic[row][col] = guess
            linear[linearPos] = guess
#            self.backtrackRobot(row, col, tryNumber, dynamic, static, rowHash, colHash
   
