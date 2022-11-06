import pygame

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, Goat_Upgrader, image):

        super().__init__()

        self.settings = Goat_Upgrader.settings
        self.screen = Goat_Upgrader.screen
        self.speed = self.settings.env_speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.damage = 40
        
    def blit_obstacle(self):

        self.screen.blit(self.image, self.rect)
    
    def update(self):

        self.rect.y += self.speed
        self.blit_obstacle()


