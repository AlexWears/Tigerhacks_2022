import pygame
import random
from obstacle import Obstacle

class CarObst(Obstacle):

    def __init__(self, JimRs_Garage, image):
    
        super().__init__(JimRs_Garage, image)
        self.speed = self.settings.env_speed + 3
        
        if random.randint(1,2) % 2 == 1:
            self.rect.left = int(self.settings.road_left + self.settings.road_width / 4)
        else:
            self.rect.left = int(self.settings.road_left + self.settings.road_width / 4 + self.settings.road_width / 2)