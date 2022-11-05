import pygame
from sys import exit
from settings import *
# not using specs below- instead using specs declared in settings.py
# width, height = 1280, 720
pygame.init()
window = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Nostalgia")

clock = pygame.time.Clock()


white = (255,255,255)
color1 = (250,235,215)
FPS = 60

#defines size of the new regular surface
# test_surface = pygame.image.load('C:/Users/arush/OneDrive/Pictures/Camera Roll/WIN_20190419_09_43_11_Pro.jpg') 
#test_surface.fill('Purple')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #defines the position of the new regular surface
    window.blit('src/code/Level_1_Tiled/Test_Level_1.tmx',(400,10))
    pygame.display.update()
    clock.tick(FPS)


# # ensures main can only be run from this file and cannotbe imported
# if __name__ == "__main__":
#     main()