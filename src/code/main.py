import pygame
import sys
from settings import *
from level import Level
# from support import import_csv_layout
from game_data import level_0
from tiles import *
import pytmx
from pytmx.util_pygame import load_pygame

# not using specs below- instead using specs declared in settings.py
# width, height = 1280, 720
pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Nostalgia")


clock = pygame.time.Clock()
level = Level(level_0, window)


white = (255,255,255)
color1 = (250,235,215)
FPS = 60

test_surface = pygame.Surface((10,20))
test_surface.fill('Purple')

def blit_all_tiles(window, tmxdata, world_offset):
	for layer in tmxdata:
		for tile in layer.tiles():
			#tile[0]...x grid location
			#tile[1]...y grid location
			#tiles[2]...image data for blitting
			x_pixel = tile[0] * 64 + world_offset[0]
			y_pixel = tile[1] * 64 + world_offset[1]
			window.blit(tile[2], (x_pixel, y_pixel))



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	window.fill(color1)
	blit_all_tiles(window = pygame.display.set_mode((1280, 720)),tmxdata = load_pygame("C:/Users/arush/OneDrive/Documents/GVSU/Fall 22/641/Github 641/GVSU-CIS641_AJ/src/code/1/Level 1_Export.tmx"),world_offset =[0,0])

	# blit_all_tiles(window = pygame.display.set_mode((1280, 720)),tmxdata = load_pygame("C:/Users/arush/Downloads/2D-Mario-style-platformer-main/2 - Level/2 - Level/levels/level_data/level_0.tmx"),world_offset =[0,0])
	level.run()

	pygame.display.update()
	clock.tick(FPS)









# ensures main can only be run from this file and cannotbe imported
if __name__ == "__main__":
    main()

