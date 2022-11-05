import pygame
import sys
from settings import *
from level import Level
import csv
# from support import import_csv_layout
from game_data import Test_Level_1
from tiles import *
import pytmx
from pytmx.util_pygame import load_pygame

# not using specs below- instead using specs declared in settings.py
# width, height = 1280, 720
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
screen = pygame.display.set_mode((1024,768))
clock = pygame.time.Clock()
level = Level(Test_Level_1,screen)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	if save_button.draw(screen):
		with open(f'level{Test_Level_1}_data.csv', 'w', newline='') as csvfile:
			writer = csv.writer(csvfile, delimiter=',')
			for row in world_data:
				writer.writerow(row)
	load_button.draw(screen)

	screen.fill('grey')
	level.run()

	pygame.display.update()
	clock.tick(60)









# ensures main can only be run from this file and cannotbe imported
if __name__ == "__main__":
    main()

