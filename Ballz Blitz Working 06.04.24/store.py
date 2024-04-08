import pygame, itertools
from pygame.sprite import Sprite
from pygame.sprite import Group
pygame.font.init()

class makeStore():
    def __init__(self, aiSettings, screen):
        #basic setup
        self.aiSettings = aiSettings
        self.screen = screen
        self.screenRect = screen.get_rect()

        self.redColour = (255, 0, 0)
        self.colourButtons = Group()
        self.upgradeButtons = Group()
        self.themeButtons = Group()

        self.font = pygame.font.SysFont('Arial', 25)

        #import image for background
        self.background = pygame.image.load("images/storebackground.png")
        self.background1 = self.background

        #images for paint brushes
        #pink
        self.pinkPaintbrush = pygame.image.load("images/paintbrushpink.png")
        self.pinkPaintbrush = pygame.transform.scale(self.pinkPaintbrush, (50, 50))
        #green
        self.greenPaintbrush = pygame.image.load("images/paintbrushgreen.png")
        self.greenPaintbrush = pygame.transform.scale(self.greenPaintbrush, (50, 50))
        #blue
        self.bluePaintbrush = pygame.image.load("images/paintbrushblue.png")
        self.bluePaintbrush = pygame.transform.scale(self.bluePaintbrush, (50, 50))
        #random
        self.randomPaintbrush = pygame.image.load("images/paintbrushrandom.png")
        self.randomPaintbrush = pygame.transform.scale(self.randomPaintbrush, (50, 50))
        #list
        self.colourButtonsPaintbrushes = [
            self.pinkPaintbrush, self.greenPaintbrush, self.bluePaintbrush,
            self.bluePaintbrush, self.bluePaintbrush, self.randomPaintbrush]

        #images for upgrades
        #multishot
        #longertimer
        #morepoints

        #images for themes

        #image for exit
        self.exitButton = pygame.image.load("images/exitbutton.png")
        self.exitButton = pygame.transform.scale(self.exitButton, (50, 50))


        #colour buttons
        buttonX = 80
        buttonY = 80
        for buttonType in (self.colourButtons, self.upgradeButtons, self.themeButtons):
            for button in range(6):
                if buttonType == self.colourButtons:
                    imageUsed = self.colourButtonsPaintbrushes[button]
                else:
                    imageUsed = self.pinkPaintbrush
                if button == 3:
                    buttonY += 80
                    buttonX = 80
                newButton = storeButtons(aiSettings, screen, buttonX, buttonY, button+1, imageUsed)
                buttonType.add(newButton)
                #print(buttonType)

                buttonX += 95
            buttonX = 80
            buttonY += 100
        self.exitButton = storeButtons(aiSettings, screen, 350, 550, "exit", self.exitButton)

    def makeStoreWindow(self):
        # store menu
        #storeBox = pygame.draw.rect(self.screen, (255, 255, 255),
                                    #pygame.Rect(50, 150, 300, 300))
        #storeBoxTop = pygame.draw.rect(self.screen, self.redColour ,
                                       #pygame.Rect(50, 150, 300, 50))
        self.screen.blit(self.background, pygame.Rect(20, 0, 350, 500))

        for i in (self.colourButtons, self.upgradeButtons, self.themeButtons):
            i.update()
        self.exitButton.update()

        blockRect = pygame.Rect(325, 10, self.aiSettings.blockWidth+25, self.aiSettings.blockHeight)
        pygame.draw.rect(self.screen, self.aiSettings.blockColour, blockRect)
        self.screen.blit(self.font.render("Block", True, (self.aiSettings.bgColour)), (blockRect))

        self.screen.blit(
            pygame.font.SysFont('Arial', 25).render(
                (" £"+str(self.aiSettings.currency)), True, (0, 0, 0)), pygame.Rect(220, 20, 300, 50))

    def checkStoreButtons(self, mouseX, mouseY):
        counter = 0
        for button in self.colourButtons:
            counter += 1
            if button.rect.collidepoint(mouseX, mouseY) and self.aiSettings.storeButtonPressed:

                if counter == 1:
                    # pink
                    if self.aiSettings.boughtOptionOne:
                        self.aiSettings.blockColour = (145, 73, 126)
                        self.aiSettings.bgColour = (214, 169, 202)
                    else:
                        if self.aiSettings.currency >= 50:
                            self.aiSettings.currency -= 50
                            self.aiSettings.boughtOptionOne = True
                            button.colour = (0,255,0)
                            button.locked = False

                elif counter == 2:
                    # forest
                    if self.aiSettings.boughtOptionTwo:
                        self.aiSettings.blockColour = (115, 161, 105)
                        self.aiSettings.bgColour = (31, 85, 20)
                    else:
                        if self.aiSettings.currency >= 50:
                            self.aiSettings.currency -= 50
                            self.aiSettings.boughtOptionTwo = True
                            button.colour = (0, 255, 0)
                            button.locked = False

                elif counter == 3:
                    # foamy sea
                    if self.aiSettings.boughtOptionThree:
                        self.aiSettings.blockColour = (9, 58, 70)
                        self.aiSettings.bgColour = (60, 168, 150)
                    else:
                        if self.aiSettings.currency >= 50:
                            self.aiSettings.currency -= 50
                            self.aiSettings.boughtOptionThree = True
                            button.colour = (0, 255, 0)
                            button.locked = False

                elif counter == 4:
                    # not chosen
                    if self.aiSettings.boughtOptionFour:
                        self.aiSettings.blockColour = (145, 73, 126)
                        self.aiSettings.bgColour = (214, 169, 202)
                    else:
                        if self.aiSettings.currency >= 50:
                            self.aiSettings.currency -= 50
                            self.aiSettings.boughtOptionFour = True
                            button.colour = (0, 255, 0)
                            button.locked = False

                elif counter == 5:
                    # not chosen
                    if self.aiSettings.boughtOptionFive:
                        self.aiSettings.blockColour = (145, 73, 126)
                        self.aiSettings.bgColour = (214, 169, 202)
                    else:
                        if self.aiSettings.currency >= 50:
                            self.aiSettings.currency -= 50
                            self.aiSettings.boughtOptionFive = True
                            button.colour = (0, 255, 0)
                            button.locked = False

                elif counter == 6:
                    #randomised
                    if self.aiSettings.boughtOptionSix:
                        self.aiSettings.randomiseColours()
                    else:
                        if self.aiSettings.currency >= 100:
                            self.aiSettings.currency -= 100
                            self.aiSettings.boughtOptionSix = True
                            button.colour = (0, 255, 0)
                            button.locked = False

        if self.exitButton.rect.collidepoint(mouseX, mouseY):
            self.aiSettings.storeButtonPressed = False


class storeButtons(Sprite):
    def __init__(self, aiSettings, screen, x, y, text, image):
        super().__init__()
        self.screen = screen
        self.aiSettings = aiSettings
        self.colour = (255, 0, 0)
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.text = str(text)
        self.textColour = (0, 0, 0)
        self.font = pygame.font.SysFont('Arial', 25)
        self.locked = True
        if self.text == "exit":
            self.locked = False
        self.image = image
        self.chains = pygame.image.load("images/chains.png")
        self.chains1 = self.chains

    def update(self):
        self.rect.y = (self.y)
        self.rect.x = (self.x)

        self.screen.blit(self.image, pygame.Rect(self.x, self.y, self.width, self.height))
        if self.locked:
            self.screen.blit(self.chains, pygame.Rect(self.x, self.y, self.width, self.height))