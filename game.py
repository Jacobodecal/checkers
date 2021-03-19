import pygame,sys
from pygame.locals import *

#Initialize Program
pygame.init()

#Patterns for the Board
white,black = (255,255,255),(0,0,0)
size_square = 50
board_length = 8
up = -1
down = 1

#Creating Draught-Board(8x8)
display = pygame.display.set_mode((size_square*board_length,size_square*board_length))
display.fill(white)
cnt = 0
for i in range(1,board_length+1):
    for j in range(1,board_length+1):
        if cnt % 2 != 0:
            pygame.draw.rect(display, black, [size_square*(j-1),size_square*(i-1),size_square,size_square])
        cnt +=1
    cnt-=1

#Creating Piece
class Piece():

    def __init__(self,x,y,color,king,direction):
        self.x = x
        self.y = y
        self.king = king
        self.color = color
        self.image = pygame.draw.circle(display,color,(x,y),15)
        self.direction = direction

    def move(self,mouse_pos):
        self.x = mouse_pos[0]
        self.y = mouse_pos[1]
        self.image = pygame.draw.circle(display,self.color,(self.x,self.y),15)
        

#Help Functions
def transform_pos_row_col(mouse_pos):
    row = int((int(mouse_pos[0]) / 50) + 1)
    col = int((int(mouse_pos[1]) / 50) + 1)
    return [row,col]


def clicked_piece(mouse_pos):
    pos = transform_pos_row_col(mouse_pos)

    for piece in all_pieces:
        if(pos == transform_pos_row_col([piece.x,piece.y])):
            return piece
    return None

def validate_move(pos_piece,mouse_pos):

    mouse_pos = transform_pos_row_col(mouse_pos)
    piece_pos = transform_pos_row_col(pos_piece)
    print(mouse_pos)
    print(piece_pos)

    for piece in all_pieces:
        if(mouse_pos == transform_pos_row_col([piece.x,piece.y])):
            return False
        elif(mouse_pos[0] == piece_pos[0] or mouse_pos[0] < piece_pos[0] - 1 or mouse_pos[0] > piece_pos[0] + 1 or mouse_pos[1] > piece_pos[1] + 1 or mouse_pos[1] < piece_pos[1] - 1 or mouse_pos[1] == piece_pos[1]):
            return False
    return mouse_pos    


#Putting Pieces on the Board
all_pieces = []
for i in range(1,board_length+1):
    for j in range(1,board_length+1):
        if i % 2 == (j + 1) % 2:
            if j <= 3:
                Piece((i*50) - 25, (j*50) - 25, (100,100,100),False,down)
                all_pieces.append(Piece((i*50) - 25, (j*50) - 25, (100,100,100),False,down))
            elif j >5:
                Piece((i*50) - 25, (j*50) - 25, (0,30,255),False,up)
                all_pieces.append(Piece((i*50) - 25, (j*50) - 25, (0,30,255),False,up))
            

#Game Loop Begins
move_piece = False
while True:


    for event in pygame.event.get():
        #QUIT
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #Piece Choice
        elif event.type == MOUSEBUTTONDOWN and move_piece == False:
            piece_pos = pygame.mouse.get_pos()
            if clicked_piece(piece_pos) == None:
                print("Click a Piece")
            else:
                piece = clicked_piece(piece_pos)
                move_piece = True
                print("Move Piece to a Validate House")
        #Move Piece
        elif event.type == MOUSEBUTTONDOWN and move_piece == True:
            mouse_pos = pygame.mouse.get_pos()
            if validate_move(piece_pos,mouse_pos) != False:
                piece.move(mouse_pos)
            move_piece = False
    pygame.display.update() 
      
                
                




    

        