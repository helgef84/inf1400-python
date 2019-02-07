import settings as S
import random as R 
import pygame as pg 
import time
import roids
import player
import bullets
import load_images as LOAD


######  PG SETUP #############

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((S.WIDTH, S.HEIGHT))
pg.display.set_caption("Astroids FOO")
clock = pg.time.Clock()


########### Sprite group four astroids #########
allsprites = pg.sprite.Group()
astroids = pg.sprite.Group()
playergroup = pg.sprite.Group()
bulletgroup = pg.sprite.Group()

######## Load images ##############
astroid_images = LOAD.load_astroid()
player_image = LOAD.load_player()
background_image = LOAD.load_background()


for i in range(0, S.MAX_ASTROIDS):
	astroid = roids.Astroid(astroid_images)
	allsprites.add(astroid)
	astroids.add(astroid)
										
player = player.Player(player_image, S.PLAYER_STARTPOS_X, S.PLAYER_STARTPOS_Y)
allsprites.add(player)
playergroup.add(player)

#### SHOOTING FUNCTION
def player_shoot(rotation, x, y):
	bulletR = bullets.Bullet(rotation, x, y)
	bulletgroup.add(bulletR)
	allsprites.add(bulletR)


###### GAME LOOP #######
running = True

#astroid_count = S.MAX_ASTROIDS
#astroid_count > 0:

while running: 
	### SET FPS ####
	clock.tick(S.FPS)

	#### Input Processing #########

	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_ESCAPE:
				pg.quit()
				quit()
			if event.key == pg.K_SPACE:
				player_shoot(player.rotation, player.rect.centerx, player.rect.centery)
		
	hits = pg.sprite.groupcollide(astroids, bulletgroup, True, True, pg.sprite.collide_circle)
	for hit in hits:
		astroid = roids.Astroid(astroid_images)
		astroids.add(astroid)
		allsprites.add(astroid)
		
######################    SCORE CALCULATION ######################
		#astroid_count -=  1

		#score = astroid_count * S.SCORE_MULTIPLIER
	#if astroid_count == :
		#running = False


	playercollide = pg.sprite.spritecollide(player, astroids, True, pg.sprite.collide_circle)
	if playercollide:
		print("you got hit...")
		#print("hit")
	screen.fill(S.WHITE)
	screen.blit(background_image, (0, 0))
	allsprites.update()
	allsprites.draw(screen)

	pg.display.flip()


pg.quit()

