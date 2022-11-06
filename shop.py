import sys
import pygame
from BetterCryptoAPI import CryptoAPI
from settings import Settings
from button import Button
from deso_price import DeSoPrice

class Shop:

    def __init__(self, Goat_Upgrader):
        self.text_color = (0,0,0)
        self.button_color = (255,255,255)
        self.font = pygame.font.SysFont("Comic Sans MS", 30)

        self.settings = Goat_Upgrader.settings
        self.screen = Goat_Upgrader.screen
        self.screen_rect = Goat_Upgrader.screen
        self.usd = self.settings.coin_count * self.settings.deso_conv

        self.deso = DeSoPrice(self)

    def _create_stuff(self):

        #Set train picture, name, price and buy button
        self.train_img = pygame.image.load("sprites/train.bmp")
        self.train_rect = self.train_img.get_rect()
        self.train_rect.center = (200, 140)
        self.train_text = self.font.render("Steam-Powered Goat", True, self.text_color)
        self.train_text_rect = self.train_text.get_rect()
        self.train_text_rect.center = (500, 140)
        self.train_price = self.font.render(str(self.settings.train_cost), True, self.text_color)
        self.train_price_rect = self.train_price.get_rect()
        self.train_price_rect.center = (800, 140)
        self.train_button = Button(self, "Buy", 30, self.text_color, 100, 50, self.button_color, 1000, 140)
        
        #Set car picture, name, price, and buy button
        self.car_img = pygame.image.load("sprites/car.bmp")
        self.car_rect = self.car_img.get_rect()
        self.car_rect.center = (200, 340)
        self.car_text = self.font.render("Goat with a V8", True, self.text_color)
        self.car_text_rect = self.car_text.get_rect()
        self.car_text_rect.center = (500, 340)
        self.car_price = self.font.render(str(self.settings.car_cost), True, self.text_color)
        self.car_price_rect = self.car_price.get_rect()
        self.car_price_rect.center = (800, 340)
        self.car_button = Button(self, "Buy", 30, self.text_color, 100, 50, self.button_color, 1000, 340)

        #Set plane picture, name, price, and buy button
        self.plane_img = pygame.image.load("sprites/plane.bmp")
        self.plane_rect = self.plane_img.get_rect()
        self.plane_rect.center = (200, 490)
        self.plane_text = self.font.render("Goat with Wings", True, self.text_color)
        self.plane_text_rect = self.plane_text.get_rect()
        self.plane_text_rect.center = (500, 490)
        self.plane_price = self.font.render(str(self.settings.plane_cost), True, self.text_color)
        self.plane_price_rect = self.plane_price.get_rect()
        self.plane_price_rect.center = (800, 490)
        self.plane_button = Button(self, "Buy", 30, self.text_color, 100, 50, self.button_color, 1000, 490)

        #Set rocket picture, name, price, and buy button
        self.rocket_img = pygame.image.load("sprites/rocket.bmp")
        self.rocket_rect = self.rocket_img.get_rect()
        self.rocket_rect.center = (200, 690)
        self.rocket_text = self.font.render("Explosive Goat", True, self.text_color)
        self.rocket_text_rect = self.rocket_text.get_rect()
        self.rocket_text_rect.center = (500, 690)
        self.rocket_price = self.font.render(str(self.settings.rocket_cost), True, self.text_color)
        self.rocket_price_rect = self.rocket_price.get_rect()
        self.rocket_price_rect.center = (800, 690)
        self.rocket_button = Button(self, "Buy", 30, self.text_color, 100, 50, self.button_color, 1000, 690)

        #Set death recap text
        self.death_recap = self.font.render("Click here for a death recap.", True, self.text_color)
        self.dr_rect = self.death_recap.get_rect()
        self.dr_rect.center = (self.settings.width/2, self.settings.height-25)

        #Set Shop TItle 
        self.shop_title = self.font.render("Upgrade Your Goat", True, self.text_color)
        self.st_rect = self.shop_title.get_rect()
        self.st_rect.center = (self.settings.width/2, 25)

        #Set Goat Instructions
        self.goat_inst = self.font.render("Press [Esc] to use the goat again", True, self.text_color)
        self.gi_rect = self.goat_inst.get_rect()
        self.gi_rect.center = (self.settings.width/2, self.settings.height-95)

        #Set no funds message
        self.no_funds = self.font.render("If you try to buy something you can't afford, you will get the goat", True, self.text_color)
        self.nf_rect = self.no_funds.get_rect()
        self.nf_rect.center = (self.settings.width/2, self.settings.height-60)

        #Set coin count text in upper right corner
        self.coin_text = self.font.render(str(self.settings.coin_count)+" DeSo", True, self.text_color)
        self.coin_text_rect = self.coin_text.get_rect()
        self.coin_text_rect.topright = (self.settings.width - 15, 10)

        #Set conversion to USD in upper right corner
        self.usd_text = self.font.render("$"+str(self.settings.coin_count * self.settings.deso_conv), True, self.text_color)
        self.usd_text_rect = self.usd_text.get_rect()
        self.usd_text_rect.topright = (self.settings.width - 15, 50)

    #Check if train buy button was pressed
    def _check_train_button(self, mouse_pos):
        if(self.train_button.rect.collidepoint(mouse_pos)):
            if(self.usd >= self.settings.train_cost):
                self.settings.v_type = 2
                self.usd -= self.settings.train_cost
                self.settings.coin_count -= self.settings.train_cost / self.settings.deso_conv
            else:
                self.settings.v_type = 1
            self.settings.health = 150
            self._reset_stuff()

    #Check if car buy button was pressed
    def _check_car_button(self, mouse_pos):
        if(self.car_button.rect.collidepoint(mouse_pos)):
            if(self.usd >= self.settings.car_cost):
                self.settings.v_type = 3
                self.usd -= self.settings.car_cost
                self.settings.coin_count -= self.settings.car_cost / self.settings.deso_conv
            else:
                self.settings.v_type = 1
            self.settings.health = 150
            self._reset_stuff()

    #Check if plane buy button was pressed
    def _check_plane_button(self, mouse_pos):
        if(self.plane_button.rect.collidepoint(mouse_pos)):
            if(self.usd >= self.settings.plane_cost):
                self.settings.v_type = 4
                self.usd -= self.settings.plane_cost
                self.settings.coin_count -= self.settings.plane_cost / self.settings.deso_conv
            else:
                self.settings.v_type = 1
            self.settings.health = 150
            self._reset_stuff()

    #Check if rocket buy button was pressed
    def _check_rocket_button(self, mouse_pos):
        if(self.rocket_button.rect.collidepoint(mouse_pos)):
            if(self.usd >= self.settings.plane_cost):
                self.settings.v_type = 5
                self.usd -= self.settings.plane_cost
                self.settings.coin_count -= self.settings.plane_cost / self.settings.deso_conv
            else:
                self.settings.v_type = 1
            self.settings.health = 150
            self._reset_stuff()

    def _reset_stuff(self):
        self.settings.moving_up = False
        self.settings.moving_down = False
        self.settings.moving_left = False
        self.settings.moving_right = False
        self.settings.obstacle_spawn_rate = self.settings.default_obstacle_spawn_rate
        self.settings.coin_spawn_rate = self.settings.default_coin_spawn_rate
        self.settings.env_speed = 5

    def load(self, Goat_Upgrader):

        pygame.mixer.init()
        pygame.mixer.music.load("sounds/shop_music.ogg")
        pygame.mixer.music.play(-1)
        self._create_stuff()
        self.deso.initialize()
        self.usd = self.settings.coin_count * self.settings.deso_conv
        while self.settings.health <= 0:

            self.screen.fill(self.settings.shop_color)

            self.screen.blit(self.train_img, self.train_rect)
            self.screen.blit(self.car_img, self.car_rect)
            self.screen.blit(self.plane_img, self.plane_rect)
            self.screen.blit(self.rocket_img, self.rocket_rect)

            self.screen.blit(self.train_text, self.train_text_rect)
            self.screen.blit(self.car_text, self.car_text_rect)
            self.screen.blit(self.plane_text, self.plane_text_rect)
            self.screen.blit(self.rocket_text, self.rocket_text_rect)

            self.screen.blit(self.train_price, self.train_price_rect)
            self.screen.blit(self.car_price, self.car_price_rect)
            self.screen.blit(self.plane_price, self.plane_price_rect)
            self.screen.blit(self.rocket_price, self.rocket_price_rect)

            self.train_button.draw_button()
            self.car_button.draw_button()
            self.plane_button.draw_button()
            self.rocket_button.draw_button()

            self.screen.blit(self.coin_text, self.coin_text_rect)
            self.screen.blit(self.usd_text, self.usd_text_rect)
            self.screen.blit(self.death_recap, self.dr_rect)
            self.screen.blit(self.shop_title, self.st_rect)
            self.screen.blit(self.goat_inst, self.gi_rect)
            self.screen.blit(self.no_funds, self.nf_rect)

            self.deso.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_train_button(mouse_pos)
                    self._check_car_button(mouse_pos)
                    self._check_plane_button(mouse_pos)
                    self._check_rocket_button(mouse_pos)
                    Goat_Upgrader.start_music()
                    return
                
                elif event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_j:
                        self.settings.v_type = 0
                        self.settings.health = 150
                        self._reset_stuff()
                        Goat_Upgrader.start_music()
                        return
                    elif key == pygame.K_c:
                        print(str(self.coins))

                    elif key == pygame.K_ESCAPE:
                        self.settings.v_type = 1
                        self.settings.health = 150
                        self._reset_stuff()
                        Goat_Upgrader.start_music()
                        return 

            pygame.display.flip()
