#bullets, tar inn koords tel start x og start y

import pygame as pg 
import roids
import settings as S 
import random as R 
import player
VEC = pg.math.Vector2


class Bullet(pg.sprite.Sprite):
	def __init__(self, rotation, startx, starty):
		pg.sprite.Sprite.__init__(self)
		self.color = S.RED
		self.r = S.BULLET_RADIUS
		self.image = pg.Surface((50, 50))
		self.image.set_colorkey(S.BLACK)
		self.image.fill(S.BLACK)
		self.rect = self.image.get_rect()
		pg.draw.circle(self.image, self.color, self.rect.center, self.r)
		self.offset = VEC(S.PLAYER_R * 2, 0).rotate(-rotation)
		self.pos = VEC(startx, starty) + self.offset
		self.vel = VEC(S.BULLET_SPEED, 0).rotate(-rotation)
		self.last_update = pg.time.get_ticks()

	def update(self):
		now = pg.time.get_ticks()
		if now - self.last_update > 2000:
			self.kill()

		if self.pos.x - self.r > S.WIDTH:
			self.pos.x = 0 - self.r
		if self.pos.x + self.r < 0:
			self.pos.x = S.WIDTH + self.r
		if self.pos.y - self.r > S.HEIGHT:
			self.pos.y = 0 - self.r
		if self.pos.y  + self.r < 0:
			self.pos.y = S.HEIGHT + self.r
		
		self.pos += self.vel
		self.rect.center = (self.pos.x, self.pos.y)

			


