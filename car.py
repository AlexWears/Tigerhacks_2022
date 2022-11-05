import sys
import pygame

from vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, JimRs_Garage):

        super().__init__(JimRs_Garage)

        self.image = pygame.image.load("sprites/car.bmp")
        self.rect = self.image.get_rect()

        self.settings.speed_vert = self.settings.car_speed_vert
        self.settings.speed_hor = self.settings.car_speed_hor

    def blit_car(self):

        self.screen.blit(self.image, self.rect)
