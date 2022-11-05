import sys
import pygame

class Road:

    def __init__(self, JimRs_Garage):
        self.settings = JimRs_Garage.settings

        self.width = 400
        self.settings.road_width = self.width
        self.height = self.settings.height
        self.screen = JimRs_Garage.screen

        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.midtop = JimRs_Garage.screen.get_rect().midtop
        self.color = (55, 55, 55)
        self.settings.road_left = self.rect.left

        self.lines = pygame.sprite.Group()

    def blit_road(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def lane_lines(self):

        if self.settings.frame_count % 145 - self.settings.env_speed == 0:
            new_line = Line(self)
            self.lines.add(new_line)

        for line in self.lines.copy():
            if line.rect.top > self.settings.height:
                self.lines.remove(line)
        
        self.lines.update()

    def update(self):
        self.blit_road()
        self.lane_lines()

    def clear_road(self):
        self.lines.empty()
        


class Line(pygame.sprite.Sprite):

    def __init__(self, road):

        super().__init__()

        self.width = 15
        self.height = 100
        self.color = (255, 255, 0)
        self.settings = road.settings
        self.screen = road.screen
        self.x = self.settings.width / 2 - self.width / 2
        self.y = -100
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.bottom = self.y
        self.rect.left = self.x
    
    def update(self):

        self.y += self.settings.env_speed
        self.rect.y = self.y
        self.rect.x = self.x
        self.blit_lines()
    
    def blit_lines(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

