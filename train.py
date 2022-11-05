import sys
import pygame

from vehicle import Vehicle

class Train(Vehicle):

    def __init__(self, JimRs_Garage):

        super().__init__(JimRs_Garage)

        self.settings.speed_vert = 3
        self.settings.speed_hor = 5

    def blit_train(self):

        self.screen.blit(self.image, self.rect)