import pygame
import csv
from support import import_csv_layout
from settings import * 
from tiles import *


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        
        # import_Csv function imported from support.py

        # set up the background(terrain)- using graphics instead of terrain for testing
        background_layout = import_csv_layout(level_data['background'])
        # ensures we are only looking at the terrain graphic 
        self.terrain_sprites = self.create_tile_group(background_layout, 'background')

    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != -1:
                    x = col_index * 16
                    y = row_index * 16

                    if type == 'background':
                        sprite = Tile(16, x, y)
                        sprite_group.add(sprite)
        return sprite_group



    def run(self):
        # run entire game
        pass