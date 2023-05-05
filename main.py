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
passList=pygame.sprite.Group()
gameScore=0
bg=pygame.image.load("src/game_files/game_objects/dance_bg.png")
bg=pygame.transform.smoothscale(bg,(800,500))
bg_rect=bg.get_rect()
bg_rect.center=400,250
screen.blit(bg,bg_rect)
disco_ball=[pygame.image.load("src/game_files/game_objects/disco_ball_0.png"),pygame.image.load("src/game_files/game_objects/disco_ball_1.png"),pygame.image.load("src/game_files/game_objects/disco_ball_2.png"),pygame.image.load("src/game_files/game_objects/disco_ball_3.png")]
disco_ball_index=0
clock=pygame.time.Clock()
        

def draw_disco_ball():
    global disco_ball_index
    if disco_ball_index>3:
        disco_ball_index=0
    img=disco_ball[round(disco_ball_index)]
    rect=img.get_rect()
    rect.center=600,250
    disco_ball_index+=0.05
    screen.blit(img,rect)
    img2=pygame.image.load("src/game_files/game_objects/disco_ball.png")
    rect2=img2.get_rect()
    rect2.center=600,50
    screen.blit(img2,rect2)

class spawnPass(pygame.sprite.Sprite):
    def __init__(self,imageName):
        super().__init__()
        self.image=imageName
        self.image=pygame.transform.smoothscale(self.image,(70,70))
        self.rect=self.image.get_rect()
        self.rect.center=500+random.randrange(0,3)*50,50
        screen.blit(self.image,self.rect)   
    def update(self):
        if self.rect.y>400:
            self.kill()
        else:
            self.rect.y+=3
class spawnCollector(pygame.sprite.Sprite):
    def __init__(self,rotation):
         super().__init__()
         self.image=pygame.image.load("src/game_files/game_objects/collector.png")
         self.image=pygame.transform.rotate(self.image,rotation)
         self.image=pygame.transform.smoothscale(self.image,(80,80))
         self.rect=self.image.get_rect()
         self.rect.center=rotation+50,80
         screen.blit(self.image,self.rect)
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
        
        if self.rect.y<50:
             key=pygame.key.get_pressed()
             if key[pygame.K_LEFT] and self.rect.x==15:
                gameScore+=1
                self.image=pygame.transform.rotate(self.image,90)
                spawnpass=spawnPass(self.image)
                passList.add(spawnpass)
                self.kill()
             if key[pygame.K_DOWN] and self.rect.x==105:
                gameScore+=1
                self.image=pygame.transform.rotate(self.image,0)
                spawnpass=spawnPass(self.image)
                passList.add(spawnpass) 
                self.kill()
             if key[pygame.K_RIGHT] and self.rect.x==195:
                gameScore+=1
                self.image=pygame.transform.rotate(self.image,270)
                spawnpass=spawnPass(self.image)
                passList.add(spawnpass) 
                self.kill()
             if key[pygame.K_UP] and self.rect.x==285:
                gameScore+=1
                self.image=pygame.transform.rotate(self.image,180)
                spawnpass=spawnPass(self.image)
                passList.add(spawnpass) 
                self.kill()
             self.rect.y -= 1
             if self.rect.y<40:
                 self.kill()
    
            

for i in range(0,4):
    reciever=spawnCollector(i*90)
    recieveList.add(reciever)


while not Done:
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
    screen.fill((14, 23, 31))
    pygame.time.wait(gameSpeed)
    screen.blit(bg,bg_rect)
    draw_disco_ball()
    passList.update()
    passList.draw(screen)
    recieveList.update()
    recieveList.draw(screen)
    arrowList.update()
    arrowList.draw(screen)
    clock.tick(60)
    pygame.display.update()