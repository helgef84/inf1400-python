#!/usr/bin/env python3

import pygame as pg
import random

#BG_FNAME = "panda.jpg"
#MOUSE_FNAME = "mouse.png"
SCREEN_X = 1020
SCREEN_Y = 510

pg.init()

screen = pg.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)
#background = pg.image.load(BG_FNAME)
#background = background.convert()

#mouse_img = pg.image.load(MOUSE_FNAME).convert_alpha()
#newmouse = pg.transform.scale(mouse_img, (35, 35))
#mouse_size_x = newmouse.get_width()
#mouse_size_x = newmouse.get_height()



class Ball:
    def __init__(self):
        self.x = int(SCREEN_X / 2)
        self.y = int(SCREEN_Y / 2)

        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)
        self.image = pg.Surface((20, 20))
        pg.draw.circle(self.image, (0, 0, 255), (self.x, self.y), 10)
        

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

       

ball = Ball()
while True:
    event = pg.event.wait()
    if event.type == pg.QUIT:
        pg.quit()

   # x, y = pg.mouse.get_pos()
   # mx = x - mouse_size_x / 2
   # my = y - mouse_size_x / 2    

    #screen.blit(background, (0, 0))
    #screen.blit(newmouse, (mx, my))
    
    ball.update()
    ball.draw(screen)
    pg.display.update()
    





