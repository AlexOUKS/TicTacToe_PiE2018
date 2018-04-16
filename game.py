import socket, sys

class Game:

    def __init__(self, player):
        self.player = player

    def connectingToServer(self):
        self.connexion_with_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connexion_with_server.connect(('127.0.0.1', 50000))
        self.connexion_with_server.send(b"Je viens d'accepter la connexion")
        while 1:
            data = self.connexion_with_server.recv(4096)
            print(str(data))


    def startGame(self):
        self.board.launch()
       # self.player1.setisTurn(True)
       # self.player2.setisTurn(False)

    def changeTurn(self):
     #   if (self.player1.isTurn):
     #       self.player2.isTurn = True
     #       self.player1.isTurn = False
      #  else:
      #      self.player2.isTurn = False
      #      self.player1.isTurn = True
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


    def setPlayerName(self, name):
        self.player.setName(name)
        self.board.waitingScreen()

    def setBoard(self, board):
        self.board = board
        self.board.waitNamePlayer()