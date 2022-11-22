from player import Player
from dot import Dot
import random as rnd


class AI(Player):

    def __init__(self, player_board, enemy_board, name = 'AI'):
        super().__init__(player_board, enemy_board)
        self.name = name

    def ask(self):
        while True:
            cell = Dot(rnd.randint(0, self.size - 1), rnd.randint(0, self.size - 1))
            if cell not in self.enemy_board.busy_list:
                print(f"{self.name}'s move", cell.coord_x+1, cell.coord_y+1)
                return cell
