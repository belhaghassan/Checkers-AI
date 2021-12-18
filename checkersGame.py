import pygame
import time
import _thread
from constants import *
from piece import * 
from algorithmAI import * 



#game state of the board itself 
#the game should have something itself
#checklist of functions that need to do this 
# Move pieces - check
# Check to see if piece is a valid move 
# by valid, if a jump is made there shouldn't be any piece on the jumpzone itself 
# also check that it doesn't go out of bounds 
# since we have to do a cutoff, implement a time limit of 10-15 seconds for each move (gotta go fast) 
# Alpha Beta cut off (specify a depth limit) 
# gonna ignore the games.py 
# PEACE AND SERENITY 


# Main Game Logic 
class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        #self.lock = _thread.allocate_lock()
        #self.difficulty = difficulty
        #self.AIPlayer = AIPlayer(self, self.difficulty)


    def getDiff(self):
        answer = eval(input("(1 for easy, 2 for hard) Difficulty Level: "))
        while not (answer == 1 or answer == 2):
            print ("Invalid inpurt, please enter 1 or 2")
            answer = eval(input("(1 for easy, 2 for hard) Difficulty Level: "))
        return answer 


    #UPDATE THE BOARD WITH OUR DUMB MOVES AAAAAAAAAAAAAAAAA
    def update(self):
        self.board.draw(self.win)
        self.get_valid_moves(self.valid_moves)
        pygame.display.update()

    #we go first because we're god
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        #empty list
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def terminate(self):
        return self.board.terminate()

    #reset the game once we're done
    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def get_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREEN, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = BLACK
        else:
            self.turn = RED
       
        

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()


#This is where the fun begins 
class Board:
    def __init__(self):

        #initalizing the board mechanics 
        self.board = []
        self.turn = 0
        self.selected_piece = None
        self.red_left = (ROWS // 2 -1) * (COLS // 2) 
        self.black_left = (ROWS // 2 -1) * (COLS // 2) 
        self.red_kings = 0
        self.black_kings = 0
        self.make_board()

        
        #just for message purposes 
        self.message = False

    #this creates the board
    #Changing from 8x8 to 6x6 for simplicity sake we can expand to other sizes if we need to in the future.  
    def make_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < ROWS//2 - 1:
                        self.board[row].append(Piece(row,col,RED))
                    elif row > ROWS//2:
                        self.board[row].append(Piece(row,col,BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    #draw the squares 
    def draw_squares(self, win):
        #draw the squares and fill the portion of the thing with black 
        win.fill(GREY) #FILL BOARD WITH GRAY COLOR AND THEN REPLACE WITH WHITE~~~~~ AAAAAAAAAAAAAAAAAAAAAAAAAA
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                #fill in squares with WHITE color 
                pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


    #Get the current number of pieces left 
    def evaluate(self):
        regPieces = self.black_left - self.red_left
        kingPieces = ((self.black_kings * 0.5) - (self.red_kings * 0.5)) 
        total = regPieces + kingPieces
        return total

    #get a list of pieces cause we're dumb~~~~~
    #HASHIRE SORE YO KAZE NO YO NII TSUKIMIHARA WO PADORU PADORU 
    def get_all_pieces(self, color):
        #list
        pieces = []
        #
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    #Move piece 
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        #if pieces reach the end on that turn then become da king 
        if row == ROWS - 1 or row == 0:
            if piece.color == BLACK:
                piece.make_king()
                self.black_kings += 1
            else:
                piece.make_king()
                self.red_kings += 1 

    #Draw *bang*
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    #YOUR USEFULNESS IS OUTLIVED NOW PERISH 
    #Reverse Uno Card because somehow the logic has changed????????
    def remove(self, pieces): 
        for piece in pieces: 
            self.board[piece.row][piece.col] = 0 
            if piece.color == RED:
                self.black_left -= 1
            else:
                self.red_left -= 1



    #winner winner chicken dinner
    #gotta figure out 
    def winner(self):
        if self.red_left == 0:
            # print("Red Wins")
            return "Red wins" 
        elif self.black_left == 0:
            # print("Black wins")
            return "Black Wins"
        else:
            return None 

    '''
    def terminate(self):
        if self.red_left == 0:
            self.winner()
        elif self.black_left == 0:
            self.winner()
        else:
            return None
    '''

    def get_piece(self, row, col):
        singlePiece = self.board[row][col]
        return singlePiece

    #This might have to be changed to match a 6 x 6 board 
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1 
        right = piece.col + 1 
        row = piece.row 

        #update red or black piece 

        if piece.king:
            #looking down the rows
            moves.update(self.move_piece_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self.move_piece_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
            #looking up the rows 
            moves.update(self.move_piece_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self.move_piece_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        #if the piece isn't a king then just find out if it's black or red and give it's normal rows 
        elif piece.color == BLACK:
            moves.update(self.move_piece_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self.move_piece_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        elif piece.color == RED:
            moves.update(self.move_piece_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self.move_piece_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
            

        return moves 

    #SHIMMY UP LEFT OR RIGHT 
    def move_piece_left(self, start, stop, step, color, left, skipped=[]):
        #dict of moves
        moves = {}
        #list of last moves 
        last = []
        #if there is no space left in the left side then break 
        #r = row 
        for r in range(start, stop, step):
            #if we look outside the board, then break 
            if left < 0:
                break
            
            #
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self.move_piece_left(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self.move_piece_right(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    #step do i go up or down 
    #skipped will tell us have we skipped any pieces, we can only move to 
    def move_piece_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self.move_piece_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self.move_piece_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves