import pygame
import os
from support import base_path
from settings import screen_width, screen_height, level_map
from level import Level
from states import start_state, run_state, game_over




pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Super Sisters @ LoveQuinn 1.0")


clock = pygame.time.Clock()

bg = os.path.join(base_path,"img","BG.png")
bg_surf = pygame.image.load(bg).convert_alpha()
bg_rect = bg_surf.get_rect(bottomleft=(0, screen_height))
bg_resize = pygame.transform.smoothscale(bg_surf, (screen_width*1.5, screen_height*1.5))

bg_02 = os.path.join(base_path,"img","BG_2.png")
bg_02_surf = pygame.image.load(bg_02).convert_alpha()
bg_02_rect = bg_surf.get_rect(bottomleft=(0, screen_height+100))
bg_02_resize = pygame.transform.smoothscale(bg_02_surf, (screen_width*1, screen_height*1))

running = True


level = Level(None, screen)



while running:
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()


    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if level.state == start_state:
                level.check_click(event.pos)


        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            if level.start_rect.collidepoint(mouse_pos):
                level.hovered_button = "start"
            elif level.quit_rect.collidepoint(mouse_pos):
                level.hovered_button = "quit"
            else:
                level.hovered_button = None





    screen.blit(bg_resize, bg_rect)


    if level.state == run_state:
        screen.blit(bg_02_resize, bg_02_rect)
        level.run()

    if game_over:
        pass
    
    if level.state == start_state:
        level.menu_window()

    pygame.display.update()

    clock.tick(60)


pygame.quit()