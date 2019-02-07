import pygame as pg 
from settings import *
import random as R 
from pygame.math import Vector2 as VEC
import math


class Ball(pg.sprite.Sprite):
	def __init__(self, image, startx, starty):
		pg.sprite.Sprite.__init__(self)
		self.radius = BALL_RADIUS
		self.image = image 
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.spawntime = pg.time.get_ticks()

		self.x = startx
		self.y = starty
		self.direction = 180

		self.rect.x = self.x
		self.rect.y = self.y

	def bounce(self, diff):
		self.direction = (180 - self.direction) % 360
		self.direction -= diff

	def update(self):
		'''
		using sin /cosine to determine ball movement
		'''
		timer = pg.time.get_ticks()
		if timer - self.spawntime >= 800:

			self.direction_radians = math.radians(self.direction)
			self.x += BALL_SPEED * math.sin(self.direction_radians)
			self.y -= BALL_SPEED * math.cos(self.direction_radians)

			self.rect.x = self.x
			self.rect.y = self.y
		
			if self.rect.y < BALL_HEIGHT:
				self.bounce(0)
			if self.rect.x + self.radius >= WIDTH:
				self.direction = (360 - self.direction) % 360
			if self.rect.x - self.radius <= 0:
				self.direction = (360 - self.direction) % 360

	def collide_player(self, player):
		self.diff = (player.rect.x + PLAYER_WIDTH / 2) - (self.rect.x + BALL_WIDTH / 2)
		self.rect.y = player.rect.y - BALL_HEIGHT
		self.bounce(self.diff)

	def collide_brick(self):
		self.bounce(0)
