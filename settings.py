import pygame
import os
from support import base_path

level_map =[
    "C                                                                             C",
    "C                                                                             C",
    "C                                                                             C",
    "C                                                                             C",
    "C                                                                             C",
    "C                                                                             C",
    "C                                                                             C",
    "C                                                           ghhhhhhhi         C",
    "C                                                                             C",
    "C                                                                        ghi  C",
    "C                                                                  ghi        C",
    "C                                                           ghhi            giC",
    "C                   ghi   ghi            ghhhhhhhhhhhhhi                      C",
    "C 7 P1 2      abc                                                        abbbcC",
    "abbbbbbbbbcqqqjklqqqqqqqqqqqqqabbbbbbbbbbcqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",
    "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
    "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
    ]

tile_size = 64

screen_width = 1200
screen_height = 800

world_width = len(level_map[0]) * tile_size
world_height = len(level_map)* tile_size
start_y = world_height - screen_height

def font_import():
    mario_font = os.path.join(base_path, "fonts", "mario.ttf")
    domino_font = os.path.join(base_path, "fonts", "main.ttf")
    arcade_font = os.path.join(base_path, "fonts", "ARCADEPI.TTF")
    return {
        "mario": mario_font,
        "domino": domino_font,
        "arcade": arcade_font
    }




platforms = ["a", "b", "c", "d", "e", "f","g","h", "i", "j", "k", "l", "n", "o", "p", "t", "y", "z"]
others = {"1":"Sign_2",
          "2":"tree",
          "3":"Tree_2",
          "4":"Tree_3",
          "5":"bush1",
          "H":"heart",
          "q":"q",
          "s":"s",
          "6":"bush4",
          "7":"Mushroom_1",
          "8": "Mushroom_2",
          "9": "Stone",
          "0": "Crate",
          "E": "elephant"}

tresaures = ["key", "big_jump"]


