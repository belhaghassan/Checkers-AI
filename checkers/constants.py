import pygame

# Declare Constants for GameBoard and Game Pieces
# ***********************************************
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

RED = (255, 0, 0)
GREY = (105,105,105)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0,0,255)


CROWN = pygame.transform.scale(pygame.image.load('Checkers_AI/assets/king.png'), (44, 25))
#************************************************
