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


class TiledMap:
	def __init__(self, filename):
		tm = pytmx.load_pygame(filename, pixelalpha=True)
		self.width = tm.width * tm.tilewidth
		self.height = tm.height * tm.tileheight
		self.tmxdata = tm

	def render(self, surface):
		ti = self.tmxdata.get_tile_image_by_gid
		for layer in self.tmxdata.visible_layers:
			if isinstance(layer, pytmx.TiledTIleLayer):
				for x, y, gid, in layer:
					tile = ti(gid)
					if tile:
						surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata))

def make_map(self):
	temp_surface = pg.pygame.Surface.Surface((self.width, self.height))
	self.render(temp_surface)
	return temp_surface



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	window.fill(color1)
	blit_all_tiles(window = pygame.display.set_mode((1280, 720)),tmxdata = load_pygame("src/code/Level_1_Tiled/Test_Level_1.tmx"),world_offset =[0,0])
	level.run()
	

	pygame.display.update()
	clock.tick(FPS)










# ensures main can only be run from this file and cannotbe imported
if __name__ == "__main__":
    main()

