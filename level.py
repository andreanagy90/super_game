import pygame
from settings import tile_size, screen_height, screen_width, others, platforms, font_import, level_map, start_y
from states import start_state, game_over, run_state
from tiles import TerrainTile, OtherTiles
from player import Player
import sys

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.terrain_tiles = pygame.sprite.Group()
        self.other_tiles = pygame.sprite.Group()
        self.hovered_button = None
        self.state = start_state
        self.player = pygame.sprite.GroupSingle()
        self.start_rect = pygame.Rect(0,0,0,0)
        self.quit_rect = pygame.Rect(0,0,0,0)
        self.worldshift_x = 0
        self.worldshift_y = 0
        self.looking = False
   

    def menu_window(self):
        fonts = font_import()
        mouse_pos = pygame.mouse.get_pos()
        s_color = (70, 70, 70)
        q_color = (70, 70, 70)

        if self.hovered_button == "start":
            s_color = "black"
        elif self.hovered_button == "quit":
            q_color = "black"

        main_font = pygame.font.Font(fonts["mario"], 84)
        menu_font = pygame.font.Font(fonts["domino"], 42)
        menu_font_02 = pygame.font.Font(fonts["arcade"], 42)

        main_text = main_font.render("Super Sisters", True, (255,255,255))
        text_rect = main_text.get_rect(center=(screen_width/2, screen_height/4))
        self.display_surface.blit(main_text, text_rect)

        start_text = menu_font.render(" -New Game- ", True, s_color)
        start_rect = start_text.get_rect(center=(screen_width/2, screen_height /2 +30 ))
        self.start_rect = start_rect       

        quit_text = menu_font.render(" -Quit- ", True, q_color)
        quit_rect = quit_text.get_rect(center=(screen_width/2, screen_height /2 +120))
        self.quit_rect= quit_rect


        self.display_surface.blit(start_text, start_rect)
        pygame.draw.rect(self.display_surface, (120, 120, 120), start_rect, width=3, border_radius=5)
        self.display_surface.blit(quit_text, quit_rect)
        pygame.draw.rect(self.display_surface, (120, 120, 120), quit_rect, width=3, border_radius=5)


    def check_click(self, mouse_pos):
        if self.start_rect.collidepoint(mouse_pos):
            self.state = run_state
            self.setup_level(level_map)
        elif self.quit_rect.collidepoint(mouse_pos):
            pygame.quit()
            sys.exit()

    def setup_level(self, layout):
        for row_index, row in enumerate (layout):
            for col_index, tile_type in enumerate(row):
                x = col_index*tile_size
                y = row_index *tile_size
                y_on_screen = y- start_y
                if tile_type in others:
                    tile = OtherTiles(tile_size, x, y_on_screen, tile_type)
                    self.other_tiles.add(tile)
                elif tile_type == "P":
                    player_sprite = Player((x,y_on_screen))
                    self.player.add(player_sprite)

                #elif tile_type != " ":
                elif tile_type in platforms:
                    tile = TerrainTile(tile_size,x,y_on_screen,tile_type)
                    self.terrain_tiles.add(tile)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        
        direction_x = player.direction.x
        


        if player_x < screen_width / 4 and direction_x < 0:
            self.worldshift_x = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.worldshift_x = -8
            player.speed = 0
        else:
            self.worldshift_x = 0
            player.speed = 7

    def scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.y
        direction_y = player.direction.y
        camera_y = screen_height - 150
                


        if player_y < screen_height / 5 :
            self.worldshift_y = 8

            
            
        elif player_y > camera_y - 64 and direction_y > 0:
            self.worldshift_y = -16

            
        else:
            self.worldshift_y = 0

    def looking_on_map(self):
        player = self.player.sprite



        if player.looking_mode and player.rect.y >= screen_height / 3:
           target_shift = -16
        else:
            target_shift = 0


        if self.worldshift_y < target_shift:
            self.worldshift_y += 1
            if self.worldshift_y > target_shift:
                self.worldshift_y = target_shift
        elif self.worldshift_y > target_shift:
            self.worldshift_y -= 1
            if self.worldshift_y < target_shift:
                self.worldshift_y = target_shift

        self.worldshift_y = int(self.worldshift_y)


            



    def vertical_collision(self):
        player = self.player.sprite
        player.gravity_apply()

        for tiles in self.terrain_tiles.sprites():
            if tiles.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = tiles.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                    
                elif player.direction.y < 0:
                    player.rect.top = tiles.rect.bottom
                    player.direction.y = 0

    def move_player(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        

    def horizontal_collision(self):
        player = self.player.sprite
        for sprite in self.terrain_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                    if player.direction.x > 0 :
                        player.rect.right = sprite.rect.left
                    if player.direction.x < 0 :
                         player.rect.left = sprite.rect.right
                


    def run(self):
        self.player.update()
        self.move_player()
        self.scroll_x()
        if self.player.sprite.looking_mode:
            self.looking_on_map()
        else:
            self.scroll_y()
        self.vertical_collision()
        self.horizontal_collision()
        self.terrain_tiles.update(self.worldshift_x, self.worldshift_y)
        self.terrain_tiles.draw(self.display_surface)
        self.other_tiles.update(self.worldshift_x, self.worldshift_y)
        self.other_tiles.draw(self.display_surface)
        self.player.draw(self.display_surface)



        


    