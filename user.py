from player import Player
from dot import Dot
from gameExceptions import *
from colorama import Fore


class User(Player):

    def ask(self):
        try:
            x, y = map(int, input('Your move, enter coordinates separated by a space:').split())
        except ValueError:
            print(Fore.RED+"Wrong input!"+Fore.RESET)
            raise BoardException
        else:
            if 0 < x < self.size+1 and 0 < y < self.size+1:
                cell = Dot(x-1, y-1)
                print("User's move", cell.coord_x + 1, cell.coord_y + 1)
                return cell
            else:
                raise BoardOutException
