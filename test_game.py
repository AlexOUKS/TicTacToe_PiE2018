from unittest import TestCase
from game import Game
from board import Board
from player import Player


class TestGame(TestCase):
    def test_checkWin(self):
        player1 = Player()
        player2 = Player()
        game = Game(player1, player2)
        board = Board(game)
        game.setBoard(board)
        testboard = [1,1,1,0,2,0,0,2,0]
        board.setBoard(testboard)
        self.assertEqual(game.checkWin(), True)
        testboard = [2, 2, 2, 0, 1, 0, 0, 1, 0]
        board.setBoard(testboard)
        self.assertEqual(game.checkWin(), True)
