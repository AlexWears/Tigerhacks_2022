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
from score import Score
from healthbar import HealthBar
 
class Goat_Upgrader:

    def __init__(self):
    # Init method
        pygame.init()

    # Creates settings, screen, screen rect, and pygame time
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.height = self.screen.get_rect().height
        self.settings.width = self.screen.get_rect().width
        pygame.display.set_caption("Goat Upgrader")
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
        self.score = Score(self)
        self.health_bar = HealthBar(self)

        self.coinCount = 0 #initialize player coin count

        self.start_button = Button(self,"Start", 20, (0,0,0), 150, 75, (255,255,255), self.settings.width-150, self.settings.height-150) #init start button

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

        if self.settings.frame_count == 1800:
            self.settings.obstacle_spawn_rate -= 5
            self.settings.coin_spawn_rate -= 30
        elif self.settings.frame_count == 3600:
            self.settings.obstacle_spawn_rate -= 5
            self.settings.coin_spawn_rate -= 30
        elif self.settings.frame_count == 5400:
            self.settings.obstacle_spawn_rate -= 5
            self.settings.coin_spawn_rate -= 30
        elif self.settings.frame_count == 7200:
            self.settings.obstacle_spawn_rate -= 5
            self.settings.coin_spawn_rate -= 30
        elif self.settings.frame_count == 9000:
            self.settings.obstacle_spawn_rate -= 5
            self.settings.coin_spawn_rate -= 30
        
        if self.settings.frame_count % self.settings.obstacle_spawn_rate == 0 or self.settings.frame_count % self.settings.obstacle_spawn_rate == 1:
            i = random.randint(0, 18)

            if 0 <= (i % 18) <= 1:
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
        self.score.update()
        self.health_bar.update()

        pygame.display.flip()

    def draw_after_death(self):
        self.screen.fill(self.settings.bg_color)
        for i in self.enemies:
            i.blit_enemy()
        for i in self.obstacles:
            i.blit_obstacle()
        for i in self.grasses:
            i.blit_grass()
        for i in self.flowers:
            i.blit_flower()
        self.road.blit_road()
        for i in self.coins:
            i.blit()
        self.score.update()
        self.health_bar.update()

        pygame.display.flip()

    def collisions(self):
        if(self.vehicle.fuel <= 0 or self.vehicle.fly_choice == 0):
            if (len(self.enemies) > 0):
                for i in range(0, len(self.enemies)):
                    if self.vehicle.rect.colliderect(self.enemies[i]):
                        self.settings.health -= self.enemies[i].damage
                        if self.settings.health > 0:
                            self.enemies[i].damage = 0
                            self.vehicle.play_hurt_sound()
                        else:
                            self.vehicle.play_dead_sound()

            if (len(self.obstacles) > 0):
                for i in self.obstacles.copy():
                    if self.vehicle.rect.colliderect(i):
                        self.settings.health -= i.damage
                        if self.settings.health > 0:
                            self.vehicle.play_hurt_sound()
                        else:
                            self.vehicle.play_dead_sound()
                        self.obstacles.remove(i)

            if (len(self.coins) > 0):
                for i in self.coins.copy():
                    if self.vehicle.rect.colliderect(i):
                        self.settings.coin_count += 1
                        self.score.coin_score += 50
                        self.coins.remove(i)
                        pygame.mixer.Sound.play(pygame.mixer.Sound("sounds/coin.ogg"))
        else: return

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
                    elif key == pygame.K_SPACE:
                        self.vehicle.fly_choice = 1
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
        self.screen.fill((120,30,20))
        self.start_button.draw_button()
        self.start_image = pygame.image.load("sprites/titleScreen.bmp")
        self.start_image_rect = self.start_image.get_rect()
        self.start_image_rect.bottomleft = (0,0)
        self.start_image_rect.center = self.screen.get_rect().center
        self.screen.blit(self.start_image, self.start_image_rect)

        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.text_color = (0,0,0)

        self.start_txt = self.font.render("Press the button or [Enter] to start.", True, self.text_color)
        self.s_txt_rect = self.start_txt.get_rect()
        self.s_txt_rect.center = (self.settings.width/2, self.settings.height-75)

        self.instructions = self.font.render("Press [Esc] to exit.", True, self.text_color)
        self.inst_rect = self.instructions.get_rect()
        self.inst_rect.center = (self.settings.width/2, self.settings.height-30)

        self.screen.blit(self.start_txt, self.s_txt_rect)
        self.screen.blit(self.instructions, self.inst_rect)

        pygame.mixer.init()
        pygame.mixer.music.load('sounds/titleMusic.ogg')
        pygame.mixer.music.play(-1)

        pygame.display.update()

        while self.settings.game_start == False:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_start_button(mouse_pos)
                    self.start_button.move_button()
                elif event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_RETURN:
                        self.start_button.move_button()
                        self.settings.game_start = True
                    elif key == pygame.K_ESCAPE:
                        sys.exit()

        self.start_music()

        while self.settings.game_start == True:

            self.get_input()
            if(self.settings.v_type == 4): self.vehicle.fly(pygame.image.load("sprites/plane.bmp"),pygame.image.load("sprites/planeShadow.bmp"))
            if(self.settings.v_type == 5): self.vehicle.fly(pygame.image.load("sprites/rocket.bmp"),pygame.image.load("sprites/rocketShadow.bmp"))
            self.draw()
            self.collisions()
            if self.settings.health <= 0:
               
                self.vehicle.image = pygame.image.load("sprites/bomb1.bmp")
                x = self.vehicle.rect.midbottom
                self.vehicle.rect = self.vehicle.image.get_rect()
                self.vehicle.rect.midbottom = x
                self.draw_after_death()
                self.screen.blit(self.vehicle.image, self.vehicle.rect)
                pygame.display.update()
    
                pygame.time.wait(1000)
                
                self.vehicle.image = pygame.image.load("sprites/bomb2.bmp")
                x = self.vehicle.rect.midbottom
                self.vehicle.rect = self.vehicle.image.get_rect()
                self.vehicle.rect.midbottom = x
                self.draw_after_death()
                self.screen.blit(self.vehicle.image, self.vehicle.rect)
                pygame.display.update()

                pygame.time.wait(1000)

                self.vehicle.image = pygame.image.load("sprites/bomb3.bmp")
                x = self.vehicle.rect.midbottom
                self.vehicle.rect = self.vehicle.image.get_rect()
                self.vehicle.rect.midbottom = x
                self.draw_after_death()
                self.screen.blit(self.vehicle.image, self.vehicle.rect)
                pygame.display.update()

                pygame.time.wait(1000)

                self.clear_screen()
                self.score.check_high_score()
                self.shop.load(self)
                if(self.settings.v_type == 0):
                    self.vehicle = Goat(self)
                    self.settings.v_type == 0
                elif(self.settings.v_type == 1):
                    self.vehicle = Goat(self)
                    self.settings.v_type == 1
                elif(self.settings.v_type == 2):
                    self.vehicle = Train(self)
                    self.settings.v_type == 2
                elif(self.settings.v_type == 3):
                    self.vehicle = Car(self)
                    self.settings.v_type == 3
                elif(self.settings.v_type == 4):
                    self.vehicle = Plane(self)
                    self.settings.v_type == 4
                elif(self.settings.v_type == 5):
                    self.vehicle = Rocket(self)
                    self.settings.v_type == 5
            self.clock.tick(self.settings.frame_rate)
            self.settings.frame_count += 1


if __name__ == "__main__":
    deso_price = CryptoAPI.get_DeSo_price()
    game = Goat_Upgrader()
    game.run_game()
