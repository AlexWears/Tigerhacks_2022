import sys
import pygame
from settings import Settings

class Vehicle:

    def __init__(self, JimRs_Garage):
        self.settings = JimRs_Garage.settings
        self.screen = JimRs_Garage.screen
        self.screen_rect = JimRs_Garage.screen.get_rect()
        self.image = pygame.image.load("sprites/thing.bmp")
        
        self.rect = self.image.get_rect()

        self.rect.bottomleft = (self.settings.width/2,self.settings.height/2)

    def blit_vehicle(self):
        self.screen.blit(self.image, self.rect)

    def update(self):

        # if(self.settings.v_type == 1):
        #     self.image = pygame.image.load("sprites/goat.bmp")
        # elif(self.settings.v_type == 2):
        #     self.image = pygame.image.load("sprites/train.bmp")
        # elif(self.settings.v_type == 3):
        #     self.image = pygame.image.load("sprites/car.bmp")
        # elif(self.settings.v_type == 4):
        #     self.image = pygame.image.load("sprites/plane.bmp")

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
        
        if 
    
        self.blit_vehicle()
