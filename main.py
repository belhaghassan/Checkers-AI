import pygame
import tkinter as tk
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

#Gets the difficulty level (i.e. the depth level for the ai to search through)
#Having tested, the AI will whoop my butt at 4
def getDiff():
    answer = eval(input("This changes the depth level search (1 (easy) - 4 (hard)) Difficulty Level: "))
    while not (answer == 1 or answer == 2 or answer == 3 or answer == 4):
        print ("Invalid input, please enter a number from 1-4")
        answer = eval(input("1 (Easy) - 4 (hard) Difficulty Level: "))
    return answer 

def tkinterDiff():
    root = tk.Tk()

    v = tk.IntVar()
    v.set(1) #Initializes the choice, i.e. Python 

    choices = [ ("1. Easy", 1),
                ("2. Semi-Easy", 2),
                ("3. Normal", 3),
                ("4. Hard", 4)]

   

    tk.Label(root, text="""Choose your Difficulty Level:""",
            justify = tk.LEFT,
            padx = 20).pack()

    for choice, val in choices:
        tk.Radiobutton(root,
                       text=choice,
                       variable=v,
                       value=val).pack(anchor=tk.W)
    root.mainloop()
    return v.get()

    

def main():

    #depth = getDiff()
    depth = tkinterDiff()
    print("Difficulty: ", depth)

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)


    while run:
        clock.tick(FPS)
        
        if game.turn == RED:
            value, new_board = minimax(game.get_board(), depth, RED, game)
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