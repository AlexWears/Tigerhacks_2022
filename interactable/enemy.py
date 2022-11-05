import sys
import pygame

class Enemy:

    def __init__(self, JimRs_Garage):

        self.settings = JimRs_Garage.settings
        self.screen = JimRs_Garage.screen

        self.image = 