from Board import *

class GameManager():
    def __init__(self):
        self.turn = 0 # 1 if player turn or -1 if enemy turn
        self.started = False
        self.gB = Board()# game board

    def startGame(self):
        return 0
        # set enemy difficulty as a string
        # use this to and create agent here

        # prompt player for head/tails for turn order

        # taketurn

    def takeTurn(self, currentPlayer):
        self.gB.p
        if(currentPlayer== 1):
            print("Please select a column (0 - 6)")
            k = input()
            k = int(k)
            pos = self.gB.getNextPlacement(k)
            #print("You selected " + str(k))
            print("Your piece was placed at " + str(pos[0]) + " " + str(pos[1]))
            return 0 # change this later to take a player input
        else:
            return 0 # change this later so that calls agent decision making

    def testforWinner(self):
        return 0
        # also kind of hard logic. search for four in a row.

gm = GameManager()
gm.takeTurn(1)
