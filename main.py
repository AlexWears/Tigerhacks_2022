import sys
import pygame

sys.path.insert(0, "./interactable")

from button import Button

from grass_and_flowers import Grass
from grass_and_flowers import Flower
from road import Road
from settings import Settings
from goat import Goat
from obstacle import Obstacle
from car_obst import CarObst
from car import Car
from interactable.enemy import Enemy
from BetterCryptoAPI import CryptoAPI
from deso_price import DeSoPrice
from shop import Shop

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
        self.deso = DeSoPrice(self)
        self.road = Road(self)
        self.enemies = []
        # self.enemies.append(Enemy(self, self.vehicle))
        self.coins = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.car_obst = CarObst(self, "sprites/evilCar.bmp")
        self.obstacles.add(self.car_obst)

        self.coins = 0 #initialize player coin count

        self.start_button = Button(self,"Start", 20, (0,0,0), 150, 75, (255,255,255), self.settings.width/2, self.settings.height/2) #init start button

        #init shop
        self.shop = Shop(self)

    def make_grass_and_flowers(self):

    # Create a new grass every other frame
        if self.settings.frame_count % 4 == 0:
            new_grass = Grass(self)
            self.grasses.add(new_grass)

    # Delete grass that's off of the screen
        for grass in self.grasses.copy():
            if grass.rect.top > self.settings.height:
                self.grasses.remove(grass)

    # Create a new flower every five frames
        if self.settings.frame_count % 8 == 0:
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
        for i in range(0, len(self.enemies)):
            self.enemies[i].update()
        for i in self.obstacles:
            i.update()
        self.vehicle.update()
        self.deso.update()
        self.start_button.draw_button()

        pygame.display.flip()

    def collisions(self):

        if (len(self.enemies) > 0):
            for i in range(0, len(self.enemies)):
                if self.vehicle.rect.colliderect(self.enemies[i]):
                    sys.exit()


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

    def _check_start_button(self, mouse_pos):
        if(self.start_button.rect.collidepoint(mouse_pos)):
            self.settings.game_start = True

    def run_game(self):

        #pygame.mixer.music.load('sounds/goat_theme.ogg')
        #pygame.mixer.music.play(-1)

        #Start menu
        self.draw()
        self.start_button.draw_button()
        while self.settings.game_start == False:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_start_button(mouse_pos)
                    self.start_button.move_button()

        while self.settings.game_start == True:
            self.get_input()
            self.draw()
            self.collisions()
            if self.settings.health <= 0:
                self.shop.load()
            self.clock.tick(self.settings.frame_rate)
            self.settings.frame_count += 1


if __name__ == "__main__":
    deso_price = CryptoAPI.get_DeSo_price()
    game = JimRs_Garage()
    game.run_game()