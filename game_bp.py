#game initialization

import pygame, random,sys
from pygame.locals import *
pygame.init()
resolution=[400,400]
game_icon=pygame.image.load("src/game_icon/dance.png")
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("ptsdance")
pygame.display.set_icon(game_icon)
gameOver = True
bg_color = (31, 35, 43)

#game settings

key_row=[0]*4
print(key_row)

while not gameOver:
    for event in pygame.event.get(): 
        
               
        if event.type==pygame.QUIT:
            gameOver=True
    screen.fill(bg_color)  
    dust=pygame.image.load("src/game_files/dus.png")
    rect1=dust.get_rect()
    rect1.center=200,0
    screen.blit(dust,rect1)
    pygame.display.update()  
                

            
        
