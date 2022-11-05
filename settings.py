import sys
import pygame

class Settings:

    def __init__(self):

    # Default settings

        self.default_bg_color = (86,125,70)

    # Settings that will NOT change over the course of the game
        
        self.bg_color = self.default_bg_color


    # Settings that will change over the course of the game

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.speed_vert = 10
        self.speed_hor = 15