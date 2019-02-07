import pygame as pg 
from settings import *
from pygame.math import Vector2 as VEC 



class Brick(pg.sprite.Sprite):
	def __init__(self, image, startx, starty):
		"""
			simple recangular image as brick
		"""
		pg.sprite.Sprite.__init__(self)
		self.image = image 
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = startx
		self.rect.y = starty