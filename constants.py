import pygame

# Declare Constants for GameBoard and Game Pieces
# ***********************************************

ROWS, COLS = 6, 6
WIDTH, HEIGHT = ROWS*100, COLS*100
SQUARE_SIZE = WIDTH//COLS

RED = (255, 0, 0)
GREY = (105,105,105)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
GREEN = (0,255,0)
#************************************************

# Directions if i can implement it
# keep it there in the event we can try to change the piece location i suppose lol 
# ***********************************************
NORTHWEST = "northwest"
NORTHEAST = "northeast"
SOUTHWEST = "southwest"
SOUTHEAST = "southeast"
#************************************************

# The stupid crown 
# ***********************************************
BeegCrown = pygame.image.load('resources/crown.png')
CROWN = pygame.transform.scale(BeegCrown, (30, 30))
# ***********************************************