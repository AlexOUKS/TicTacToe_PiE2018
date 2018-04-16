from player import Player
from board import Board
from game import Game

player = Player()
game = Game(player)
board = Board(game)
game.setBoard(board)
