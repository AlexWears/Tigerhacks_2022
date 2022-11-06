import sys
import pygame
from settings import Settings

class Vehicle(pygame.sprite.Sprite):

    pygame.mixer.init()

    def __init__(self, Goat_Upgrader):
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.settings = Goat_Upgrader.settings
        self.screen = Goat_Upgrader.screen
        self.screen_rect = Goat_Upgrader.screen.get_rect()
        self.image = pygame.image.load("sprites/thing.bmp")
        self.health = self.settings.health
        self.scale_i = 1
        self.fly_i = 0
        self.fuel = 0
        self.fly_choice = False

        self.fb_text = self.font.render("Press [Space] to fly", True, (255,255,255))
        self.fbt_rect = self.fb_text.get_rect()
        self.fbt_rect.bottomleft = (55, self.settings.height-55)
        
        self.rect = self.image.get_rect()

        self.rect.bottomleft = (self.settings.width/2,self.settings.height/2)

    def blit_vehicle(self):
        self.screen.blit(self.image, self.rect)

    def update(self):

        if self.settings.moving_right and self.rect.right < self.settings.width:
            self.rect.x += self.settings.speed_hor
        if self.settings.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.speed_hor
        if self.settings.moving_down and self.rect.bottom < self.settings.height:
            self.rect.y += self.settings.speed_vert
        if self.settings.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.speed_vert

        if self.rect.bottom < self.settings.height:
            self.rect.y += self.settings.env_speed
    
        self.blit_vehicle()

    def play_hurt_sound(self):

        self.hurt_sound = pygame.mixer.Sound("sounds/goathurt.ogg")
        pygame.mixer.Sound.play(self.hurt_sound)

    def play_dead_sound(self):

        self.dead_sound = pygame.mixer.Sound("sounds/goatdead.ogg")
        pygame.mixer.Sound.play(self.dead_sound)

    def fly(self, image, shadow):
        if(self.settings.v_type != 4 and self.settings.v_type != 5):
            return
        if(self.fuel > 0 and self.fly_choice):
            if self.scale_i < 20 and self.fly_i == 0:
                self.image = pygame.transform.scale(self.image, (116*self.scale_i,116*self.scale_i))
                self.scale_i += 1
                return
            if(self.fly_i == 0): 
                self.image = shadow
                self.fly_i = 1
            self.fuel -= 1
            self.update_fuel()
        if(self.fuel <= 0):
            self.image = image
            if self.scale_i > 1 and self.fly_i:
                self.image = pygame.transform.scale(self.image, (116*self.scale_i,116*self.scale_i))
                self.scale_i -= 1
                return
            self.image = image
            self.fly_i = 0
            self.scale_i = 1
            self.fly_choice = False
        return

    def fuel_gauge(self, Goat_Upgrader):
        
        self.settings = Goat_Upgrader.settings
        self.screen = Goat_Upgrader.screen

        self.initialize_fuel()


    def initialize_fuel(self):
        
        #initial fuel bar
        self.height1 = 50
        self.width1 = (self.fuel * 2)
        self.FB_rect = pygame.Rect(50, self.settings.height - 50, self.width1, self.height1)
        self.FBcolor = (230, 210, 115)
        self.FB_rect.bottomleft = (50, self.settings.height - 50)

        #back of health bar (black bar)
        self.height2 = 60
        self.width2 = 1010
        self.BG_rect = pygame.Rect(45, self.settings.height - 45, self.width2, self.height2)
        self.BGcolor = (0, 0, 0)
        self.BG_rect.bottomleft = (45, self.settings.height - 45)

        #Fuel Bar Text
        

    def update_fuel(self):
        self.initialize_fuel()
        pygame.draw.rect(self.screen, self.BGcolor, self.BG_rect)
        pygame.draw.rect(self.screen, self.FBcolor, self.FB_rect)
        self.screen.blit(self.fb_text, self.fbt_rect)
            

