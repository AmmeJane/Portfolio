import pygame.font

class playButton():

    def __init__(self,aiSettings, screen):
        self.aiSettings = aiSettings
        self.screen = screen
        self.screenRect = screen.get_rect()

        #dimensions and properties
        self.width, self.height = 200, 50
        self.buttonColour = (0,255,0)
        self.textColour = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        #size and location
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screenRect.center

        #prep
        self.prepMsg("play")


    def prepMsg(self, msg):
        #turns msg into rendered image
        self.msgImage = self.font.render(msg, True, self.textColour, self.buttonColour)
        self.msgImageRect = self.msgImage.get_rect()
        self.msgImageRect.center = self.rect.center

    def drawButton(self):
        self.screen.fill(self.buttonColour, self.rect)
        self.screen.blit(self.msgImage, self.msgImageRect)

class storeButton():
    def __init__(self, aiSettings, screen):
        self.aiSettings = aiSettings
        self.screen = screen
        self.screenRect = screen.get_rect()

        # dimensions and properties
        self.width, self.height = 100, 50
        self.buttonColour = (255, 0, 0)
        self.textColour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # size and location
        self.rect = pygame.Rect(280, 20, self.width, self.height)

        # prep
        self.prepMsg("store")

    def prepMsg(self, msg):
        # turns msg into rendered image
        self.msgImage = self.font.render(msg, True, self.textColour, self.buttonColour)
        self.msgImageRect = self.msgImage.get_rect()
        self.msgImageRect.center = self.rect.center

    def drawButton(self):
        self.screen.fill(self.buttonColour, self.rect)
        self.screen.blit(self.msgImage, self.msgImageRect)


class leaderBoardButton():
    def __init__(self, aiSettings, screen):
        self.aiSettings = aiSettings
        self.screen = screen
        self.screenRect = screen.get_rect()

        # dimensions and properties
        self.width, self.height = 220, 50
        self.buttonColour = (0, 0, 255)
        self.textColour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # size and location
        self.rect = pygame.Rect(20, 20, self.width, self.height)

        # prep
        self.prepMsg("leaderboard")

    def prepMsg(self, msg):
        # turns msg into rendered image
        self.msgImage = self.font.render(msg, True, self.textColour, self.buttonColour)
        self.msgImageRect = self.msgImage.get_rect()
        self.msgImageRect.center = self.rect.center

    def drawButton(self):
        self.screen.fill(self.buttonColour, self.rect)
        self.screen.blit(self.msgImage, self.msgImageRect)

class gameExplaination():
    def __init__(self, aiSettings, screen):
        self.aiSettings = aiSettings
        self.screen = screen
        self.screenRect = screen.get_rect()

        # dimensions and properties
        self.width, self.height = 220, 50
        self.buttonColour = (0, 0, 0)
        self.textColour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # size and location
        self.rect = pygame.Rect(90, 400, self.width, self.height)

        # prep
        self.prepMsg("how to play")

    def prepMsg(self, msg):
        # turns msg into rendered image
        self.msgImage = self.font.render(msg, True, self.textColour, self.buttonColour)
        self.msgImageRect = self.msgImage.get_rect()
        self.msgImageRect.center = self.rect.center

    def drawButton(self):
        self.screen.fill(self.buttonColour, self.rect)
        self.screen.blit(self.msgImage, self.msgImageRect)


