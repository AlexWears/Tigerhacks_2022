import sys
import pygame

class Settings:

    def __init__(self):

    # Default settings to return to
    
    # The resolution that we're using:
    # Width: 1500
    # Height: 1000
 
        self.default_bg_color = (86,125,70)
        self.default_obstacle_spawn_rate = 30
        self.default_coin_spawn_rate = 250
        self.default_env_speed = 5
        self.width = 1500 
        self.height = 1000

        self.goat_speed_vert = 8
        self.goat_speed_hor = 6

        self.train_speed_vert = 6
        self.train_speed_hor = 4

        self.car_speed_vert = 10
        self.car_speed_hor = 8

        self.plane_speed_vert = 10
        self.plane_speed_hor = 8

        self.rocket_speed_vert = 12
        self.rocket_speed_hor = 10

        self.game_start = False

    # Screen Settings
    
        self.bg_color = self.default_bg_color
        self.frame_rate = 60


    # Vehicle Settings

        self.v_type = 1

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.speed_vert = 10
        self.speed_hor = 15

        self.health = 150

        self.coin_count = 0
        self.high_score = 0

    # Environment Settings

        self.env_speed = self.default_env_speed
        self.time_between_grass = 2
        self.frame_count = 0
        self.road_width = 0
        self.road_left = 0
        
        self.enemy_goat_speed = 4
        self.obstacle_spawn_rate = self.default_obstacle_spawn_rate
        self.coin_spawn_rate = self.default_coin_spawn_rate

    # Shop Settings

        self.deso_conv = 0
        self.shop_color = (174, 176, 181)

        self.train_cost = 50
        self.car_cost = 75
        self.plane_cost = 0
        self.rocket_cost = 125
