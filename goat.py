import sys
import pygame

from vehicle import Vehicle

class Goat(Vehicle):

    def __init__(self, JimRs_Garage):
        
        super().__init__(JimRs_Garage)
        
        self.image = pygame.image.load("sprites/goat.bmp")

        self.settings.speed_vert = self.settings.goat_speed_vert
        self.settings.speed_hor = self.settings.goat_speed_hor

    def blit_goat(self):
        
        self.screen.blit(self.image, self.rect)