from pygame import display, event, time, font, draw, quit, MOUSEBUTTONDOWN, QUIT, KEYDOWN, K_SPACE
from constants import OFFSET, TILE_SIZE, COLOURS, BLACK, COLOUR_LIST
from setup import make_background, add_snakes_and_ladders, add_players
from random import randint
from math import floor, ceil

class MyGame:
    def __init__(self):
        width = 700
        height = 600
        self.game_window = display.set_mode((width, height))
        display.set_caption("Sankes and Ladders")
        self.clock = time.Clock()

    def reset(self):
        self.game_window.fill(BLACK)
        self.background = make_background()
        self.snakes_and_ladders = add_snakes_and_ladders(self.background)
        self.players = add_players()
        self.player_turn = 0

    def redraw_window(self):
        # background first
        self.game_window.blit(self.background, (OFFSET, OFFSET))
        self.draw_players()
        display.update()

    def draw_players(self):
        for i in self.players:
            player = self.players[i]
            self.game_window.blit(
                player["image"], 
                ((player["pos"][0] * TILE_SIZE) + player["offset"][0], 
                 (player["pos"][1] * TILE_SIZE) + player["offset"][1])
            )
    
    def roll_dice(self):
        display_font = font.SysFont("arial", 80)
        for _ in range(20):
            colour = next(COLOURS)
            moves = randint(1, 6)
            draw.rect(self.game_window, BLACK, (550, 50, 200, 200))
            text_surface = display_font.render(str(moves), True, colour)
            self.game_window.blit(self.background, (OFFSET, OFFSET))
            self.game_window.blit(text_surface, (600, 100))
            self.draw_players()
            display.update()
            self.clock.tick(10)
        colour = COLOUR_LIST[self.player_turn + 2]
        moves = randint(1, 6)
        draw.rect(self.game_window, BLACK, (550, 50, 200, 200))
        text_surface = display_font.render(str(moves), True, colour)
        self.game_window.blit(self.background, (OFFSET, OFFSET))
        self.game_window.blit(text_surface, (600, 100))
        self.draw_players()
        display.update()
        return moves

    def move_player(self, moves):
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
                self.game_over()
                self.reset()
                return
            self.clock.tick(4)
            self.redraw_window()
        self.check_extra_moves()
        self.player_turn += 1
        if self.player_turn == 4:
            self.player_turn = 0
        event.clear()

    def game_over(self):
        self.game_window.fill(BLACK)
        txt_font = font.SysFont('ariel', 100)
        text_surface = txt_font.render('Winner is', True, COLOUR_LIST[self.player_turn + 2])
        self.game_window.blit(text_surface, (200,200))
        text_surface = txt_font.render('Player', True, COLOUR_LIST[self.player_turn + 2])
        self.game_window.blit(text_surface, (200,300))
        text_surface = txt_font.render(str(self.player_turn + 1), True, COLOUR_LIST[self.player_turn + 2])
        self.game_window.blit(text_surface, (450,300))
        txt_font = font.SysFont('ariel', 50)
        text_surface = txt_font.render(str('Press Space to play again'), True, COLOUR_LIST[self.player_turn + 2])
        self.game_window.blit(text_surface, (150,450))
        display.update()
        event.clear()
        while True:
            for item in event.get():
                if item.type == QUIT:
                    quit()
                    raise SystemExit()
                elif item.type == KEYDOWN and item.key == K_SPACE:
                    self.reset()
                    return
                
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
                new_col = round(self.players[self.player_turn]["pos"][0], 0)
                new_row = round(self.players[self.player_turn]["pos"][1], 0)
                self.players[self.player_turn]["pos"] = [new_col, new_row]
                return

    def main(self):
        run = True
        self.reset()
        self.redraw_window()
        while run:
            for item in event.get():
                if item.type == QUIT:
                    run = False
                    quit()
                    raise SystemExit()
                elif item.type == KEYDOWN and item.key == K_SPACE:
                    moves = self.roll_dice()
                    self.move_player(moves)
            moves = self.roll_dice()
            self.move_player(moves)

if __name__ == '__main__':
    my_game = MyGame()
    my_game.main()