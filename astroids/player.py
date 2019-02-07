import settings as S 
import pygame as pg 
import random as R 
import roids
import bullets
VEC = pg.math.Vector2


class Player(pg.sprite.Sprite):

	def __init__(self, image, startx, starty):
		pg.sprite.Sprite.__init__(self)
		self.size = S.PLAYER_SIZE
		self.radius = S.PLAYER_R
		
		self.image0 = image
		self.image = self.image0.copy()
		self.image.set_colorkey(S.WHITE)
		self.image0.set_colorkey(S.WHITE)
		self.image.convert()
		
		self.rect = self.image.get_rect()

		self.vel = VEC(0, 0)
		self.acceleration = VEC(0.3, 0)
		self.pos = VEC(startx, starty)
		self.rotation = 90
		self.roatation_speed = 1 
		self.last_update = pg.time.get_ticks()
		

	def rotate(self, speed):
		now = pg.time.get_ticks()
		if now - self.last_update > 30:
			self.last_update = now
			self.rotation = (self.rotation + speed) % 360
			new_image = pg.transform.rotate(self.image0, self.rotation - 90)
			old_center = self.rect.center
			self.image = new_image
			self.rect = self.image.get_rect()
			self.rect.center = old_center

	def move(self):
		key = pg.key.get_pressed()
		now = pg.time.get_ticks()
		if key[pg.K_LEFT]:
			self.roatation_speed = 15
			self.rotate(self.roatation_speed)
		if key[pg.K_RIGHT]:
			self.roatation_speed = -15
			self.rotate(self.roatation_speed)
		if key[pg.K_UP]:
			self.vel += self.acceleration.rotate(-self.rotation)
		if key[pg.K_DOWN]:
			self.vel -= self.acceleration.rotate(-self.rotation) / 2
		if self.vel.length() > S.PLAYER_MAX_SPEED:
			self.vel.scale_to_length(S.PLAYER_MAX_SPEED)

	'''def animate_player(self, image, images):
		now = pg.time.get_ticks()
		
		if now - self.last_update > 20:
			self.image0 = images[self.index]
			self.index += 1

		if self.index > 1:
			self.index = 0

		self.image0 = image
'''

	def update(self):
	
		self.move()
		if self.pos.x + self.radius < 0:
			self.pos.x = S.WIDTH + self.radius
		if self.pos.x - self.radius > S.WIDTH:
			self.pos.x = 0 - self.radius
		if self.pos.y + self.radius < 0:
			self.pos.y = S.HEIGHT - self.radius
		if self.pos.y - self.radius > S.HEIGHT:
			self.pos.y = 0 - self.radius
		self.pos += self.vel 
		self.rect.center = (self.pos.x, self.pos.y)