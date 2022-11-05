import sys
import pygame

class Settings:

    def __init__(self):

    # Default settings to return to

        self.default_bg_color = (86,125,70)
        self.width = 1500
        self.height = 1000

    # Screen Settings
    
        self.bg_color = self.default_bg_color


    # Vehicle Settings

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.speed_vert = 10
        self.speed_hor = 15

    # Environment Settings

        self.env_speed = 3