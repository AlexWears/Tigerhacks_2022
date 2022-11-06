import sys
import pygame
import random

class Coin(pygame.sprite.Sprite):

    def __init__(self, Goat_Upgrader):

        super().__init__()

        self.settings = Goat_Upgrader.settings
        self.screen = Goat_Upgrader.screen

        self.image = pygame.image.load("sprites/DeSo.bmp")
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.x = random.randint(0, self.settings.width - self.rect.width)

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.settings.env_speed
        self.blit()

        