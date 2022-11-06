import sys
import pygame
from settings import Settings

class Vehicle(pygame.sprite.Sprite):

    pygame.mixer.init()

    def __init__(self, Goat_Upgrader):
        self.settings = Goat_Upgrader.settings
        self.screen = Goat_Upgrader.screen
        self.screen_rect = Goat_Upgrader.screen.get_rect()
        self.image = pygame.image.load("sprites/thing.bmp")
        self.health = self.settings.health
        self.scale_i = 1
        self.fly_i = 0
        self.fuel = 0
        self.fly_choice = 0
        
        self.rect = self.image.get_rect()

        self.rect.bottomleft = (self.settings.width/2,self.settings.height/2)

    def blit_vehicle(self):
        self.screen.blit(self.image, self.rect)

    def update(self):

        if self.settings.moving_right and self.rect.right < self.settings.width:
            self.rect.x += self.settings.speed_hor
        if self.settings.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.speed_hor
        if self.settings.moving_down and self.rect.bottom < self.settings.height:
            self.rect.y += self.settings.speed_vert
        if self.settings.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.speed_vert

        if self.rect.bottom < self.settings.height:
            self.rect.y += self.settings.env_speed
    
        self.blit_vehicle()

    def play_hurt_sound(self):

        self.hurt_sound = pygame.mixer.Sound("sounds/goathurt.ogg")
        pygame.mixer.Sound.play(self.hurt_sound)

    def play_dead_sound(self):

        self.dead_sound = pygame.mixer.Sound("sounds/goatdead.ogg")
        pygame.mixer.Sound.play(self.dead_sound)

    def fly(self, image):
        if(self.settings.v_type != 4 and self.settings.v_type != 5):
            print("here")
            print(self.settings.v_type)
            return
        print("fly choice =" + str(self.fly_choice))
        if(self.fuel > 0 and self.fly_choice == 1):
            print("inside")
            if self.scale_i < 20:
                pygame.transform.scale(self.image, (116*self.scale_i,116*self.scale_i))
                self.scale_i += 1
                print("iterator =" + str(self.scale_i))
                return
            if(self.fly_i == 0): 
                self.image = pygame.image.load("sprites/thing.bmp")
                self.fly_i += 1
                print("fly_i = " + str(self.fly_i))
            self.fuel -= 1
            print("fuel =" + str(self.fuel))
            if(self.fuel <= 0):
                self.image = image
                self.fly_i = 0
                self.scale_i = 1
                self.fly_choice = 0
        print("nothing")
        return
            

