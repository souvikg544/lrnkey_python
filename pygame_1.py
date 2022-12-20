# Introduction to the pygame module

#Pygame as the name suggests helps us to create games in python



import pygame
import time
import random

# Importing Sprite


from pygame.locals import (
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
        self.surf= pygame.Surface((60,40))
        self.surf.fill((0,0,255))
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
        if self.rect.right>500:
            self.rect.right=500
        if self.rect.top<=0:
            self.rect.top=0
        if self.rect.bottom>=500:
            self.rect.bottom=500

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.surf=pygame.Surface((40,40))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(
            center=(
            random.randint(520,600),
            random.randint(0,500),
        )
        )
        self.speed=random.randint(0,1)

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if(self.rect.right<0):
            self.kill()


pygame.init()
screen=pygame.display.set_mode([500,500])
player = Player()


enemies=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
all_sprites.add(player)

addenemy = pygame.USEREVENT +1

pygame.time.set_timer(addenemy,250)

run=True
i=0
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

    screen.fill((0,255,255))

    #r=pygame.draw.circle(screen,(0,0,255),(250,250),100)
    pressed_keys=pygame.key.get_pressed()
    player.update(pressed_keys)

    enemies.update()

    for entity in all_sprites:
        screen.blit(entity.surf,entity.rect)

    pygame.display.flip()

pygame.quit()
