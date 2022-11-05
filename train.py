import sys
import pygame

from vehicle import Vehicle

class Train(Vehicle):

    def __init__(self, JimRs_Garage):

        super().__init__(JimRs_Garage)

        self.image = pygame.image.load("sprites/train.bmp")

        self.settings.speed_vert = self.settings.train_speed_vert
        self.settings.speed_hor = self.settings.train_speed_hor

    def blit_train(self):

        self.screen.blit(self.image, self.rect)