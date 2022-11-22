from copy import deepcopy
from dot import Dot
from colorama import Back
from gameExceptions import *


class GameBoard:
    def __init__(self, size=6, hide=False, ships_count=7):
        # init()
        self.ship_marker = "■"
        self.marker_miss = "X"
        self.marker = "※"
        self.empty_dot = '‧'
        self.busy_dot = '#'
        self.ship_shot = '⊠'
        self.size = size
        self.board = [[self.empty_dot] * self.size for _ in range(self.size)]
        self.ships_list = []
        self.busy_list = []
        self.hide = hide
        self.alive_ships = ships_count

    def add_ship(self, ship):
        for dot in ship.dots:
            if self.out(dot) or dot in self.busy_list:
                return "Wrong"
        for dot in ship.dots:
            self.board[dot.coord_x][dot.coord_y] = self.ship_marker
            self.busy_list.append(dot)
        self.ships_list.append(ship)
        self.contour(ship)

    def contour(self, ship, show=False):
        for dot in ship.dots:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    cell = Dot(dot.coord_x + dx, dot.coord_y + dy)
                    if not (self.out(cell)) and cell not in self.busy_list:
                        self.busy_list.append(cell)
                        if show:
                            self.board[cell.coord_x][cell.coord_y] = self.busy_dot

    def show(self, hide=False):
        nums = list(map(str, range(1, self.size + 1)))
        nums.insert(0, ' ')
        print(Fore.RED + "|".join(nums) + '|' + Fore.RESET)

        r = iter(range(1, self.size + 1))
        field_ = deepcopy(self.board)
        if hide:
            field_ = [[p if p == self.marker_miss or p == self.ship_shot else 'o' for p in f] for f in field_]
        list(map(lambda x: x.insert(0, str(next(r))), field_))
        print(Fore.RED, end="")
        print("\u2502\n\033[31m".join(list(map(lambda x: "\033[39m\u2502".join(x), field_))) + '\u2502')

    def out(self, dot):
        return not ((0 <= dot.coord_x < self.size) and (0 <= dot.coord_y < self.size))
        pass

    def shot(self, dot):
        if self.out(dot):
            raise BoardOutException
        if dot in self.busy_list:
            raise BoardAlreadyFiredException

        self.busy_list.append(dot)
        for ship in self.ships_list:
            if dot in ship.dots:
                ship.lives -= 1
                self.board[dot.coord_x][dot.coord_y] = self.ship_shot
                if ship.lives == 0:
                    self.alive_ships -= 1
                    self.contour(ship, True)
                    print(Back.GREEN+'The ship is destroyed \u2694'+Back.RESET)
                    return False
                else:
                    print(Back.GREEN+'The ship is hit \u26F5'+Back.RESET)
                    return True
        self.board[dot.coord_x][dot.coord_y] = self.marker_miss
        print(Back.RED+'Miss'+Back.RESET)
        return False

    def reset_busy(self):
        self.busy_list = []
