import sys
import pygame

from vehicle import Vehicle

class Goat(Vehicle):

    def __init__(self, JimRs_Garage):
        
        super().__init__(JimRs_Garage)

    def blit_goat(self):
        
        self.screen.blit(self.image, self.rect)