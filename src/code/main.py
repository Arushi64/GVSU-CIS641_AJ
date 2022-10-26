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



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	window.fill(color1)
	blit_all_tiles(window = pygame.display.set_mode((1280, 720)),tmxdata = load_pygame("2D_Platformer_Logic-main/Level 1.tmx"),world_offset =[0,0])

	level.run()

	pygame.display.update()
	clock.tick(FPS)









# ensures main can only be run from this file and cannotbe imported
if __name__ == "__main__":
    main()

