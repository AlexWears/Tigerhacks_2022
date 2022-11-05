import sys
import pygame
font = pygame.font.SysFont("Arial", 20)

class Button:

    def __init__(self, JimRs_Garage, text, x_coord, y_coord):
        self.settings = JimRs_Garage.settings
        self.screen = JimRs_Garage.screen
        self.screen_rect = JimRs_Garage.screen.get_rect()

        self.x_coord = x_coord
        self.y_coord = y_coord

        self.font = pygame.font.SysFont("Arial", font)

    def text(self, text, color):
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(color)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x_coord, self.y_coord, self.size[0], self.size[1])
    
    def render(self):
        self.screen.blit(self.surface, (self.x_coord, self.y_coord))

    def click(self, mouse_click):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_click.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.getpressed()[0]:
                if self.rect.collidepoint(mouse_x, mouse_y):
                    self.text("","red")


