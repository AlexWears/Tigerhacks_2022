import sys
import pygame

from settings import Settings
from goat import Goat
from BetterCryptoAPI import CryptoAPI

class JimRs_Garage:

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((1500,1000))
        pygame.display.set_caption("JimR's Garage")

        self.vehicle = Goat(self)

    def draw(self):

        self.screen.fill(self.settings.bg_color)
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


if __name__ == "__main__":
    deso_price = CryptoAPI.get_DeSo_price()
    game = JimRs_Garage()
    game.run_game()