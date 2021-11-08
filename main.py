import pygame
from constants import WIDTH, HEIGHT
from board import Board


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def main():
    run = True
    clock = pygame.time.Clock()

    # Call checkersGame
    
    board = Board()


    while run:
        clock.tick(FPS)
        pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw(WIN)
        pygame.display.update()

    pygame.quit()


main()