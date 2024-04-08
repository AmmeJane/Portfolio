import pygame, math
from pygame.sprite import Sprite
from ship import crosshair as ch


class fireball(Sprite):
    #to manage balls fired from the fireship to the crosshair

    def __init__(self, aiSettings, screen, fireship, crosshair):
        super().__init__()
        self.screen = screen
        self.aiSettings = aiSettings

        #can disable fireball collision to help with block bug
        self.canCollide = True
        self.movable = True

        #create a fireball rect at (0,0) then set correct position
        self.image = pygame.image.load("images/fireball.png")
        self.image1 = self.image
        self.image = pygame.transform.scale(self.image,(30,50))
        self.originalImage = self.image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rotation = 0

        #make new fireball where fireship is
        self.rect.centerx = fireship.rect.centerx
        self.rect.centery = fireship.rect.centery
        #self.rect.bottom = fireship.rect.bottom

        #store fireball position as decimal value
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        #rotating the fireball and image
        self.speedFactorx = aiSettings.fireballSpeedFactor
        self.speedFactory = aiSettings.fireballSpeedFactor

        self.hitEdge = aiSettings.fireballHitEdge

        # update position
        crosshairLocation = ch.getCrosshairLocation(crosshair)
        opposite = (self.x - crosshairLocation.x)
        adjacent = (self.y - crosshairLocation.y)
        # TOA
        try:
            self.hypotenuse = math.atan(opposite / adjacent)

        except:
            self.hypotenuse = 0

    def checkEdges(self):
        # printErrors("checking edges")
        screenRect = self.screen.get_rect()
        if self.rect.right == screenRect.right:
            self.speedFactorx *= -1
        elif self.rect.left == 0:
            self.speedFactorx *= -1
        elif self.rect.top == screenRect.top:
            self.speedFactory *= -1
        elif self.rect.bottom == screenRect.bottom:
            self.kill()


    def update(self, crosshair, screen):
        #move the fireball to the crosshair


        #code to find out what to do  (left/right, up, down and so on)
        #               |
        #               v

        self.checkEdges()

        self.y -= self.speedFactory
        self.x -= self.speedFactorx * self.hypotenuse

        self.rect.y = (self.y)
        self.rect.x = (self.x)


        if self.speedFactory < 0:
            self.rotation = -abs(math.degrees(self.hypotenuse)) * self.speedFactorx % 360
            self.rotation += 180
        else:
            self.rotation = math.degrees(self.hypotenuse) * self.speedFactorx % 360


        #rotating image
        #originalImage is y at 1 and x at 0
        self.image = pygame.transform.rotate(self.originalImage, self.rotation)
        #print(self.x,self.y, math.degrees(self.hypotenuse))
    def blitMe(self):
        #draw fireball on screen
        self.screen.blit(self.image, self.rect)





