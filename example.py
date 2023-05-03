import pygame,random,sys
pygame.init()
resolution=[400,400]
screen=pygame.display.set_mode(resolution)
pygame.display.set_caption("example")
Done=False
sprite_list=pygame.sprite.Group()
class Sprite(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        self.image=pygame.image.load("src/game_files/dus.png")
        self.rect=self.image.get_rect()
        self.rect.center=width,height
        screen.blit(self.image,self.rect)
    def die(self):
        self.kill()
for x in range(5):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Done=True
    for i in range(5):
        sprite=Sprite(random.randrange(1,400),random.randrange(1,400))
        sprite_list.add(sprite)
        print(sprite_list)
        sprite.die()

        
    pygame.display.update()