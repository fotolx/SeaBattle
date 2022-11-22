import random as rnd
from gameBoard import GameBoard
from ships import Ship
from dot import Dot
from user import User
from ai import AI
from gameExceptions import *
from colorama import Back


class Game:
    def __init__(self, size=6, hide=True):
        rnd.seed()
        self.size = size
        self.hide = hide
        self.autoplay = False
        self.ships_lenghts = [3, 2, 2, 1, 1, 1, 1]
        # print("Generating player board...")
        self.user_board = self.random_board()
        # print("Generating AI board...")
        self.ai_board = self.random_board()

    def create_board(self):
        game_board = GameBoard(size=self.size, ships_count=len(self.ships_lenghts))
        attempts = 0
        for ship_length in self.ships_lenghts:
            while True:
                attempts += 1
                if attempts > 1000:
                    return None
                ship = Ship(ship_length, Dot(rnd.randint(0, self.size), rnd.randint(0, self.size)), rnd.randint(0, 1))
                if game_board.add_ship(ship) == "Wrong":
                    continue
                else:
                    break
        game_board.reset_busy()
        return game_board

    def random_board(self):
        game_board = None
        while game_board is None:
            game_board = self.create_board()
        return game_board

    def greet(self):
        print("╔", "="*27, "╗", sep="")
        print("║   ",Back.BLUE +" \u26F5 "+Back.RESET," WELCOME ",Back.BLUE +" \u26F5 "+Back.RESET,"   ║")
        print("║          to  the          ║")
        print("║ ", Back.BLUE +"-=[ Sea Battle Game ]=-"+Back.RESET," ║")
        print("║            v1.0           ║")
        print("╚", "=" * 27, "╝"+Fore.RESET, sep="")
        print("You are playing against computer.")
        print("You need to destroy all enemy ships first.")
        print("To shoot enter coords separated by space.")
        print("Like this: x y")
        print("x - is the row, y - is the column.")
        self.ask_settings()

    def ask_settings(self):
        auto = input('\nYou can play by yourself or try autoplay.\nWhat do you prefer? (a - auto, anything other is '
                     'play by yourself): ')
        if auto == 'a':
            self.autoplay = True
        return


    def loop(self):
        if self.autoplay:
            self.user = AI(self.user_board, self.ai_board, 'User')
        else:
            self.user = User(self.user_board, self.ai_board)
        self.ai = AI(self.ai_board, self.user_board)
        players_move = True
        print("\n",Back.GREEN +"Game started"+Back.RESET)
        while True:
            if not self.user.board.alive_ships:
                self.show_boards()
                raise BoardAiWinsException
            if not self.ai.board.alive_ships:
                self.show_boards()
                raise BoardPlayerWinsException
            self.show_boards()
            if players_move:
                print(Fore.GREEN + "\nUser's move" + Fore.RESET)
                move = self.user.move()
            else:
                print(Fore.LIGHTBLUE_EX + "\nAI's move" + Fore.RESET)
                move = self.ai.move()
            if not move:
                players_move = not players_move

    def show_boards(self):
        print(Fore.GREEN + "\nUser's board", "(" + str(self.user.board.alive_ships), "ships alive)" + Fore.RESET)
        self.user_board.show()
        print(Fore.LIGHTBLUE_EX + "\nAI's board", "(" + str(self.ai.board.alive_ships), "ships alive)" + Fore.RESET)
        self.ai_board.show(self.hide)

    def start(self):
        self.greet()
        self.loop()
