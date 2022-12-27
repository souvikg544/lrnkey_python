# Introduction to the pygame module

#Pygame as the name suggests helps us to create games in python

import pygame
import time
import random

# Importing Sprite


from pygame.locals import (
RLEACCEL,
K_UP,
K_DOWN,
K_LEFT,
K_RIGHT,
K_ESCAPE,
KEYDOWN,
QUIT
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf= pygame.image.load("rocket1.png").convert()
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self,pressed_keys):
        if(pressed_keys[K_UP]):
            self.rect.move_ip(0,-1) # x,y
        if (pressed_keys[K_DOWN]):
            self.rect.move_ip(0, 1)
        if (pressed_keys[K_LEFT]):
            self.rect.move_ip(-1, 0)
        if (pressed_keys[K_RIGHT]):
            self.rect.move_ip(1, 0)

        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>700:
            self.rect.right=700
        if self.rect.top<=0:
            self.rect.top=0
        if self.rect.bottom>=700:
            self.rect.bottom=700

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.surf = pygame.image.load("birds1.png").convert()
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
            random.randint(720,800),
            random.randint(0,700),
        )
        )
        self.speed=random.randint(0,1)

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if(self.rect.right<0):
            self.kill()

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud,self).__init__()
        self.surf=pygame.image.load("cloud70.png").convert()
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(520, 600),
                random.randint(0, 500),
            )
        )
    def update(self):
        self.rect.move_ip(-1,0)
        if self.rect.right<0 :
            self.kill()


pygame.init()

start=time.time()

screen=pygame.display.set_mode([700,700])
player = Player()


enemies=pygame.sprite.Group()
clouds=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
all_sprites.add(player)

addenemy = pygame.USEREVENT +1
pygame.time.set_timer(addenemy,250)

addcloud=pygame.USEREVENT + 2
pygame.time.set_timer(addcloud,1000)

run=True
i=0
clock=pygame.time.Clock()


# Implement scores
score=0

# Displaying text
font=pygame.font.Font('freesansbold.ttf',32)
text=font.render("lost",True,(0,255,0),(0,0,128))
textrect=text.get_rect()
textrect.center=(100,100)



text_score=font.render("Score : ",True,(0,255,0),(0,0,128))
text_score_rect=text_score.get_rect()
text_score_rect.center=(500,600)

run1=True
while run:  # infinite loop
    for e in pygame.event.get():
        if(e.type == pygame.QUIT):
            run=False
        if(e.type==KEYDOWN):
            if (e.key == K_ESCAPE):
                run=False

        elif(e.type==addenemy):
            newenemy = Enemy()
            enemies.add(newenemy)
            all_sprites.add(newenemy)

        elif(e.type == addcloud):
            new_cloud=Cloud()
            clouds.add(new_cloud)
            all_sprites.add(clouds)



    #r=pygame.draw.circle(screen,(0,0,255),(250,250),100)
    pressed_keys=pygame.key.get_pressed()
    player.update(pressed_keys)

    enemies.update()
    clouds.update()
    screen.fill((135, 206, 250))
    for entity in all_sprites:
        screen.blit(entity.surf,entity.rect)

    if pygame.sprite.spritecollideany(player,enemies):
        player.kill()
        print("Lost")
        screen.blit(text,textrect)
        #clock.tick(1)
        run=False
    text_score = font.render(f"Score : {i}", True, (0, 255, 0), (0, 0, 128))

    pt = time.time()  # Shortcut for present time
    if ((int(pt) - int(start)) == 1):
        i+=1
        start = pt

    screen.blit(text_score, text_score_rect)

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
