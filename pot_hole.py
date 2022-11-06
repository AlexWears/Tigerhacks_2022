import pygame
import random
from obstacle import Obstacle

class PotHole(Obstacle):

    def __init__(self, JimRs_Garage, image):

        super().__init__(JimRs_Garage, image)

        self.rect.x = random.randint(self.settings.road_left, self.settings.road_left + self.settings.road_width - self.rect.width)
        self.damage = 20