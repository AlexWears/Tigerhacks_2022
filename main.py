import sys
import random
import pygame

from button import Button

from grass_and_flowers import Grass
from grass_and_flowers import Flower
from road import Road
from settings import Settings
from goat import Goat
from obstacle import Obstacle
from car_obst import CarObst
from pot_hole import PotHole
from tree import Tree
from car import Car
from puddle import Puddle
from rock import Rock
from coin import Coin
from enemy import Enemy
from BetterCryptoAPI import CryptoAPI
from deso_price import DeSoPrice
from shop import Shop
from plane import Plane
from train import Train
from rocket import Rocket
from sounds import Sounds
 
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
        self.enemies.append(Enemy(self, self.vehicle))
        self.coins = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()

        self.coinCount = 0 #initialize player coin count

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

    def make_enemies_and_obstacles(self):
        
        if self.settings.frame_count % self.settings.obstacle_spawn_rate == 0:
            i = random.randint(0, 18)

            if 0 <= (i % 18) <= 2:
                self.enemies.append(Enemy(self, self.vehicle))
            elif 3 <= (i % 18) < 5:
                self.obstacles.add(CarObst(self, "sprites/evilCar.bmp"))
            elif 6 <= (i % 18) < 8:
                self.obstacles.add(PotHole(self, "sprites/pothole.bmp"))
            elif 9 <= (i % 18) < 11:
                self.obstacles.add(Puddle(self, "sprites/puddle.bmp"))
            elif 12 <= (i % 18) < 14:
                self.obstacles.add(Rock(self, "sprites/rock.bmp"))
            elif 15 <= (i % 18) < 17:
                self.obstacles.add(Tree(self, "sprites/biggerTree.bmp"))

        if (len(self.enemies) > 0):
            for i in range(0, len(self.enemies)):
                try:
                    self.enemies[i].update()
                except IndexError:
                    pass
        for i in self.obstacles:
            i.update()

    def make_coins(self):

        if random.randint(0, 1000) % self.settings.coin_spawn_rate == 0:
            new_coin = Coin(self)
            self.coins.add(new_coin)

        for i in self.coins:
            i.update()
        

    def draw(self):

    # Make screen background, make the grass, make the road, make the vehicle
        self.screen.fill(self.settings.bg_color)
        self.make_grass_and_flowers()
        self.make_road()
        self.make_enemies_and_obstacles()
        self.make_coins()
        self.vehicle.update()
        self.deso.update()
        self.start_button.draw_button()

        pygame.display.flip()

    def collisions(self):

        if (len(self.enemies) > 0):
            for i in range(0, len(self.enemies)):
                if self.vehicle.rect.colliderect(self.enemies[i]):
                    self.settings.health -= 100
                    if self.settings.health > 0:
                        self.vehicle.play_hurt_sound()
                    else:
                        self.vehicle.play_dead_sound()
                    return

        if (len(self.obstacles) > 0):
            for i in self.obstacles.copy():
                if self.vehicle.rect.colliderect(i):
                    if self.settings.health > 0:
                        self.vehicle.play_hurt_sound()
                    else:
                        self.vehicle.play_dead_sound()
                    self.obstacles.remove(i)

        if (len(self.coins) > 0):
            for i in self.coins.copy():
                if self.vehicle.rect.colliderect(i):
                    self.settings.coin_count += 1
                    self.coins.remove(i)

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

    def clear_screen(self):

        self.grasses.empty()
        self.flowers.empty()
        self.enemies.clear()
        self.obstacles.empty()
        self.road.clear_road()

    @staticmethod
    def start_music():
        pygame.mixer.init()
        pygame.mixer.music.load('sounds/goat_theme.ogg')
        pygame.mixer.music.play(-1)

    def run_game(self):

        #Start menu
        self.draw()
        self.start_button.draw_button()
        while self.settings.game_start == False:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_start_button(mouse_pos)
                    self.start_button.move_button()

        self.start_music()

        while self.settings.game_start == True:

            self.get_input()
            self.draw()
            self.collisions()
            if self.settings.health <= 0:
                self.clear_screen()
                self.shop.load(self)
                if(self.settings.v_type == 0):
                    self.vehicle = Goat(self)
                elif(self.settings.v_type == 1):
                    self.vehicle = Goat(self)
                elif(self.settings.v_type == 2):
                    self.vehicle = Train(self)
                elif(self.settings.v_type == 3):
                    self.vehicle = Car(self)
                elif(self.settings.v_type == 4):
                    self.vehicle = Plane(self)
                elif(self.settings.v_type == 5):
                    self.vehicle = Rocket(self)
            self.clock.tick(self.settings.frame_rate)
            self.settings.frame_count += 1


if __name__ == "__main__":
    deso_price = CryptoAPI.get_DeSo_price()
    game = JimRs_Garage()
    game.run_game()