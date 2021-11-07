import pygame
from constants import WHITE, ROWS, RED, GREY, SQUARE_SIZE

class Board:
    def __init__(self):
        self.board = []
        self.turn = 0
        self.selected_piece = None
        self.red_left = 12
        self.white_left = 12
        self.red_kings = 0
        self.white_kings = 0

    def draw_squares(self, win):
        win.fill(GREY) #FILL BOARD WITH BLACK
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


    def create_board(self):
        pass