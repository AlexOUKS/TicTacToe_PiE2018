class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def startGame(self):
        self.board.launch()
        self.player1.setisTurn(True)
        self.player2.setisTurn(False)

    def changeTurn(self):
        if (self.player1.isTurn):
            self.player2.isTurn = True
            self.player1.isTurn = False
        else:
            self.player2.isTurn = False
            self.player1.isTurn = True
        self.checkWin()

    def checkWin(self):
        array = self.board.getBoard()
        valid = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

        for i in range(0, len(valid)):
            if ((array[valid[i][0]] != 0) & (array[valid[i][1]] != 0) & (array[valid[i][2]] != 0)):
                if ((array[valid[i][0]] == array[valid[i][1]] & array[valid[i][1]] == array[valid[i][2]] & array[valid[i][0]] == array[valid[i][2]])):
                    if (array[valid[i][0]] == 1):
                        self.board.endGame(2)
                    else:
                        self.board.endGame(1)


    def getPlayer1(self):
        return self.player1

    def getPlayer2(self):
        return self.player2

    def setBoard(self, board):
        self.board = board