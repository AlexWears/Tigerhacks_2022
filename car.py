import sys
import pygame

from vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, Goat_Upgrader):

        super().__init__(Goat_Upgrader)

        self.image = pygame.image.load("sprites/car.bmp")
        self.rect = self.image.get_rect()

        self.settings.speed_vert = self.settings.car_speed_vert
        self.settings.speed_hor = self.settings.car_speed_hor

    def blit_car(self):

        self.screen.blit(self.image, self.rect)

    def play_hurt_sound(self):

        self.hurt_sound = pygame.mixer.Sound("sounds/carhurt.ogg")
        pygame.mixer.Sound.play(self.hurt_sound)

    def play_dead_sound(self):

        self.dead_sound = pygame.mixer.Sound("sounds/cardead.ogg")
        pygame.mixer.Sound.play(self.dead_sound)