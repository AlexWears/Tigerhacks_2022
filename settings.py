import sys
import pygame

class Settings:

    def __init__(self):

    # Default settings to return to
    
    # The resolution that we're using:
    # Width: 1500
    # Height: 1000

        self.default_bg_color = (86,125,70)
        self.width = 1500
        self.height = 1000

        self.goat_speed_vert = 5
        self.goat_speed_hor = 3

        self.train_speed_vert = 3
        self.train_speed_hor = 3

        self.car_speed_vert = 3
        self.car_speed_hor = 3

        self.plane_speed_vert = 3
        self.plane_speed_hor = 3

    # Screen Settings
    
        self.bg_color = self.default_bg_color
        self.frame_rate = 60


    # Vehicle Settings

        # self.v_type = 1

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.speed_vert = 10
        self.speed_hor = 15

    # Environment Settings

        self.env_speed = 5
        self.time_between_grass = 2
        self.frame_count = 0
        self.road_width = 0