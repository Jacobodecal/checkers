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
        if cnt % 2 == 0:
            pygame.draw.rect(display, white, [size_square*(j-1),size_square*(i-1),size_square,size_square])
        else:
            pygame.draw.rect(display, black, [size_square*(j-1),size_square*(i-1),size_square,size_square])
        cnt +=1
    cnt-=1

#Game Loop Begins
while True:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        