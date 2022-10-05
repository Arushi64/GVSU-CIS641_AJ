import pygame
import sys
from settings import *
from level import Level
# from support import import_csv_layout
from game_data import level_0
# from tiles import *

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

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	window.fill(color1)
	level.run()

	pygame.display.update()
	clock.tick(FPS)

# def draw_window():
#     window.fill(color1)
#     pygame.display.update()

# def main(): 
#     run = True

#     # game will run until run is not true or you exit out of it
#     while run:

#         # check for events in pygame
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#                 # sys.exit()
        
#         level.run()
#         draw_window()
        

#     pygame.quit()





















# ensures main can only be run from this file and cannotbe imported
if __name__ == "__main__":
    main()

