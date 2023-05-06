import pygame,random,sys,os
from pygame.locals import *
pygame.init()
pygame.mixer.init() 
pygame.mixer.music.set_volume(0.5)
resolution=[800,500]
screen=pygame.display.set_mode(resolution)
pygame.display.set_caption("ptsdance")

gameOver=True
gameSpeed=15
arrowList=pygame.sprite.Group()
recieveList=pygame.sprite.Group()
passList=pygame.sprite.Group()
gameScore=0
disco_ball=[pygame.image.load("src/game_files/game_objects/disco_ball_0.png"),pygame.image.load("src/game_files/game_objects/disco_ball_1.png"),pygame.image.load("src/game_files/game_objects/disco_ball_2.png"),pygame.image.load("src/game_files/game_objects/disco_ball_3.png")]
disco_bg=[pygame.image.load("src/game_files/game_objects/dance_bg_0.png"),pygame.image.load("src/game_files/game_objects/dance_bg_1.png"),pygame.image.load("src/game_files/game_objects/dance_bg_2.png"),pygame.image.load("src/game_files/game_objects/dance_bg_3.png"),pygame.image.load("src/game_files/game_objects/dance_bg_4.png"),pygame.image.load("src/game_files/game_objects/dance_bg_3.png"),pygame.image.load("src/game_files/game_objects/dance_bg_2.png"),pygame.image.load("src/game_files/game_objects/dance_bg_1.png"),pygame.image.load("src/game_files/game_objects/dance_bg_0.png")]
dance_bg_index=0
disco_ball_index=0
white=(255,255,255)
blue=(56,138,211)
float_effect=[0,1,3,4,3,1,0]
font_big=pygame.font.Font("src/font/GALSB.ttf",40)
font_small=pygame.font.Font("src/font/GALSB.ttf",32)
clock=pygame.time.Clock()
def menuScreen():
        
        global gameOver,dance_bg_index
        btn_1=font_big.render("START",True,blue)
        btn_1_rect=btn_1.get_rect()
        btn_1_rect.center=400,350
        btn_2=font_small.render("QUIT",True,blue)
        btn_2_rect=btn_2.get_rect()
        btn_2_rect.center=400,400
        hover=0
        l=0
        while gameOver:
            dance_bg_index+=0.25
            l+=0.25
            if dance_bg_index>8:
                dance_bg_index=0
            if l>6:
                l=0
            for event in pygame.event.get():
               if event.type==pygame.QUIT:
                   pygame.quit()
                   sys.exit()
               if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    hover=1
                    btn_2=font_big.render("QUIT",True,blue)
                    btn_2_rect=btn_2.get_rect()
                    btn_1=font_small.render("START",True,blue)
                    btn_1_rect=btn_1.get_rect()
                   
                if event.key==pygame.K_UP:
                    hover=0
                    btn_2=font_small.render("QUIT",True,blue)
                    btn_2_rect=btn_2.get_rect()
                    btn_1=font_big.render("START",True,blue)
                    btn_1_rect=btn_1.get_rect()
                    
                if hover==1 and event.key==pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()
                if hover==0 and event.key==pygame.K_SPACE:
                    gameOver=False

            btn_1_rect.center=400,350
            btn_2_rect.center=400,400
            if hover==0:
               btn_1_rect.center=400,350 + float_effect[round(l)]
            else:
               btn_2_rect.center=400,390 + float_effect[round(l)]
            bg_sel_img=pygame.image.load("src/game_files/game_objects/bg_wp_sel.png")
            bg_sel_img=pygame.transform.smoothscale(bg_sel_img,(1600,1000))
            bg_sel_rect=bg_sel_img.get_rect()
            bg_sel_rect.center=460,250
            bg_img=disco_bg[round(dance_bg_index)]
            bg_img=pygame.transform.smoothscale(bg_img,(1600,1000))
            bg_img_rect=bg_img.get_rect()
            bg_img_rect.center=460,250
            bg_wp_img=pygame.image.load("src/game_files/game_objects/bg_wp.png")
            bg_wp_img=pygame.transform.smoothscale(bg_wp_img,(800,500))
            bg_wp_rect=bg_wp_img.get_rect()
            bg_wp_rect.center=400,250
            screen.fill((255,255,255))
            screen.blit(bg_wp_img,bg_wp_rect)
            screen.blit(bg_img,bg_img_rect)
            screen.blit(bg_sel_img,bg_sel_rect)
            screen.blit(btn_2,btn_2_rect)
            screen.blit(btn_1,btn_1_rect)
            pygame.display.update()
        
        screen.fill((0,0,0))
        load_txt=font_big.render("LOADING...",True,(255,255,255))
        load_txt_rect=load_txt.get_rect()
        load_txt_rect.center=650,450
        screen.blit(load_txt,load_txt_rect)
        pygame.display.update()
        pygame.time.wait(1000)
        
menuScreen()

def draw_disco_ball():
    global disco_ball_index,dance_bg_index
    if dance_bg_index>8:
        dance_bg_index=0
    if disco_ball_index>3:
        disco_ball_index=0
    bg_img=disco_bg[round(dance_bg_index)]
    img=disco_ball[round(disco_ball_index)]
    bg_img=pygame.transform.smoothscale(bg_img,(800,500))
    bg_rect=bg_img.get_rect()
    bg_rect.center=400,250
    rect=img.get_rect()
    rect.center=600,250
    disco_ball_index+=0.05
    dance_bg_index+=0.25
    ball_img=pygame.image.load("src/game_files/game_objects/disco_ball.png")
    ball_img_rect=ball_img.get_rect()
    ball_img_rect.center=600,50
    dance_floor=pygame.image.load("src/game_files/game_objects/dance_floor.png")
    dance_floor=pygame.transform.smoothscale(dance_floor,(350,200))
    dance_floor_rect=dance_floor.get_rect()
    dance_floor_rect.center=600,405
    bg_wp=pygame.image.load("src/game_files/game_objects/bg_wp.png")
    bg_wp=pygame.transform.smoothscale(bg_wp,(800,500))
    bg_wp_rect=bg_wp.get_rect()
    bg_wp_rect.center=400,250
    screen.blit(bg_wp,bg_wp_rect)
    screen.blit(bg_img,bg_rect)
    screen.blit(ball_img,ball_img_rect)
    screen.blit(dance_floor,dance_floor_rect)
    screen.blit(img,rect)
    
class spawnPass(pygame.sprite.Sprite):
    def __init__(self,imageName):
        super().__init__()
        self.image=imageName
        self.image=pygame.transform.smoothscale(self.image,(70,70))
        self.rect=self.image.get_rect()
        self.rect.center=500+random.randrange(0,3)*50,50
        screen.blit(self.image,self.rect)   
    def update(self):
        if self.rect.y>300:
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
        self.rect.y -= 2
        
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

menuScreen()
for i in range(0,4):
    reciever=spawnCollector(i*90)
    recieveList.add(reciever)
 
music_dir="src/music/"
file_list=os.listdir(music_dir)
random.shuffle(file_list)
music_list_index=0
while not gameOver:
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load("src/music/"+str(file_list[music_list_index]))
        pygame.mixer.music.play()
        music_list_index+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                screen.fill((0,0,0))
                gameOver=True
                menuScreen()
    if random.randrange(0,200)%29==3 and len(arrowList)<random.randrange(5):
        for i in range(4):   
           rotation=random.randrange(0,4)*90
           color=str(random.randrange(0,50)%8)
        arrow=spawnArrow(color,rotation)
        arrowList.add(arrow)
    screen.fill((14, 23, 31))
    pygame.time.wait(gameSpeed)
    draw_disco_ball()
    passList.update()
    passList.draw(screen)
    recieveList.update()
    recieveList.draw(screen)
    arrowList.update()
    arrowList.draw(screen)
    clock.tick(60)
    pygame.display.update()