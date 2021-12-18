import pygame
from checkers.checkersGame import CheckersGame
from checkers.constants import SQUARE_SIZE, WIDTH, HEIGHT



FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = CheckersGame(WIN)
    # Call checkersGame

    while run:
        clock.tick(FPS)
        
        if game.turn == RED:
            value, new_board = minimax(game.get_board(), 4, RED, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

        game.update()
    
    pygame.quit()

main()