import sys
import pygame

class Sounds:

    pygame.mixer.init()

    goathurt = pygame.mixer.Sound("sounds/goathurt.ogg")
    goatdead = pygame.mixer.Sound("sounds/goatdead.ogg")
    carhurt = pygame.mixer.Sound("sounds/carhurt.ogg")
    cardead = pygame.mixer.Sound("sounds/cardead.ogg")
    trainhurt = pygame.mixer.Sound("sounds/trainhurt.ogg")
    traindead = pygame.mixer.Sound("sounds/traindead.ogg")
    planehurt = pygame.mixer.Sound("sounds/planehurt.ogg")
    planedead = pygame.mixer.Sound("sounds/planedead.ogg")
    rockethurt = pygame.mixer.Sound("sounds/rockethurt.ogg")
    rocketdead = pygame.mixer.Sound("sounds/rocketdead.ogg")

    @staticmethod
    def goat_hurt_sound():
        goathurt = pygame.mixer.Sound("sounds/goathurt.ogg")
        pygame.mixer.Sound.play(goathurt)
        
    