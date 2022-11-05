import sys
import pygame

class JimRs_Garage:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1500,1000))
        pygame.display.set_caption("JimR's Garage")

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
        pygame.display.flip()

if __name__ == "__main__":
    game = JimRs_Garage()
    game.run_game()
