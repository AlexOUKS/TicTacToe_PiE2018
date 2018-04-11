from tkinter import *

class Board:

    def __init__(self, game):
        self.game = game
        self.newGame()

    def newGame(self):
        self.coordBoard = [[[0, 0], [200, 200]],
                           [[200, 0], [400, 200]],
                           [[400, 0], [600, 200]],
                           [[0, 200], [200, 400]],
                           [[200, 200], [400, 400]],
                           [[400, 200], [600, 400]],
                           [[0, 400], [200, 600]],
                           [[200, 400], [400, 600]],
                           [[400, 400], [600, 600]]]

        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.window = Tk()

        self.window['bg'] = 'white'

        self.canvas = Canvas(self.window, width=600, height=600, background='yellow')
        ligne1 = self.canvas.create_line(200, 0, 200, 600)
        ligne2 = self.canvas.create_line(400, 0, 400, 600)
        ligne3 = self.canvas.create_line(0, 200, 600, 200)
        ligne4 = self.canvas.create_line(0, 400, 600, 400)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.draw)

        bouton = Button(self.window, text="Replay", command=self.clearBoard)
        bouton.pack(side=LEFT)

    def clearBoard(self):
        self.newGame()

    def draw(self, event):

        for i in range(0, len(self.coordBoard)):
            x1 = self.coordBoard[i][0][0]
            y1 = self.coordBoard[i][0][1]
            x2 = self.coordBoard[i][1][0]
            y2 = self.coordBoard[i][1][1]
            if (self.board[i] == 0):
                if ((x1 < event.x & event.x < x2) & (y1 < event.y & event.y < y2)):
                    if (self.game.getPlayer1().getisTurn() == True):
                        self.canvas.create_line(x1, y1, x2, y2)
                        self.canvas.create_line(x2, y1, x1, y2)
                        self.board[i] = 1
                    else:
                        ligne1 = self.canvas.create_line(200, 0, 200, 600)
                        self.canvas.create_oval(x1, y1, x2, y2, outline="#1f1", width=2)
                        self.board[i] = 2
                    self.game.changeTurn()


    def launch(self):
        self.window.mainloop()

    def endGame(self, num):
        self.canvas.create_text(300, 300, text="Player "+str(num)+" win", font="Arial 16 italic", fill="blue")
        self.canvas.unbind("<Button 1>")

    def getBoard(self):
        return self.board