import pygame as pg 
from settings import *
from pygame.math import Vector2 as VEC 



'''
    Player class
'''

class Player(pg.sprite.Sprite):
    def __init__(self, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image 
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = PLAYER_POS_X
        self.rect.y = PLAYER_POS_Y
    
        self.vel = VEC(0, 0)
        self.pos = VEC(self.rect.centerx, self.rect.y)

    def update(self):
        key = pg.key.get_pressed()

        if key[pg.K_LEFT]:
            if self.rect.x <= 0:
                self.rect.x = 0
                self.vel = VEC(0, 0)
            else:
                self.vel = VEC(-PLAYER_SPEED, 0)
        if key[pg.K_RIGHT]:
            if self.rect.x + PLAYER_WIDTH >= WIDTH:
                self.rect.x = WIDTH - PLAYER_WIDTH
                self.vel = VEC(0, 0)
            else: 
                self.vel = VEC(PLAYER_SPEED, 0) 

        self.pos += self.vel
        self.rect.center = (self.pos.x, self.pos.y)
        self.vel = VEC(0, 0)




