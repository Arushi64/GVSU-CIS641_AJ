import pygame
color2 = (250,125,215)
class Tile(pygame.sprite.Sprite):

    def __init__(self,size, x,y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color2)
        self.rect = self.image.get_rect(topleft = (x,y))