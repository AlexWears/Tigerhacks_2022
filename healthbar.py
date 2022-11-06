import sys
import pygame

class HealthBar(pygame.sprite.Sprite):

    def __init__(self, JimRs_Garage):

        self.settings = JimRs_Garage.settings
        self.screen = JimRs_Garage.screen
        self.health = self.settings.health

        self.initialize()


    def initialize(self):
        
        #initial health bar
        self.height1 = 50
        self.width1 = (self.health * 5)
        self.HB_rect = pygame.Rect(50,50, self.width1, self.height1)
        self.HBcolor = (215, 60, 55)
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
