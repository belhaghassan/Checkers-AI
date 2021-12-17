import pygame
from checkersGame import *
from constants import *
from algorithmAI import *


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == RED:
            value, new_board = minimax(game.get_board(), 3, RED, game)
            game.ai_move(new_board)

        
        if game.winner() != None:
            print(game.winner())
            run = False
        

        #Trying to change the method so that it would check if the pieces = to 0 then run the game.winner() command but seems to be having issues
        '''
        if game.terminate() != None:
            print(game.winner())
            run = False
        '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

main()