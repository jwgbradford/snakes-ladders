from pygame import display, event, MOUSEBUTTONDOWN, quit, QUIT, time
from constants import OFFSET, TILE_SIZE
from setup import make_background, add_snakes_and_ladders, add_players
from random import randint
from math import floor

class MyGame:
    def __init__(self):
        width = 700
        height = 600
        self.game_window = display.set_mode((width, height))
        display.set_caption("Sankes and Ladders")
        self.background = make_background()
        self.snakes_and_ladders = add_snakes_and_ladders(self.background)
        self.players = add_players()
        self.player_turn = 0
        self.clock = time.Clock()

    def redraw_window(self):
        # background first
        self.game_window.blit(self.background, (OFFSET, OFFSET))
        for i in self.players:
            player = self.players[i]
            self.game_window.blit(
                player["image"], 
                ((player["pos"][0] * TILE_SIZE) + player["offset"][0], 
                 (player["pos"][1] * TILE_SIZE) + player["offset"][1])
            )
        display.update()

    def roll_dice(self):
        moves = randint(1, 6)
        for _ in range(moves):
            if self.players[self.player_turn]["pos"][1] % 2 > 0:
                if self.players[self.player_turn]["pos"][0] == 9:
                    self.players[self.player_turn]["pos"][1] -= 1
                else:
                    self.players[self.player_turn]["pos"][0] += 1
            else:
                if self.players[self.player_turn]["pos"][0] == 0:
                    self.players[self.player_turn]["pos"][1] -= 1
                else:
                    self.players[self.player_turn]["pos"][0] -= 1
            if self.players[self.player_turn]["pos"] == [0, 0]:
                print("winner")
                raise SystemExit()
            self.clock.tick(4)
            self.redraw_window()
        self.check_extra_moves()
        self.player_turn += 1
        if self.player_turn == 4:
            self.player_turn = 0
        event.clear()

    def check_extra_moves(self):
        current_pos = self.players[self.player_turn]["pos"]
        steps = 120
        for snadder in self.snakes_and_ladders:
            if snadder[0] == current_pos:
                d_col = (snadder[1][0] - current_pos[0]) / steps
                d_row = (snadder[1][1] - current_pos[1]) / steps
                for _ in range(steps):
                    self.players[self.player_turn]["pos"][0] += d_col
                    self.players[self.player_turn]["pos"][1] += d_row
                    self.redraw_window()
                    self.clock.tick(60)
                # going up / down - sometimes skips cells on exit...
                new_col = floor(self.players[self.player_turn]["pos"][0])
                new_row = floor(self.players[self.player_turn]["pos"][1])
                self.players[self.player_turn]["pos"] = [new_col, new_row]
                return

    def main(self):
        run = True
        self.redraw_window()
        while run:
            for item in event.get():
                if item.type == QUIT:
                    run = False
                    quit()
                    raise SystemExit()
                elif item.type == MOUSEBUTTONDOWN:
                    pass
            self.roll_dice()

if __name__ == '__main__':
    my_game = MyGame()
    my_game.main()