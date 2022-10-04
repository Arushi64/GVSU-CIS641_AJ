import pygame
from settings import *
from level import Level

# not using specs below- instead using specs declared in settings.py
# width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Nostalgia")
clock = pygame.time.Clock()
level = Level(level_data, window)


white = (255,255,255)
color1 = (250,235,215)

FPS = 60

def draw_window():
    window.fill(color1)
    pygame.display.update()



def main(): 
    run = True

    # game will run until run is not true or you exit out of it
    while run:

        # check for events in pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()

    pygame.quit()





















# ensures main can only be run from this file and cannotbe imported
if __name__ == "__main__":
    main()

