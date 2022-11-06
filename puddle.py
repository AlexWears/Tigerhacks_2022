import pygame
import random
from obstacle import Obstacle

class Puddle(Obstacle):

    def __init__(self, Goat_Upgrader, image):

        super().__init__(Goat_Upgrader, image)

        self.rect.x = random.randint(0, self.settings.width)

        while self.rect.right > self.settings.road_left and self.rect.right < self.settings.road_left + self.settings.road_width:
            self.rect.x = random.randint(0, self.settings.width)

        self.damage = 20