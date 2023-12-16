from pygame import Surface, Color
from itertools import cycle

# rgb colours
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
RED, GREEN, BLUE = (255, 0, 0), (0, 255, 0), (0, 0, 255)
YELLOW, CYAN, MAGENTA, PURPLE = (255, 255, 50), (255, 50, 255), (50, 255, 255), (95, 0, 160)
COLOUR_LIST = (RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, PURPLE)
COLOURS = cycle(COLOUR_LIST)

WORLD_SIZE = 500
TILE_SIZE = 50
OFFSET = TILE_SIZE / 2
TILES = int(WORLD_SIZE / TILE_SIZE)
BLUE_IMAGE = Surface((TILE_SIZE,TILE_SIZE))
BLUE_IMAGE.fill(Color('lightskyblue2'))
GRAY_IMAGE = Surface((TILE_SIZE,TILE_SIZE))
GRAY_IMAGE.fill(Color('slategray4'))

GAME_SPEED = 60 # fps
GAME_TICK = 1/GAME_SPEED