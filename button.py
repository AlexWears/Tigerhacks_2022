import sys
import pygame

class Button:

    def __init__(self, JimRs_Garage, text, t_size, t_color, b_width, b_height, b_color, x, y):

        self.settings = JimRs_Garage.settings
        self.screen = JimRs_Garage.screen
        self.screen_rect = JimRs_Garage.screen.get_rect()

        self.width, self.height = b_width, b_height
        self.button_color = b_color
        self.text_color = t_color
        self.font = pygame.font.SysFont("Comic Sans MS", t_size)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)

        self._prep_msg(text)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def move_button(self):
        self.rect.center = (-100, -100)
        self.msg_image_rect.center = (-100, -100)
        self.draw_button()


