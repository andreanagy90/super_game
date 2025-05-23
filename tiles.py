import pygame
from settings import others, platforms
from support import base_path
import os




class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft= (x,y))
        

    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y

class TerrainTile(Tile):
    def __init__(self, size, x, y, terrain_type):
        super().__init__(size, x, y)
        self.path = os.path.join(base_path, "img", "terrain", terrain_type + ".png")
        self.image= pygame.image.load(self.path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x,y))

class OtherTiles(Tile):
    def __init__(self, size, x, y, type):
        super().__init__(size, x, y)
        self.path = os.path.join(base_path, "img", "others",f"{others[type]}.png")
        self.image= pygame.image.load(self.path).convert_alpha()
        self.rect = self.image.get_rect(bottomleft=(x,(y + size)))

    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y

class Crate:
    pass