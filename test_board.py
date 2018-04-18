from unittest import TestCase
from game import Game
from board import Board
from player import Player

class TestBoard(TestCase):
    def test_draw(self):
        player1 = Player()
        player2 = Player()
        game = Game(player1, player2)
        board = Board(game)
        game.setBoard(board)
        event = Event()
        testboard = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(board.draw(event), testboard)

class Event:
    def __init__(self):
        self.x = 100
        self.y = 100

    def x(self):
        return self.x

    def y(self):
        return self.y

