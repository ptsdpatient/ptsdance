import pygame,sys
pygame.init()
screen=pygame.display.set_mode((800,500))
white=(255,255,255)
gameOver=True
disco_bg=[pygame.image.load("src/game_files/game_objects/dance_bg_0.png"),pygame.image.load("src/game_files/game_objects/dance_bg_1.png"),pygame.image.load("src/game_files/game_objects/dance_bg_2.png"),pygame.image.load("src/game_files/game_objects/dance_bg_3.png"),pygame.image.load("src/game_files/game_objects/dance_bg_4.png"),pygame.image.load("src/game_files/game_objects/dance_bg_3.png"),pygame.image.load("src/game_files/game_objects/dance_bg_2.png"),pygame.image.load("src/game_files/game_objects/dance_bg_1.png"),pygame.image.load("src/game_files/game_objects/dance_bg_0.png")]
float_effect=[0,1,3,4,3,1,0]
def menuScreen():
        global gameOver
        bg_img=pygame.image.load("src/game_files/game_objects/menu_bg.png")
        bg_img=pygame.transform.smoothscale(bg_img,(800,500))
        bg_img_rect=bg_img.get_rect()
        font_big=pygame.font.Font("src/font/GALSB.ttf",40)
        font_small=pygame.font.Font("src/font/GALSB.ttf",32)
        btn_1=font_big.render("START",True,white)
        btn_1_rect=btn_1.get_rect()
        btn_1_rect.center=400,300
        btn_2=font_small.render("QUIT",True,white)
        btn_2_rect=btn_2.get_rect()
        btn_2_rect.center=400,350
        hover=0
        l=0
        while gameOver:
            l+=0.1
            if l>6:
                l=0
            for event in pygame.event.get():
               if event.type==pygame.QUIT:
                   pygame.quit()
               if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    hover=1
                    btn_2=font_big.render("QUIT",True,white)
                    btn_2_rect=btn_2.get_rect()
                    btn_1=font_small.render("START",True,white)
                    btn_1_rect=btn_1.get_rect()
                   
                if event.key==pygame.K_UP:
                    hover=0
                    btn_2=font_small.render("QUIT",True,white)
                    btn_2_rect=btn_2.get_rect()
                    btn_1=font_big.render("START",True,white)
                    btn_1_rect=btn_1.get_rect()
                    
                if hover==1 and event.key==pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()
            btn_1_rect.center=400,300
            btn_2_rect.center=400,350
            if hover==0:
               btn_1_rect.center=400,300 + float_effect[round(l)]
            else:
               btn_2_rect.center=400,340 + float_effect[round(l)]
             
            screen.fill(white)
            screen.blit(bg_img,bg_img_rect)
            screen.blit(btn_2,btn_2_rect)
            screen.blit(btn_1,btn_1_rect)
            pygame.display.update()

menuScreen()