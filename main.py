import pygame,random,sys
from pygame.locals import *
pygame.init()
resolution=[800,500]
screen=pygame.display.set_mode(resolution)
pygame.display.set_caption("arrows")
Done=False
gameSpeed=15
arrowList=pygame.sprite.Group()
recieveList=pygame.sprite.Group()
highlightList=pygame.sprite.Group()
gameScore=0
arrowBlink=[pygame.image.load("src/game_files/game_objects/arrow_light_4.png"),pygame.image.load("src/game_files/game_objects/arrow_light_3.png"),pygame.image.load("src/game_files/game_objects/arrow_light_2.png"),pygame.image.load("src/game_files/game_objects/arrow_light_1.png"),pygame.image.load("src/game_files/game_objects/arrow_light_0.png")]
class spawnCollector(pygame.sprite.Sprite):
    def __init__(self,rotation):
         super().__init__()
         self.image=pygame.image.load("src/game_files/game_objects/collector.png")
         self.image=pygame.transform.rotate(self.image,rotation)
         self.image=pygame.transform.smoothscale(self.image,(80,80))
         self.rect=self.image.get_rect()
         self.rect.center=rotation+50,80
         screen.blit(self.image,self.rect)
         print(self.rect.x)
    def update(self):
         key=pygame.key.get_pressed()
         if key[pygame.K_LEFT] and self.rect.x==10:
             self.rect.x=5    
         if key[pygame.K_DOWN] and self.rect.x==100:
             self.rect.y=45
         if key[pygame.K_RIGHT] and self.rect.x==190:
             self.rect.x=195    
         if key[pygame.K_UP] and self.rect.x==280:
             self.rect.y=35

         if self.rect.x==5 and not key[pygame.K_LEFT]:
             self.rect.x=10
         if self.rect.x==100 and not key[pygame.K_DOWN]:
             self.rect.y=40
         if self.rect.x==195 and not key[pygame.K_RIGHT]:
             self.rect.x=190
         if self.rect.x==280 and not key[pygame.K_UP]:
             self.rect.y=40
          
class spawnArrow(pygame.sprite.Sprite):
    def __init__(self,color,rotation):
        super().__init__()
        arrowName="arrow_"+color+".png"
        self.image=pygame.image.load("src/game_files/game_objects/" + arrowName)
        self.image=pygame.transform.smoothscale(self.image,(70,70))
        self.image=pygame.transform.rotate(self.image,rotation+90)
        self.rect=self.image.get_rect()
        self.rect.center=rotation+50,400
        screen.blit(self.image,self.rect)      
        
    def update(self):
        global gameScore
        self.rect.y -= 1
        rotation=self.rect.angle
        if self.rect.y<50:
             key=pygame.key.get_pressed()
             if key[pygame.K_LEFT] and self.rect.x==15:
                gameScore+=1
                
                self.kill()
             if key[pygame.K_DOWN] and self.rect.x==105:
                gameScore+=1
                self.kill()
             if key[pygame.K_RIGHT] and self.rect.x==195:
                gameScore+=1
                self.kill()
             if key[pygame.K_UP] and self.rect.x==285:
                gameScore+=1
                self.kill()
             self.rect.y -= 1
             if self.rect.y<40:
                 self.kill()

for i in range(0,4):
    reciever=spawnCollector(i*90)
    recieveList.add(reciever)


while not Done:
    print(gameScore)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    if random.randrange(0,200)%29==3 and len(arrowList)<5:
        for i in range(4):   
           rotation=random.randrange(0,4)*90
           color=str(random.randrange(0,8))
        arrow=spawnArrow(color,rotation)
        arrowList.add(arrow)
       
    screen.fill((0, 0, 0))
    pygame.time.wait(gameSpeed)
    recieveList.update()
    recieveList.draw(screen)
    arrowList.update()
    arrowList.draw(screen)
    pygame.display.update()