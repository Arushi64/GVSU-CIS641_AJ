import pygame
from support import import_csv_layout


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        
        # function imported from support.py
        # terrain_layout = import_csv_layout(level_data['terrain'])
        terrain_layout = '../code/0/level_0_terrain.csv'


    def run(self):
        # run entire game
        pass