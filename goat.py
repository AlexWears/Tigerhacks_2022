import sys
import pygame

from vehicle import Vehicle

class Goat(Vehicle):

    def __init__(self, JimRs_Garage):
        
        super().__init__(JimRs_Garage)
        if self.settings.v_type == 1:
            self.image = pygame.image.load("sprites/fancyGoat.bmp")
        elif self.settings.v_type == 0:
            self.image = pygame.image.load("sprites/goat.bmp")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.settings.width/2,self.settings.height/2)

        self.settings.speed_vert = self.settings.goat_speed_vert
        self.settings.speed_hor = self.settings.goat_speed_hor

    def blit_goat(self):
        
        self.screen.blit(self.image, self.rect)

    def play_hurt_sound(self):

        self.hurt_sound = pygame.mixer.Sound("sounds/goathurt.ogg")
        pygame.mixer.Sound.play(self.hurt_sound)

    def play_dead_sound(self):

        self.dead_sound = pygame.mixer.Sound("sounds/goatdead.ogg")
        pygame.mixer.Sound.play(self.dead_sound)