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

        self.rect.bottomleft = (900,700)

    def blit_vehicle(self):
        self.screen.blit(self.image, self.rect)

    def update(self):

        if self.settings.moving_right == True:
            self.rect.x += self.settings.speed_hor
        if self.settings.moving_left == True:
            self.rect.x -= self.settings.speed_hor
        if self.settings.moving_down == True:
            self.rect.y += self.settings.speed_vert
        if self.settings.moving_up == True:
            self.rect.y -= self.settings.speed_vert
    
        self.blit_vehicle()
