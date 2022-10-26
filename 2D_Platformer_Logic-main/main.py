import pygame, sys
from settings import * 
from level import Level
from pygame.locals import *
import pytmx
from pytmx.util_pygame import load_pygame



# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Nostalgia')
clock = pygame.time.Clock()

level = Level()
world_offset = [0,0]



while True:
	# event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	screen.fill(BG_COLOR)
	level.run()
	

	# drawing logic
	pygame.display.update()
	clock.tick(60)