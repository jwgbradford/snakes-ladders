from pygame import font, Surface, draw, init
from constants import COLOUR_LIST, BLUE_IMAGE, GRAY_IMAGE, WORLD_SIZE, TILES, TILE_SIZE
from itertools import cycle
from random import randrange

init()

def make_background(): # this function creates a single image background
    # set up a simple list of images that we can iterate through
    images = cycle((BLUE_IMAGE, GRAY_IMAGE))
    background = Surface((WORLD_SIZE, WORLD_SIZE))
    tile_number = 100
    tile_inc = -1
    # Use two nested for loops to get the coordinates.
    for row in range(TILES):
        for column in range(TILES):
            # alternate between the blue and gray image.
            image = next(images)
            # Blit one image after the other at their respective coords
            background.blit(
                image, 
                ((column * TILE_SIZE), 
                    (row * TILE_SIZE))
                )
            # create number images
            number_image = text_to_image(str(tile_number))
            tile_number += tile_inc
            # add to background (if we add to the tile, we end up overwriting)
            background.blit(
                number_image, 
                ((column * TILE_SIZE) + 5, 
                    (row * TILE_SIZE) + 5)
                )
        image = next(images) # set the first tile image
        tile_inc *= -1 # reverse numbering direction
        tile_number -= TILES
        tile_number += tile_inc
    return background

def add_snakes_and_ladders(background):
    # make an empty dictionary for our snakes & ladders lists
    snakes_and_ladders = []
    for _ in range(3):
        snakes_and_ladders.append(make_snake_ladder(background, COLOUR_LIST[0]))
        snakes_and_ladders.append(make_snake_ladder(background, COLOUR_LIST[1]))
    #returns a surface, and dictionary of snakes & ladders
    return snakes_and_ladders

def text_to_image(text):
    display_font = font.SysFont("arial", 20)
    text_surface = display_font.render(text, True, COLOUR_LIST[6])
    return text_surface

def make_snake_ladder(background, colour):
    start_col = randrange(0, TILES - 1, 1)
    start_row = randrange(0, TILES - 1, 1)
    end_col = randrange(0, TILES - 1, 1)
    end_row = randrange(0, TILES - 1, 1)
    # prevent start / end on same row (flat ladder)
    while start_row == end_row:
        end_row = randrange(1, TILES, 1)
    start_pos = ((start_col * TILE_SIZE) + TILE_SIZE / 2, (start_row * TILE_SIZE) + TILE_SIZE / 2)
    end_pos = ((end_col * TILE_SIZE) + TILE_SIZE / 2, (end_row * TILE_SIZE) + TILE_SIZE / 2)
    draw.line(background, colour, start_pos, end_pos, width=10)
    line_coords = []
    # rememeber our playing board starts (0,0) top left, but we start playing (0, 0) bottom left
    if (
        (colour == COLOUR_LIST[0] and start_row < end_row) or # snakes go down
        (colour == COLOUR_LIST[1] and start_row > end_row) # ladders go up
        ) :
        line_coords = [[start_col, start_row], [end_col, end_row]]
    else:
        line_coords = [[end_col, end_row], [start_col, start_row]]
    return line_coords

def add_players():
    offset_size = TILE_SIZE / 4
    offset_pattern = [(2, 2), (2, 4), (4, 2), (4, 4)]
    player_dict = {}
    for player in range(4):
        player_dict[player] = {
            "offset" : (offset_size * offset_pattern[player][0], offset_size * offset_pattern[player][1]),
            "pos" : [0, 9],
            "image" : make_player(player)
        }
    return player_dict

def make_player(player_number):
    player_size = TILE_SIZE / 2
    player_image = Surface((player_size, player_size))
    player_image.set_colorkey((0,0,0))
    draw.circle(
                player_image, 
                COLOUR_LIST[player_number + 2], 
                (player_size / 2 , player_size / 2), 
                player_size / 2, 
                0
    )
    return player_image