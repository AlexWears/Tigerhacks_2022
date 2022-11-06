import sys
import pygame
from settings import Settings
from BetterCryptoAPI import CryptoAPI

class DeSoPrice():

    def __init__(self, JimRs_Garage):

        

        self.font = pygame.font.SysFont("Comic Sans MS", 20)

        self.settings = JimRs_Garage.settings
        self.screen = JimRs_Garage.screen
        self.screen_rect = JimRs_Garage.screen.get_rect()
        self.initialize()

        

        #white box
        self.height = 40
        self.width = 100
        self.box_rect = pygame.Rect(50,50, self.width, self.height)
        self.color = (255, 255, 255)
        self.box_rect.bottomright = (self.settings.width - self.image.get_width() + 25, self.settings.height - 5)


    def initialize(self):
        self.settings.deso_conv = CryptoAPI.get_DeSo_price()

        self.image = pygame.image.load("sprites/DeSo.bmp")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.settings.width - self.image.get_width() - 10, self.settings.height - 10)

        self.text = self.font.render(str(self.settings.deso_conv), True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.bottomleft = (self.settings.width - self.text_rect.width - self.image.get_width() - 20, self.settings.height - 12.5)


    def blit_DeSo_price(self):
        pygame.draw.rect(self.screen, self.color, self.box_rect)
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text, self.text_rect)
        

    def update(self):
        self.blit_DeSo_price()
