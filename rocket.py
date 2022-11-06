import sys
import pygame

from vehicle import Vehicle

class Rocket(Vehicle):

    def __init__(self, Goat_Upgrader):

        super().__init__(Goat_Upgrader)

        self.image = pygame.image.load("sprites/rocket.bmp")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.settings.width/2,self.settings.height/2)

        self.settings.speed_vert = self.settings.rocket_speed_vert
        self.settings.speed_hor = self.settings.rocket_speed_hor
        self.fuel = 500
        self.max_fuel = 500

    def blit_train(self):

        self.screen.blit(self.image, self.rect)

    def play_hurt_sound(self):

        self.hurt_sound = pygame.mixer.Sound("sounds/rockethurt.ogg")
        pygame.mixer.Sound.play(self.hurt_sound)

    def play_dead_sound(self):

        self.dead_sound = pygame.mixer.Sound("sounds/rocketdead.ogg")
        pygame.mixer.Sound.play(self.dead_sound)