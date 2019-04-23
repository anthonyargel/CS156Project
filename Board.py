import numpy as np


# This board class holds an array that represents a connect 4 board.
# This array should only hold -1, 0, or 1.
# -1 represents opponent piece, 1 represents player piece, and 0 representing no piece in that slot on the array.
class Board():
    def __init__(self, row = 6, column = 7):
        self.row = row
        self.column = column
        self.boardSize = (row,column)
        self.board = np.zeros((row,column)) # create a 2d array of 0s using rows and columns

    # resets the board by making all values 0.
    def reset_board(self):
        for i in range(self.row):
            for j in range(self.column):
                self.board[i][j] = 0

        
    # returns a list containing the state of the board
    # get percept uses this?
    def getBoardState(self):
        # return board
        return self.board

        # saving for now, maybe easier to format?
        result = []
        for i in range(self.row):
            currentRow = []
            for j in range(self.column):
                currentRow.append(self.board[i][j])
            result.append(currentRow)
        return result

    # given a column number, find the next row that a piece will be placed in.
    # returns the next placement of the piece, if the column is full, will return [-1,-1]
    def getNextPlacement(self, colNbr):
        thePlacementPos = [] # list containing x,y of new pos
        lastRowPos = self.row #create a variable as the last row position
        while(self.board[lastRowPos - 1][colNbr] != 0 and lastRowPos != -1): # loop through rows in that column
            lastRowPos = lastRowPos - 1 # if that row isn't empty (aka 0) then look at the next lowest position
            #print(lastRowPos)
        # when we findlowest nonused spot, save it in a list
        if(lastRowPos == -1):
            #print("Didn't find an open spot")
            return [-1,-1]
        else:
            #print("found an open spot")
            thePlacementPos.append(lastRowPos)
            thePlacementPos.append(colNbr)
        return thePlacementPos # return that list
        #for i in range(self.row):




# board testing code from board.py
        
b1 = Board()
#print(b1.getBoardState())

testColumn = 3
for i in range(b1.row):
    b1.board[i][testColumn] = 1
#b1.board[b1.row-1][b1.column-1] = 1
print(b1.getBoardState())
#place = b1.getNextPlacement(testColumn)
#print(place)

for j in range(b1.column):
    pos = b1.getNextPlacement(j)
    if(pos[0] == -1):
        print("no free space available at that position")
    else:
        print("Next free space is at: " + str(b1.getNextPlacement(j)))

