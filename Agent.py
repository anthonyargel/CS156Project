import numpy as np

class Agent():
    def __init__(self):
        self.board = 0
        self.fourGoodInARowV = 500
        self.threeGoodInARowV = 5
        self.twoGoodInARowV = 3
        self.oneGoodInARowV = 1
        self.fourBadInARowV = 1000
        self.threeBadInARowV = 6
        self.twoBadInARowV = 2
        self.oneBadInARowV = 1

    def getPercept(self, receivedBoard):
        board = receivedBoard
        return

    def minMax(self, startingPos, atRoot, isMax, maxDepth, currentDepth, currentBoard, val):

    # stop condition is when we've hit max depth
        if currentDepth == maxDepth:
        # when we've hit a leaf node, calculate the value of the state
            newVal = runStaticEvaluationFunction(currentBoard)
            val.append(newVal)
        return val

        # if we're on a max node, then next is min
        if isMax == True:
            for i in len(self.board[0]):
                newP = currentBoard.getNextPlacement(i)
                currentBoard[newP[0], newP[1]] = 2
                if atRoot == True:
                    startingPos = newP
                minMax(startingPos, False, False, maxDepth, currentDepth + 1, currentBoard, val)
            return max(val)
        else:
            for i in len(self.board[0]):
                newP = currentBoard.getNextPlacement(i)
                currentBoard[newP[0], newP[1]] = 1
                if atRoot == true:
                    startingPos = newP
                minMax(startingPos, False, True, maxDepth, currentDepth + 1, currentBoard, val)
            return min(val)
            
    def runStaticEvaluatorFunction(self, board):
        # variables for evaluator function
        frGood = 0
        thrGood = 0
        twoGood = 0
        oneGood = 0
        frBad = 0
        thrBad = 0
        twoBad = 0
        oneBad = 0

        # loop left right
        for i in range(len(board[0])):
            counter = 0
            color = -1
            for j in range(len(board[i])):
                if board[i][j] == color:
                    counter = counter + 1
                    #print(color)
                elif board[i][j] != color:
    # if the board changes color then add totals
                    #the first 1 or 2 we meet becomes color and is counted once
                    if board[i][j] == 1 or board[i][j] == 2 and color == -1:
                        color = board[i][j]
                        counter = 1
                        if j == len(board) - 1: # edge case
                            if color == 1:
                                oneBad = oneBad + 1
                            else:
                                oneGood = oneGood + 1
                    # if 1, we add bad values
                    elif color == 1 and board[i][j] == 2:
                        if counter >= 4:
                            frBad = frBad + 1
                        elif counter == 3:
                            thrBad = thrBad + 1
                        elif counter == 2:
                            twoBad = twoBad + 1
                        elif counter == 1:
                            oneBad = oneBad + 1
                        color = board[i][j]
                        counter = 1
                    elif color == 2 and board[i][j] == 1:
                        if counter >= 4:
                            frGood = frGood +1
                        elif counter == 3:
                            thrGood = thrGood + 1
                        elif counter == 2:
                            twoGood = twoGood +1
                        elif counter == 1:
                            oneGood = oneGood + 1
                            # reset counter
                        color = board[i][j]
                        counter = 1
                    elif board[i][j] == 0 and color != -1: #if board is 0 but previous color wasn't 0
                        #print(str(counter))
                        if color == 1:
                            if counter >= 4:
                                frBad = frBad + 1
                            elif counter == 3:
                                thrBad = thrBad + 1
                            elif counter == 2:
                                twoBad = twoBad + 1
                            elif counter == 1:
                                oneBad = oneBad + 1
                        elif color == 2:
                            if counter >= 4:
                                frGood = frGood +1
                            elif counter == 3:
                                thrGood = thrGood + 1
                            elif counter == 2:
                                twoGood = twoGood +1
                            elif counter == 1:
                                oneGood = oneGood + 1
                                # reset to default because 0 means nothing there
                        color = -1
                        counter = 0
                        #print("counter reset")
                   # print(color) shows how the loop is going
                    

        
        # loop up down
        for i in range(len(board)):
            counter = 0
            color = -1
            for j in range(len(board[i])):
                if board[j][i] == color:
                    counter = counter + 1
                elif board[j][i] != color:
    # if the board changes color then add totals
                    #the first 1 or 2 we meet becomes color and is counted once
                    if board[j][i] == 1 or board[j][i] == 2 and color == -1:
                        color = board[j][i]
                        counter = 1
                        if j == len(board[i]) - 1: # edge case
                            if color == 1:
                                oneBad = oneBad + 1
                            else:
                                oneGood = oneGood + 1
                    # if 1, we add bad values
                    elif color == 1:
                        if counter >= 4:
                            frBad = frBad + 1
                        elif counter == 3:
                            thrBad = thrBad + 1
                        elif counter == 2:
                            twoBad = twoBad + 1
                        elif counter == 1:
                            oneBad = oneBad + 1
                        color = board[j][i]
                        counter = 1
                    elif color == 2:
                        if counter >= 4:
                            frGood = frGood +1
                        elif counter == 3:
                            thrGood = thrGood + 1
                        elif counter == 2:
                            twoGood = twoGood +1
                        elif counter == 1:
                            oneGood = oneGood + 1
                            # reset counter
                        color = board[j][i]
                        counter = 1
                    else:
                        counter = 0

       
        # loop diag negative slope
        self.printValsFound(frGood, thrGood, twoGood, oneGood, frBad, thrBad, twoBad,oneBad)
        evaluatedVal = (self.fourGoodInARowV* frGood) + (self.threeGoodInARowV*thrGood) + (self.twoGoodInARowV*twoGood) + (self.oneGoodInARowV*oneGood) - (self.fourBadInARowV* frBad) - (self.threeBadInARowV*thrBad) - (self.twoBadInARowV*twoBad) - (self.oneBadInARowV*oneBad)
        print("Score for this board state is: " + str(evaluatedVal))


    def printValsFound(self, frGood, thrGood, twoGood, oneGood, frBad, thrBad, twoBad,oneBad):
        print("--------------------------------------------------------")
        print("Pieces (and numeric value) found in a row by player:")
        print("--------------------------------------------------------")
        print("Player: AI")
        print("Four: "+ str(frGood) + " (+"+str(self.fourGoodInARowV*frGood)+")")
        print("Three: "+str(thrGood) + " (+"+str(self.threeGoodInARowV*thrGood)+")")
        print("Two: "+str(twoGood)+ " (+"+str(self.twoGoodInARowV*twoGood)+")")
        print("One: "+str(oneGood) + " (+"+str(self.oneGoodInARowV*oneGood)+")")
        print("--------------------------------------------------------")
        print("Player: Human")
        print("Four: "+ str(frBad)+ " (+"+str(self.fourBadInARowV*frBad)+")")
        print("Three: "+str(thrBad)+ " (+"+str(self.threeBadInARowV*thrBad)+")")
        print("Two: "+str(twoBad)+ " (+"+str(self.twoBadInARowV*twoBad)+")")
        print("One: "+str(oneBad)+ " (+"+str(self.oneBadInARowV*oneBad)+")")
        print("--------------------------------------------------------")
        
