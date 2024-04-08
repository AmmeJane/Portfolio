import pygame

class crosshair():

    def __init__(self, aiSettings: object, screen: object) -> object:

        #initalise the fire and set its starting position
        self.screen = screen
        self.aiSettings = aiSettings

        #load the fire and get its rect
        self.image = pygame.image.load("images/pixelCrosshair.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #make crosshair at nearesh top center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.y = aiSettings.crosshairHeight
            #self.rect.bottom = self.screen_rect.bottom

        #store a decimal value for ship speed
        self.center = float(self.rect.centerx)


        #movement flags
        self.movingRight = False
        self.movingLeft = False

    def getCrosshairLocation(self):
        self.rect.x = self.rect.x + 10
        return self.rect

    def update(self):
        #update the ships position based on the movement flag
        if self.movingRight and self.rect.right < self.screen_rect.right:
            self.center += self.aiSettings.crosshairSpeedFactor
        if self.movingLeft and self.rect.left > 0:
            self.center -= self.aiSettings.crosshairSpeedFactor
        #update rect object from self.center
        self.rect.centerx = self.center

    def blitMe(self):
        #draw ship at location
        self.screen.blit(self.image, self.rect)


class fireship():
    
    def __init__(self, aiSettings, screen):
        #initalise the fire and set its starting position
        self.screen = screen
        self.aiSettings = aiSettings

        #load the fire and get its rect
        self.image = pygame.image.load("images/fire1.png")
        self.image = pygame.transform.scale(self.image,(150,150))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #make new ball at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitMe(self):
        #draw ship at location
        self.screen.blit(self.image, self.rect)
