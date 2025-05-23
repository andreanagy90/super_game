import pygame
import os
from support import base_path

level_map =[
    "                                                                               ",
    "   noooooooooop     nop nop nop     np                                         ",
    "                                 2    abbbbbc  1      2   2     5              ",
    "                                     eeeeeeeeeeef   nooooooop  nop             ",
    "                                                                       2       ",
    "                                                         4   5      nooooop    ",
    "                                                       nooooooop 2             ",
    "                                   1                             np            ",
    "                                  nop                         15       nop     ",
    "                           nop         nop                   nop               ",
    "                          151 25 3        2 3           3   3   c   53         ",
    "                        23abbbbbbbbc      nooop         noooop     noooop      ",
    "  P5  312  1  35       abbeeeeeeeeeec              1       df             np   ",
    "3abbbbbbbbbbbbbbbc    abbbbbbbbbbbbbbc           abbbc        np             np",
    "deeeeeeeeeeeeeeeeef deeeeeeeeeeeeeeeef          deeeeef deeee         eeeeeeeef"]

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
others = {"1":"cactus",
          "2":"plant",
          "3":"rock",
          "4":"skeleton",
          "5":"tree",
          "H":"heart"
          }

tresaures = ["key", "big_jump"]


