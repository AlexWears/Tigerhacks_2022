import pygame

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, JimRs_Garage, image):

        super().__init__()

        self.settings = JimRs_Garage.settings
        self.screen = JimRs_Garage.screen
        self.speed = self.settings.env_speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.y = 0
        
    def blit_obstacle(self):

        self.screen.blit(self.image, self.rect)
    
    def update(self):

        self.rect.y += self.speed
        self.blit_obstacle()


