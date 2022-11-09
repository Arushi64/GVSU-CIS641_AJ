from settings import vertical_tile_number, tile_size, screen_width
import pygame
from tiles import AnimatedTile

class Sky:
    def __init__(self, horizon):
        self.top = pygame.image.load('src/code/graphics/sky/sky_bottom.png').convert_alpha()
        self.bottom = pygame.image.load('src/code/graphics/sky/sky_bottom.png').convert_alpha()
        self.middle = pygame.image.load('src/code/graphics/sky/sky_middle.png').convert_alpha()
        self.horzion = horizon

        # stretch
        self.top = pygame.transform.scale(self.top, (screen_width, tile_size))
        self.bottom = pygame.transform.scale(self.bottom, (screen_width, tile_size))
        self.middle = pygame.transform.scale(self.middle, (screen_width, tile_size))

    def draw(self, surface):
        for row in range(vertical_tile_number):
            y = row * tile_size
            if row < self.horzion:
                surface.blit(self.top, (0, y))
            elif row == self.horzion:
                surface.blit(self.middle, (0, y))
            else:
                surface.blit(self.bottom, (0, y))

class Water:
    def __init__(self, top, level_width):
        water_start = -screen_width
        water_tile_width = 100
        tile_x_amount = int((level_width + screen_width) / water_tile_width)
        self.water_sprites = pygame.sprite.Group()

        for tile in range(tile_x_amount):
            x = tile * water_tile_width + water_start
            y = top
            sprite = AnimatedTile(100, x, y, 'src/code/graphics/water')
            self.water_sprites.add(sprite)

    def draw(self, surface, shift):
        self.water_sprites.update(shift)
        self.water_sprites.draw(surface)