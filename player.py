import pygame
from support import base_path, folder_import
import os



class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        #self.image_path = os.path.join(base_path, "img", "char", "idle", "idle_1.png")
        self.animations = {"idle": [], "run": [], "jump": [],"walk": [], "dead": []}
        self.import_character()
        self.frame_index = 0
        self.image = self.animations["idle"][self.frame_index].convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0,0)
        self.on_ground = True
        self.speed = 6
        self.run_speed = 0.08
        self.gravity = 0.7
        self.jump_speed = -17
        self.status = "idle"
        self.facing_forward = True
        self.animation_speed = 0.15
        self.looking_mode = False

    def import_character(self):
        char_path = os.path.join(base_path, "img", "char")

        for animation in self.animations.keys():
            full_path = os.path.join(char_path, animation)
            self.animations[animation] = folder_import(full_path)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed

        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        image = animation[int(self.frame_index)]
        if self.facing_forward:
            self.image = image
        else:
            filpped_image = pygame.transform.flip(image, True, False)
            self.image = filpped_image

    def jump(self):
        self.direction.y = self.jump_speed




    def gravity_apply(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y




    def keyboard_input(self):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_RIGHT]:
            self.status = "walk"
            self.direction.x = 1
            self.facing_forward = True


        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_forward = False  
            self.status = "walk"  

        else:
            self.direction.x = 0
            self.status = "idle"

        if keys[pygame.K_SPACE] and self.on_ground:
            self.on_ground = False
            self.status = "jump"
            self.jump()
        
        if keys[pygame.K_LEFT] and keys[pygame.K_LCTRL]:
            self.status = "run"
            self.direction.x -= self.speed * self.run_speed

        if keys[pygame.K_RIGHT] and keys[pygame.K_LCTRL]:
            self.status = "run"
            self.direction.x += self.speed * self.run_speed
            
        if keys[pygame.K_DOWN] and self.status == "idle":
            self.looking_mode = True


                

        





    def get_status(self):
        if self.direction.y < 0:
            self.status = "jump"
        else:
            if self.direction.x != 0:
                self.status = "walk"
            else:
                self.status = "idle"
    
    def update(self):
        self.keyboard_input()
        self.get_status()
        self.animate()
        


