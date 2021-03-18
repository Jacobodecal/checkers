import pygame,sys
from pygame.locals import *

#Initialize Program
pygame.init()

#Patterns for the Board
white,black = (255,255,255),(0,0,0)
size_square = 50
board_length = 8

#Creating Draught-Board(8x8)
display = pygame.display.set_mode((size_square*board_length,size_square*board_length))
display.fill(white)
cnt = 0
for i in range(1,board_length+1):
    for j in range(1,board_length+1):
        if cnt % 2 != 0:
            pygame.draw.rect(display, black, [size_square*(j-1),size_square*(i-1),size_square,size_square])
        #else:
            #pygame.draw.rect(display, black, [size_square*(j-1),size_square*(i-1),size_square,size_square])
        cnt +=1
    cnt-=1

#Creating Piece
class Piece:

    def __init__(self,x,y,color):
        self.image = pygame.draw.circle(display,color,(x,y),15)
    
    def move(self,x,y):
        self.x = x
        self.y = y


#Putting Pieces on the Board
for i in range(1,board_length+1):
    for j in range(1,board_length+1):
        if i % 2 == (j + 1) % 2:
            if j <= 3:
                Piece((i*50) - 25, (j*50) - 25, (100,100,100))
            elif j >5:
                Piece((i*50) - 25, (j*50) - 25, (0,30,255))
#Game Loop Begins
while True:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            print("Mecheu")
    

        