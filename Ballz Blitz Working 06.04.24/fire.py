import pygame

class fire():

    def __init__(self, screen):

        #initalise the fire and set its starting position
        self.screen = screen

        #load the fire and get its rect
        self.image = pygame.image.load("images/fire.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect

        #make new ball at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitMe(self):
        #draw ship at location
        self.screen.blit(self.image, self.rect)

