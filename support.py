import sys
import os
from os import walk 
import pygame

base_path = getattr(sys,"_MEIPASS", os.path.dirname(os.path.abspath(__file__)))

def folder_import(path):
    surface_list = []
    for way, list, files in walk(path):
        for image in files:
            full_path = os.path.join(way, image)
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list




