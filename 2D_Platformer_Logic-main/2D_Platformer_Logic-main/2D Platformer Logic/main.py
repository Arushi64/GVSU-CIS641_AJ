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

def blit_all_tiles(window, tmxdata, world_offset):
	for layer in tmxdata:
		for tile in layer.tiles():
			#tiles[0]....x grid location
			#tiles [1].....y grid location 
			x_pixel = tile[0] * 70 + world_offset[0]
			y_pixel = tile[1] * 70 + world_offset[1]
			window.blit(tile[2],(x_pixel, y_pixel))

def main5():
	tmxdata = load_pygame("Levels\Level 1.tmx")


while True:
	# event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	screen.fill(BG_COLOR)
	blit_all_tiles(window = pygame.display.set_mode((1280, 720)),tmxdata = load_pygame("C:/Users/arush/OneDrive/Documents/GVSU/Fall 22/641/Github 641/GVSU-CIS641_AJ/Levels/Level 1.tmx"),world_offset =[0,0])
	level.run()
	

	# drawing logic
	pygame.display.update()
	clock.tick(60)