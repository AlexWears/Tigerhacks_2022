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

    def load(self):
        self.screen.fill(self.settings.shop_color)
        self.settings.deso_conv = CryptoAPI.get_DeSo_price()

    

