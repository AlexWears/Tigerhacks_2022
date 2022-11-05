import sys
import pygame

from settings import Settings

from goat import Goat

class JimRs_Garage:

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((1500,1000))
        pygame.display.set_caption("JimR's Garage")

        self.vehicle = Goat(self)

    def draw(self):

        self.screen.fill(self.settings.bg_color)
        self.vehicle.blit_vehicle()
        pygame.display.flip()

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.draw()


if __name__ == "__main__":
    game = JimRs_Garage()
    game.run_game()
