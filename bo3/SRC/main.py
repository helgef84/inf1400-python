import pygame as pg
from os import path
import sys
import player, brick, ball 
from settings import *
from pygame.math import Vector2 as Vector
import time
from textbox import *




'''
	Initialize the game as a class

'''

class Game():
	def __init__(self):
		'''
			Initialize pygame module and set initial values 
			load image, and fonts used to draw text on screen
		'''
		pg.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		pg.display.set_caption("BREAKOUT")
		self.clock = pg.time.Clock()
		self.FONT = pg.font.Font(None, 32)
		
		### Starting values
		self.score = 0
		self.brick_count = 0
		self.player_lives = 3
		self.running = True	
		self.level = 0

		### Create (or open) high score text file
		self.high_score = open("high_score.txt", "a+")
		
		### Load map of the first level
		self.load_map_data(LEVELS[self.level])
		
		### load images 
		self.intro_image = self.load_introimage()
		self.gameover_image = self.load_gameover_image()
		self.paused_image = self.load_paused_image()
		self.level_complete_image = self.load_level_complete()
		self.background = self.load_background()
		self.ball_image = self.load_ball()
		self.player_image = self.load_player()
		self.brick_image = self.load_brick()
		
		### Load fonts
		self.SMALLTEXT = pg.font.SysFont("comicsansms", 25)
		self.MEDIUMTEXT = pg.font.SysFont("comicsansms", 50)
		self.LARGETEXT = pg.font.SysFont("comicsansms", 80)	

	def new(self):
		'''
		Set up spritegroups for game elements: Later used for collision detection
		Initialize game elements and add to sprite groups.
		Draw the map to be displayed
		'''
		### set spritegroups
		self.allsprites = pg.sprite.Group()
		self.playersprite = pg.sprite.Group()
		self.ballsprite = pg.sprite.Group()
		self.bricksprite = pg.sprite.Group()
		
		### Draw map
		self.draw_map()
		
		### Create player sprite
		self.player = player.Player(self.player_image)
		self.allsprites.add(self.player)
		self.playersprite.add(self.player)
		
		### Starts the gameloop
		self.run()


	def run(self):
		'''
		This function acts as the actual game loop. all events, updates and draws are done
		from this function
		'''

		self.playing = True

		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()
		

	##############################################################
	### Game screens

	def introscreen(self):
		'''
			intro screen / instructions

		'''

		self.intro = True
		self.image = self.intro_image
		while self.intro:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_SPACE or event.key == pg.K_c:
						self.new()
					if event.key == pg.K_ESCAPE or event.key == pg.K_q:
						pg.quit()
						sys.exit()
			
			self.screen.fill(BLACK)
			self.screen.blit(self.image, (0, 0))
			
			pg.display.flip()

	def game_over(self):
		'''
			game over screen, 
			play again or quit
			display textbox to enter name to save high score to file
		'''
		self.gameover = True
		self.image = self.gameover_image
		
		### Initialize the textbox class
		self.input_box = InputBox((WIDTH * 0.60), (HEIGHT / 2), 140, 32, self.high_score, self.score)
		
		while self.gameover:

			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()
				
				### Get input from player
				self.input_box.handle_event(event)
				
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_SPACE or event.key == pg.K_c:
						self.score = 0
						self.player_lives = 3
						self.new()
					if event.key == pg.K_ESCAPE or event.key == pg.K_q:
						pg.quit()
						sys.exit()
					if event.key == pg.K_RETURN:
						self.introscreen()
			self.input_box.update()	

			self.screen.fill(BLACK)
			self.screen.blit(self.image, (0, 0))

			### Save input to file along with the score
			self.message_to_screen("YOUR SCORE: " + str(self.score), BLACK, -(HEIGHT * 0.45), "medium")
			### Draw input text to screen
			self.input_box.draw(self.screen)

			pg.display.flip()
		
	def game_paused(self):
		'''
			Halts the gameloop while game is paused. 
			Does not lose game state
		'''
		self.paused = True
		self.image = self.paused_image
		while self.paused:
			
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_SPACE or event.key == pg.K_c:
						self.paused = False
					if event.key == pg.K_r:
						self.paused = False
						self.playing = False
						self.introscreen()
					if event.key == pg.K_ESCAPE or event.key == pg.K_q:
						pg.quit()
						sys.exit()
			
			self.screen.fill(BLACK)
			self.screen.blit(self.image, (0, 0))
			
			pg.display.flip()

	def level_complete(self):
		'''
			Waiting screen between levels
		'''
		self.complete = True
		self.image = self.level_complete_image

		while self.complete:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_SPACE or event.key == pg.K_c:
						self.complete = False
					if event.key == pg.K_ESCAPE or event.key == pg.K_q:
						pg.quit()
						sys.exit()
			self.screen.fill(BLACK)
			self.screen.blit(self.image, (0, 0))
			pg.display.flip()

	##########################################################
	def update(self):
		'''
			calls update() on all sprites in the allsprites group, rather than a single call to 
			each game elements class function
		'''
		
		self.allsprites.update()
	
	def events(self):
		'''
			most event-handling is done with this function, 
		'''

		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.game_paused()

		'''
			check if game over
		'''
		if self.ball.rect.y > HEIGHT:
			self.ball.kill()
			self.player_lives -= 1
			self.ball = ball.Ball(self.ball_image, self.player.rect.centerx, self.player.rect.y -(2 * BALL_HEIGHT))
			self.allsprites.add(self.ball)
			self.ballsprite.add(self.ball)
			if self.player_lives == 0:
				
				time.sleep(0.5)
				self.game_over()

		### bounce ball from player sprite
		bounce_on_player = pg.sprite.spritecollide(self.player, self.ballsprite, False)
		if bounce_on_player:
			self.ball.collide_player(self.player)
	
		###  bounce ball from brick sprit, remove bricks on impact.
		brick_hits = pg.sprite.groupcollide(self.ballsprite, self.bricksprite, False, True)
		for hit in brick_hits:
			if len(self.bricksprite) == 0:
				self.score += 10
			self.score += 10 * len(brick_hits)
			
			self.ball.collide_brick()

		### keep track of remaining bricks until level complete		
		self.brick_count = len(self.bricksprite)

		if self.brick_count == 0:
			time.sleep(0.5)
			self.level += 1
			if self.level >= len(LEVELS):
				self.level = 0
			self.level_complete()
			self.load_map_data(LEVELS[self.level])
			self.new()

	def draw(self):
		'''
			fills the surface black, then calls draw() on all sprites in the allsprites group
			lastly, display.flip() to display changes.
		'''

		self.screen.fill(BLACK)
		self.screen.blit(self.background, (0, 0))
		self.allsprites.draw(self.screen)
		
		### Show the score, lives left and bricks remaining at the top of the screen
		self.message_to_screen("SCORE: " + str(self.score)  + "  LIVES: "+ str(self.player_lives) + "   BRICKS: " + str(self.brick_count), GREEN, -(HEIGHT * 0.45))
		pg.display.flip()

	###################################################################

	############## UTILITY FUNCTIONS ###################
	
	###	DRAW THE LEVEL MAP 

	def load_map_data(self, filename):
		'''
			Load the textfile with the map data
		'''
		gamefolder = path.dirname(__file__)
		self.map = self.create_map(path.join(gamefolder, filename ))
		
	def create_map(self, filename):
		'''
			Create a list with map objects to use in draw_map function
		'''
		self.map_data = []
		with open(filename, "rt") as file:
			for line in file:
				self.map_data.append(line)

	def draw_map(self):
		'''
			Draw the bricks on the playing surface from map-file
		'''
		for row, tiles in enumerate(self.map_data):
			for column, tile in enumerate(tiles):
				if tile == "-":
					startx = column * (GRID_SIZE_X + 5) + 1
					starty = row * (GRID_SIZE_Y + 5) + 1
					self.brick = brick.Brick(self.brick_image, startx, starty)
					self.bricksprite.add(self.brick)
					self.allsprites.add(self.brick)
					#self.brick_count += 1
				
				if tile == "B":
					ballstartx = column * GRID_SIZE_X
					ballstarty = row * GRID_SIZE_Y
					self.ball = ball.Ball(self.ball_image, ballstartx, ballstarty)
					self.ballsprite.add(self.ball)
					self.allsprites.add(self.ball)
			

	### FUNCTIONS FOR DRAWING TEXT ON SCREEN

	def text_obj(self, text, color, size):
		'''
			return a surface with rendered text based on size given as parameter when calling function
		'''
		if size == "small":
			textsurface = self.SMALLTEXT.render(text, True, color)
		elif size == "medium":
			textsurface = self.MEDIUMTEXT.render(text, True, color)
		elif size == "large":
			textsurface = self.LARGETEXT.render(text, True, color)

		return textsurface, textsurface.get_rect()

	def message_to_screen(self, text, color, Y_OFFSET = 0, size = "small"):
		'''
			displays the text on screen
		'''
		textSurf, textRect = self.text_obj(text, color, size)
		textRect.center = int((WIDTH / 2)), int((HEIGHT / 2) + Y_OFFSET)
		self.screen.blit(textSurf, textRect)


	###	LOAD ALL GAME IMAGES

	def load_introimage(self):
		self.intro_image = pg.image.load("images/startup.png")
		self.scaled_intro = pg.transform.scale(self.intro_image, (WIDTH, HEIGHT))
		return self.scaled_intro
	def load_gameover_image(self):
		self.gameover_image = pg.image.load("images/gameover.png")
		self.scaled_gameover = pg.transform.scale(self.gameover_image, (WIDTH, HEIGHT))
		return self.scaled_gameover
	def load_paused_image(self):
		self.paused_image = pg.image.load("images/paused.png")
		self.scaled_paused = pg.transform.scale(self.paused_image, (WIDTH, HEIGHT))
		return self.scaled_paused
	def load_background(self):
		self.background = pg.image.load("images/bkgnd.jpg")
		self.scaled_background = pg.transform.scale(self.background, (WIDTH, HEIGHT))
		return self.scaled_background
	def load_ball(self):
		self.ball_image = pg.image.load("images/ball.png")
		self.scaled_ball = pg.transform.scale(self.ball_image, BALL_SIZE)
		return self.scaled_ball
	def load_player(self):
		self.player_image = pg.image.load("images/paddle.png")
		self.scaled_player_image = pg.transform.scale(self.player_image, PLAYER_SIZE)
		return self.scaled_player_image
	def load_brick(self):
		self.brick_image = pg.image.load("images/brick.png")
		self.scaled_brick_image = pg.transform.scale(self.brick_image, (GRID_SIZE_X, GRID_SIZE_Y))
		return self.scaled_brick_image
	def load_level_complete(self):
		self.level_complete_image = pg.image.load("images/level_complete.png")
		self.scaled_level_complete_image = pg.transform.scale(self.level_complete_image, (WIDTH, HEIGHT))
		return self.scaled_level_complete_image

	### Start the GAME

game = Game()

while game.running:
	game.introscreen()
	pg.quit()
	sys.exit()













