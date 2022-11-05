import sys
import pygame

from grass_and_flowers import Grass
from grass_and_flowers import Flower
from settings import Settings
from goat import Goat
from BetterCryptoAPI import CryptoAPI

class JimRs_Garage:

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width,self.settings.height))
        pygame.display.set_caption("JimR's Garage")
        self.clock = pygame.time.Clock()

        self.vehicle = Goat(self)
        self.grasses = pygame.sprite.Group()
        self.flowers = pygame.sprite.Group()

        self.coins = 0 #initialize player coin count

    def make_grass_and_flowers(self):

        if self.settings.frame_count % 2 == 0:
            new_grass = Grass(self)
            self.grasses.add(new_grass)

        for grass in self.grasses.copy():
            if grass.rect.top > self.settings.height:
                self.grasses.remove(grass)

        if self.settings.frame_count % 5 == 0:
            new_flower = Flower(self)
            self.flowers.add(new_flower)

        for flower in self.flowers.copy():
            if flower.rect.top > self.settings.height:
                self.flowers.remove(flower)

        self.grasses.update()
        self.flowers.update()
        

    def draw(self):
        self.screen.fill(self.settings.bg_color)
        self.make_grass_and_flowers()
        self.vehicle.update()
        pygame.display.flip()

    def get_input(self):
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_UP:
                        self.settings.moving_up = True
                    elif key == pygame.K_DOWN:
                        self.settings.moving_down = True
                    elif key == pygame.K_LEFT:
                        self.settings.moving_left = True
                    elif key == pygame.K_RIGHT:
                        self.settings.moving_right = True
                    elif key == pygame.K_ESCAPE:
                        sys.exit()

                elif event.type == pygame.KEYUP:
                    key = event.key
                    if key == pygame.K_UP:
                        self.settings.moving_up = False
                    elif key == pygame.K_DOWN:
                        self.settings.moving_down = False
                    elif key == pygame.K_LEFT:
                        self.settings.moving_left = False
                    elif key == pygame.K_RIGHT:
                        self.settings.moving_right = False

    def run_game(self):

        while True:
            
            self.get_input()
            self.draw()
            self.clock.tick(self.settings.frame_rate)
            self.settings.frame_count += 1


if __name__ == "__main__":
    deso_price = CryptoAPI.get_DeSo_price()
    game = JimRs_Garage()
    game.run_game()