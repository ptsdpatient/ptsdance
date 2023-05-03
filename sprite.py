import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((400,400))
Done = False
while not Done:
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
           Done=True
       if event.type==pygame.KEYDOWN:
           if event.key==K_SPACE:
               print("hello world")
           
       