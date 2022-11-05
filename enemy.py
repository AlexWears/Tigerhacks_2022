import sys
import pygame
import math
import random

class Enemy:

    def __init__(self, JimRs_Garage, vehicle):

        self.settings = JimRs_Garage.settings
        self.enemy_list = JimRs_Garage.enemies
        self.screen = JimRs_Garage.screen
        self.vehicle = vehicle

        self.image = pygame.image.load("sprites/evilGoat.bmp")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0,0)
        # self.x = random.randint(0, self.settings.width - self.rect.width)
        # self.y = 0
        self.rect.x = random.randint(0, self.settings.width - self.rect.width)
        self.rect.y = 0

        self.angle = 0
        self.speed = self.settings.enemy_goat_speed


    def blit_enemy(self):
        self.calculate_angle()

        
        if self.rect.x - self.vehicle.rect.x < -self.speed:
            self.rect.x += self.speed
        elif self.rect.x - self.vehicle.rect.x > self.speed:
            self.rect.x -= self.speed
        else:
            self.rect.x -=  self.rect.x - self.vehicle.rect.x

        if not (self.rect.bottom < self.vehicle.rect.bottom):
            if self.angle < 0:
                self.angle -= 180
            elif self.angle > 0:
                self.angle += 180
        elif self.rect.x == self.vehicle.rect.x:
            self.rect.y += self.speed
    
        self.image_rotated = pygame.transform.rotate(self.image, self.angle)
        self.screen.blit(self.image_rotated, self.rect)

    def update(self):

        if (len(self.enemy_list) == 0):
            return

        self.rect.y += self.settings.env_speed
        self.blit_enemy()
        
        if self.rect.top > self.settings.height:
            self.enemy_list.remove(self)
            
            
    def calculate_angle(self):
        try:
            self.angle = math.degrees(math.atan(float(self.vehicle.rect.left - self.rect.left) / float(self.vehicle.rect.bottom - self.rect.bottom)))
        except ZeroDivisionError:
            self.angle = self.angle