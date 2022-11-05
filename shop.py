import sys
import pygame
from BetterCryptoAPI import CryptoAPI
from settings import Settings

class Shop:

    def __init__(self, JimRs_Garage):
        self.settings = JimRs_Garage.settings
        self.screen = JimRs_Garage.screen
        self.screen_rect = JimRs_Garage.screen
        self.coins = JimRs_Garage.coins

        self.train_img = pygame.image.load("sprites/train.bmp")
        self.car_img = pygame.image.load("sprites/car.bmp")
        self.plane_img = pygame.image.load("sprites/plane.bmp")
        self.rocket_img = pygame.image.load("sprites/rocket.bmp")

        self.


    def load(self):
        self.settings.deso_conv = CryptoAPI.get_DeSo_price()
        #self.USD = self.settings.deso_conv * self.coins

        while self.settings.health == 0:
            self.screen.fill(self.settings.shop_color)
            
            
        
        






    

