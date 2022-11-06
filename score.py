import sys
import pygame

class Score:

    def __init__(self, Goat_Upgrader):
        self.text_color = (0,0,0)
        self.back_color = (255,255,255)
        self.font = pygame.font.SysFont("Comic Sans MS", 30)

        self.settings = Goat_Upgrader.settings
        self.screen = Goat_Upgrader.screen
        self.screen_rect = Goat_Upgrader.screen
        self.coin_score = 0

        self.score_text = self.font.render("Score: "+str(self.settings.frame_count), True, self.text_color)
        self.score_rect = self.score_text.get_rect()
        self.score_rect.topright = (self.settings.width - 10, 10)

        self.hs_text = self.font.render("High: "+str(self.settings.high_score), True, self.text_color)
        self.hs_rect = self.hs_text.get_rect()
        self.hs_rect.topright = (self.settings.width - 10, 50)

    def update(self):

        self.score_text = self.font.render("Score: "+str(self.settings.frame_count + self.coin_score), True, self.text_color)
        self.score_rect = self.score_text.get_rect()
        self.score_rect.topright = (self.settings.width - 10, 10)

        self.hs_text = self.font.render("High: "+str(self.settings.high_score), True, self.text_color)
        self.hs_rect = self.hs_text.get_rect()
        self.hs_rect.topright = (self.settings.width - 10, 50)

        self.screen.blit(self.score_text, self.score_rect)
        self.screen.blit(self.hs_text, self.hs_rect)

    def check_high_score(self):
        if self.settings.frame_count + self.coin_score > self.settings.high_score:
            self.settings.high_score = self.settings.frame_count + self.coin_score
            self.settings.frame_count = 0
            self.coin_score = 0