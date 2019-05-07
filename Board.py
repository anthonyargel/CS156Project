import numpy as np
from Agent import *

# This board class holds an array that represents a connect 4 board.
# This array should only hold -1, 0, or 1.
# 2 represents opponent piece, 1 represents player piece, and 0 representing no piece in that slot on the array.
class Board():
    def __init__(self, row = 7, column = 7):
        self.row = row
        self.column = column
        self.boardSize = (row,column)
        self.board = grids = [[0] * column for _ in range(row)]

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
    
    def printBoardState(self):
        print('Current board:')
        print(*self.board, sep='\n')

    def placePiece(self, pos, player):
        self.board[pos[0]][pos[1]] = player
    
    # given a column number, find the next row that a piece will be placed in.
    # returns the next placement of the piece, if the column is full, will return [-1,-1]
    def getNextPlacement(self, colNbr):
        thePlacementPos = [] # list containing x,y of new pos
        lastRowPos = self.row - 1 #create a variable as the last row position
        while(self.board[lastRowPos][colNbr] != 0 and lastRowPos != -1): # loop through rows in that column
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



######### test code

# create the board
b2 = Board()

# emulating human turn
pos = b2.getNextPlacement(1)
b2.placePiece(pos, 1)

# emulating AI turn
pos = b2.getNextPlacement(4)
b2.placePiece(pos, 2)

# emulating human turn
pos = b2.getNextPlacement(1)
b2.placePiece(pos, 1)

# emulating AI turn
pos = b2.getNextPlacement(5)
b2.placePiece(pos, 2)

b2.printBoardState()
a = Agent()
a.runStaticEvaluatorFunction(b2.board)



