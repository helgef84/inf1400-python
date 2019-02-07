'''
	This file contains all variables used by the game.
	To change a variable (i.e. screen dimensions),  it only needs to change in this file
	to affect all functions in the program using it
'''

# SCREEN VARIABLES
WIDTH = 900
HEIGHT = 600 

'''
	Divide the surface into a grid, one brick will fit into one grid frame.
'''
GRID_SIZE_X = int(WIDTH / 15)
GRID_SIZE_Y = int(HEIGHT / 15)

FPS = 60


# COLORS

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (35, 35, 35)

# TEXTBOX 

#COLOR_INACTIVE = (204, 253, 252)
#COLOR_ACTIVE = (9, 204, 199)

# PLAYER VARIABLES

PLAYER_WIDTH = 100
PLAYER_HEIGHT = 20
PLAYER_SIZE = (PLAYER_WIDTH, PLAYER_HEIGHT)
PLAYER_POS_X = int(WIDTH / 2)
PLAYER_POS_Y = HEIGHT - PLAYER_HEIGHT
PLAYER_SPEED = 10

# BALL VARIABLES
BALL_WIDTH = 20
BALL_HEIGHT = 20
BALL_RADIUS = 10
BALL_SIZE = (BALL_WIDTH, BALL_HEIGHT)
BALL_SPEED = 8

# MAPS

LEVELS = ["levels/level1.txt", "levels/level2.txt", "levels/level3.txt", "levels/level4.txt" ,"levels/level5.txt"]

