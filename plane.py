import sys
import pygame

from vehicle import Vehicle

class Plane(Vehicle):
    
    def __init__(self, Goat_Upgrader):

        super().__init__(Goat_Upgrader)

        self.image = pygame.image.load("sprites/plane.bmp")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.settings.width/2,self.settings.height/2)

        self.settings.speed_vert = self.settings.plane_speed_vert
        self.settings.speed_hor = self.settings.plane_speed_hor

    def blit_plane(self):

        self.screen.blit(self.image, self.rect)

    def play_hurt_sound(self):

        self.hurt_sound = pygame.mixer.Sound("sounds/planehurt.ogg")
        pygame.mixer.Sound.play(self.hurt_sound)

    def play_dead_sound(self):

        self.dead_sound = pygame.mixer.Sound("sounds/planedead.ogg")
        pygame.mixer.Sound.play(self.dead_sound)