import sys
import pygame
from settings import Settings

class JimRs_Garage:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1500,1000))

        pygame.display.set_caption("JimR's Garage")

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()

if __name__ == "__main__":
    game = JimRs_Garage()
    game.run_game()
