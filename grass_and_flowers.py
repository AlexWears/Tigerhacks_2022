import sys
import pygame
import random

class Grass_and_flowers(pygame.sprite.Sprite):

    def __init__(self, JimRs_Garage):

        super().__init__()

        self.settings = JimRs_Garage.settings
        self.screen = JimRs_Garage.screen
        self.screen_rect = JimRs_Garage.screen.get_rect()

        self.image = pygame.image.load("sprites/Grass.bmp")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0,0)

        self.y = 0
        self.x = random.randint(0, self.settings.width)

    def blit_grass(self):

        self.screen.blit(self.image, self.rect)

    def update(self):

        self.y += self.settings.env_speed
        self.rect.y = self.y
        self.blit_grass()
    