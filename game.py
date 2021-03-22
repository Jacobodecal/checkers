import pygame,sys
from pygame.locals import *

#Initialize Program
pygame.init()

#Patterns for the Board
white,black,grey,blue = (255,255,255),(0,0,0),(100,100,100),(0,30,255)
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

#Creating Piece class
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
def transform_in_row_col(mouse_pos):
    row = int((int(mouse_pos[0]) / 50) + 1)
    col = int((int(mouse_pos[1]) / 50) + 1)
    return [row,col]


def clicked_piece(mouse_pos):
    pos = transform_in_row_col(mouse_pos)

    for piece in all_pieces:
        if(pos == transform_in_row_col([piece.x,piece.y])):
            return piece
    return None

def delete_eated_piece(pos_piece,mouse_pos,direction):

    eat_left = False
    if(mouse_pos[0] < pos_piece[0]):
        eat_left = True

    for piece in all_pieces:
        if(eat_left == True):
            if(piece.color == grey and transform_in_row_col([piece.x,piece.y]) == [pos_piece[0] + direction,pos_piece[1] + direction]):
                delete_piece(piece)
            elif(piece.color == blue and transform_in_row_col([piece.x,piece.y]) == [pos_piece[0] - direction,pos_piece[1] + direction]):
                delete_piece(piece)
        else:
            if(piece.color == blue and transform_in_row_col([piece.x,piece.y]) == [pos_piece[0] + direction,pos_piece[1] + direction]):
                delete_piece(piece)
            elif(piece.color == grey and transform_in_row_col([piece.x,piece.y]) == [pos_piece[0] - direction,pos_piece[1] + direction]):
                delete_piece(piece)

def delete_piece(piece):
    for i in range(len(all_pieces) - 1):
        if piece.x == all_pieces[i].x and piece.y == all_pieces[i].y:
            del all_pieces[i]
            break

def eat_piece_movement(pos_piece,mouse_pos,direction):

    valid_movement = False

    for piece in all_pieces:
        if(transform_in_row_col([piece.x,piece.y]) == [pos_piece[0] + direction , pos_piece[1] + direction] or transform_in_row_col([piece.x,piece.y]) == [pos_piece[0] + direction , pos_piece[1] - direction]):
            if(mouse_pos[1] == pos_piece[1] + 2* direction and (mouse_pos[0] == pos_piece[0] + 2*direction or mouse_pos[0] == pos_piece[0] - 2*direction)):
                valid_movement = True

    return valid_movement

def validate_move(pos_piece,mouse_pos,direction):

    mouse_pos = transform_in_row_col(mouse_pos)
    piece_pos = transform_in_row_col(pos_piece)
    print(mouse_pos)
    print(piece_pos)

    for piece in all_pieces:
        #Piece House
        if(mouse_pos == transform_in_row_col([piece.x,piece.y])):
            return False
    #Eat Piece Case
    if(eat_piece_movement(piece_pos,mouse_pos,direction) == True):
        delete_eated_piece(piece_pos,mouse_pos,direction)
        return mouse_pos
    #Diagonal movement online
    elif(mouse_pos[0] == piece_pos[0] or mouse_pos[0] < piece_pos[0] - 1 or mouse_pos[0] > piece_pos[0] + 1 or mouse_pos[1] > piece_pos[1] + 1 or mouse_pos[1] < piece_pos[1] - 1 or mouse_pos[1] == piece_pos[1]):
        return False
    #Direction of each piece
    elif((direction == up and mouse_pos[1] > piece_pos[1]) or (direction == down and mouse_pos[1] < piece_pos[1])):
        return False

    return mouse_pos    

def check_end_game():
    cnt_pieces_grey = 0
    cnt_pieces_blue = 0
    for piece in all_pieces:
        if(piece.color == grey):
            cnt_pieces_grey = cnt_pieces_grey + 1
        else:
            cnt_pieces_blue = cnt_pieces_blue + 1
    if cnt_pieces_blue == 0:
        return grey
    elif cnt_pieces_grey == 0:
        return blue
    else:
        return None

#Creating pieces and a vector with all pieces
all_pieces = []
for i in range(1,board_length + 1):
    for j in range(1, board_length + 1):
        if i % 2 == (j + 1) % 2:
            if j <= 3:
                Piece((i*50) - 25, (j*50) - 25, (100,100,100),False,down)
                all_pieces.append(Piece((i*50) - 25, (j*50) - 25, (100,100,100),False,down))
            elif j >5:
                Piece((i*50) - 25, (j*50) - 25, (0,30,255),False,up)
                all_pieces.append(Piece((i*50) - 25, (j*50) - 25, (0,30,255),False,up))

def draw_board_and_pieces():
    #board
    display.fill(white)
    cnt = 0
    for i in range(1,board_length+1):
        for j in range(1,board_length+1):
            if cnt % 2 != 0:
                pygame.draw.rect(display, black, [size_square*(j-1),size_square*(i-1),size_square,size_square])
            cnt +=1
        cnt-=1
    #pieces
    for piece in all_pieces:
        pygame.draw.circle(display, piece.color, (piece.x,piece.y), 15)
            

#Game Loop Begins
move_piece = False
while True:

    display.fill(black)
    draw_board_and_pieces()

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
            direction = piece.direction
            if validate_move(piece_pos,mouse_pos,direction) != False:
                piece.move(mouse_pos)
            move_piece = False

    #check end game
    if check_end_game() == blue or check_end_game() == grey:
        print("Player " + str(check_end_game()) + " won the game!!")

    pygame.display.update() 
      
                
                




    

        