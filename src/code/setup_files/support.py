from os import walk
import pygame

def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
        if image != '.DS_Store': #if the filename is not .DS_Store then do the following
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list