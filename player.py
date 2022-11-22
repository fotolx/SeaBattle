from gameExceptions import *
import random as rnd


class Player:
    def __init__(self, player_board, enemy_board):
        rnd.seed()
        self.board = player_board
        self.enemy_board = enemy_board
        self.size = self.board.size

    def ask(self):
        pass

    def move(self):
        while True:
            try:
                coords = self.ask()
                return self.enemy_board.shot(coords)
            except BoardException as e:
                print(e)
