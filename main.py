import sys
import pygame
from button import Button

from grass_and_flowers import Grass
from grass_and_flowers import Flower
from road import Road
from settings import Settings
from goat import Goat
from BetterCryptoAPI import CryptoAPI

class JimRs_Garage:

    def __init__(self):
    # Init method
        pygame.init()

    # Creates settings, screen, screen rect, and pygame time
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.height = self.screen.get_rect().height
        self.settings.width = self.screen.get_rect().width
        pygame.display.set_caption("JimR's Garage")
        self.clock = pygame.time.Clock()

    # Creates the sprites that we'll need
        self.vehicle = Goat(self)
        self.grasses = pygame.sprite.Group()
        self.flowers = pygame.sprite.Group()
        self.road = Road(self)

        self.coins = 0 #initialize player coin count
        self.start_button = Button(self,"Start",30,500,500) #init start button

    def make_grass_and_flowers(self):

    # Create a new grass every other frame
        if self.settings.frame_count % 2 == 0:
            new_grass = Grass(self)
            self.grasses.add(new_grass)

    # Delete grass that's off of the screen
        for grass in self.grasses.copy():
            if grass.rect.top > self.settings.height:
                self.grasses.remove(grass)

    # Create a new flower every five frames
        if self.settings.frame_count % 5 == 0:
            new_flower = Flower(self)
            self.flowers.add(new_flower)

    # Delete flowers that are off the screen
        for flower in self.flowers.copy():
            if flower.rect.top > self.settings.height:
                self.flowers.remove(flower)

    # Update grass and flower positions
        self.grasses.update()
        self.flowers.update()

    # Make the road in the middle

    def make_road(self):
        self.road.update()
        

    def draw(self):

    # Make screen background, make the grass, make the road, make the vehicle
        self.screen.fill(self.settings.bg_color)
        self.make_grass_and_flowers()
        self.make_road()
        self.vehicle.update()
        pygame.display.flip()

    def get_input(self):
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_UP or key == pygame.K_w:
                        self.settings.moving_up = True
                    elif key == pygame.K_DOWN or key == pygame.K_s:
                        self.settings.moving_down = True
                    elif key == pygame.K_LEFT or key == pygame.K_a:
                        self.settings.moving_left = True
                    elif key == pygame.K_RIGHT or key == pygame.K_d:
                        self.settings.moving_right = True
                    elif key == pygame.K_ESCAPE:
                        sys.exit()

                elif event.type == pygame.KEYUP:
                    key = event.key
                    if key == pygame.K_UP or key == pygame.K_w:
                        self.settings.moving_up = False
                    elif key == pygame.K_DOWN or key == pygame.K_s:
                        self.settings.moving_down = False
                    elif key == pygame.K_LEFT or key == pygame.K_a:
                        self.settings.moving_left = False
                    elif key == pygame.K_RIGHT or key == pygame.K_d:
                        self.settings.moving_right = False

    def run_game(self):

        pygame.mixer.music.load('sounds/goat_theme.ogg')
        pygame.mixer.music.play(-1)

        #Start menu
        self.draw()
        while self.start_button.click(pygame.event.poll()) == False:
            self.start_button.render()

        while True:
            self.get_input()
            self.draw()
            self.clock.tick(self.settings.frame_rate)
            self.settings.frame_count += 1


if __name__ == "__main__":
    deso_price = CryptoAPI.get_DeSo_price()
    game = JimRs_Garage()
    game.run_game()