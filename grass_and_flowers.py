import sys
import pygame
import random

class Grass(pygame.sprite.Sprite):

    def __init__(self, Goat_Upgrader):

        super().__init__()

        self.settings = Goat_Upgrader.settings
        self.screen = Goat_Upgrader.screen
        self.screen_rect = Goat_Upgrader.screen.get_rect()

        self.image = pygame.image.load("sprites/Grass.bmp")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0,0)

        self.y = 0
        self.x = random.randint(0, self.settings.width - self.rect.width)

    def blit_grass(self):

        self.screen.blit(self.image, self.rect)

    def update(self):

        self.y += self.settings.env_speed
        self.rect.y = self.y
        self.rect.x = self.x
        self.blit_grass()

class Flower(pygame.sprite.Sprite):

    def __init__(self, Goat_Upgrader):

        super().__init__()

        self.settings = Goat_Upgrader.settings
        self.screen = Goat_Upgrader.screen
        self.screen_rect = Goat_Upgrader.screen.get_rect()

        self.image = pygame.image.load("sprites/YellowFlower.bmp")

        if random.randint(1,2) % 2 == 0:
            self.image = pygame.image.load("sprites/RedFlower.bmp")

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0,0)

        self.y = 0
        self.x = random.randint(0, self.settings.width - self.rect.width)

    def blit_flower(self):

        self.screen.blit(self.image, self.rect)

    def update(self):

        self.y += self.settings.env_speed
        self.rect.y = self.y
        self.rect.x = self.x
        self.blit_flower()