import settings as S 
import pygame as pg 
import random as R
import time


class Astroid(pg.sprite.Sprite):
	startpos = [0, S.HEIGHT]
	def __init__(self, images):
		pg.sprite.Sprite.__init__(self)
		self.color = R.choice(S.COLORS)
		self.radius = R.choice(S.ASTROIDS)
		
		if(self.radius == S.SMALL_ASTROID):
			self.image0  = images[0]
			self.image = self.image0.copy()
		elif(self.radius == S.MEDIUM_ASTROID):
			self.image0 = images[1]
			self.image = self.image0.copy()
		elif(self.radius == S.BIG_ASTROID):
			self.image0 = images[2]
			self.image = self.image0.copy()
		
		self.rect = self.image.get_rect()
		self.rect.centerx = R.randint(0, S.WIDTH)
		self.rect.bottom = R.choice(self.startpos)
		

		if self.rect.centerx > S.WIDTH / 2:
			self.xv = R.randint(2, S.ENEMY_MAXSPEED) * -1
		else:
			self.xv = R.randint(2, S.ENEMY_MAXSPEED)

		if self.rect.bottom == 0:
			self.xy = R.randint(2, S.ENEMY_MAXSPEED)
		elif self.rect.bottom == S.HEIGHT:
			self.xy = R.randint(2, S.ENEMY_MAXSPEED) * -1

		self.rotation = 0
		self.rotation_speed = R.randint(-5, 5)
		self.last_update = pg.time.get_ticks()


	def move(self):
		self.rect.centerx += int(self.xv)
		self.rect.bottom += int(self.xy)

	def rotate(self):
		now = pg.time.get_ticks()
		if now - self.last_update > 100:
			self.last_update = now
			self.rotation = (self.rotation + self.rotation_speed) % 360
			new_image = pg.transform.rotate(self.image0, self.rotation)
			old_center = self.rect.center
			self.image = new_image
			self.rect = self.image.get_rect()
			self.rect.center = old_center


	def update(self):
		self.move()
		self.rotate()

		#######  wrap around edges in x direction ########
		if self.rect.centerx + self.radius < 0:
			self.rect.centerx = S.WIDTH + self.radius
		if self.rect.centerx - self.radius > S.WIDTH:
			self.rect.centerx = 0 - self.radius
		########### Wrap in y direction ############
		if self.rect.bottom + self.radius < 0:
			self.rect.bottom  = S.HEIGHT + (self.radius * 2)
		if self.rect.bottom - (self.radius * 2) > S.HEIGHT:
			self.rect.bottom = 0










































