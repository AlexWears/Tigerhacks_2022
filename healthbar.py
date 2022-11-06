import sys
import pygame

class HealthBar(pygame.sprite.Sprite):

    def __init__(self, Goat_Upgrader):

        self.settings = Goat_Upgrader.settings
        self.screen = Goat_Upgrader.screen
        self.health = self.settings.health

        self.initialize()


    def initialize(self):
        
        self.health = self.settings.health

        #initial health bar
        self.height1 = 50
        self.width1 = (self.health * 5)
        self.HB_rect = pygame.Rect(50,50, self.width1, self.height1)
        self.HBcolor = (120, 30, 20)
        self.HB_rect.topleft = (50, 50)

        #back of health bar (black bar)
        self.height2 = 60
        self.width2 = 760
        self.BG_rect = pygame.Rect(45,45, self.width2, self.height2)
        self.BGcolor = (0, 0, 0)
        self.BG_rect.topleft = (45, 45)

        #initial print of healthbar
        pygame.draw.rect(self.screen, self.BGcolor, self.BG_rect)
        pygame.draw.rect(self.screen, self.HBcolor, self.HB_rect)

    def update(self):
        self.initialize()
        pygame.draw.rect(self.screen, self.BGcolor, self.BG_rect)
        pygame.draw.rect(self.screen, self.HBcolor, self.HB_rect)
