from player import Player
from board import Board
from game import Game

player1 = Player()
player2 = Player()

game = Game(player1, player2)
board = Board(game)
game.setBoard(board)
game.startGame()