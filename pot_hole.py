import pygame
import random
from obstacle import Obstacle

class PotHole(Obstacle):

    def __init__(self, Goat_Upgrader, image):

        super().__init__(Goat_Upgrader, image)

        self.rect.x = random.randint(self.settings.road_left, self.settings.road_left + self.settings.road_width - self.rect.width)
        self.damage = 20