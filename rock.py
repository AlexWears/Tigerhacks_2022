import pygame
import random
from obstacle import Obstacle

class Rock(Obstacle):

    def __init__(self, JimRs_Garage, image):

        super().__init__(JimRs_Garage, image)

        self.rect.x = random.randint(0, self.settings.width - self.rect.width)