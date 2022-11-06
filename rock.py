import pygame
import random
from obstacle import Obstacle

class Rock(Obstacle):

    def __init__(self, Goat_Upgrader, image):

        super().__init__(Goat_Upgrader, image)

        self.rect.x = random.randint(0, self.settings.width - self.rect.width)

        self.damage = 45