import pygame
import random
from obstacle import Obstacle

class Tree(Obstacle):

    def __init__(self, JimRs_Garage, image):

        super().__init__(JimRs_Garage, image)

        self.rect.x = random.randint(0, self.settings.width)

        while self.rect.x > self.settings.road_left and self.rect.right < self.settings.road_left + self.settings.road_width:
            self.rect.x = random.randint(0, self.settings.width)