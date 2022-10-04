import pygame
from settings import *

# not using specs below- instead using specs declared in settings.py
# width, height = 1280, 720
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dangerous Dave")

WHITE = (255,255,255)
COLOR1 = (230,45,24)

FPS = 60

def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()


# main game function 
def main():
    # clock = pygame.time.Clock(FPS = 60) # caps fps at x frames per second 
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

