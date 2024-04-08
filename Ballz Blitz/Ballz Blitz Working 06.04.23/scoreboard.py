import pygame
import settings as AiSettings

class scoreboard():

    def __init__(self,aiSettings, screen):
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.aiSettings = aiSettings
        self.stats = self.aiSettings.stats

        #font settings
        self.font = pygame.font.SysFont('Arial', 25)
        self.textColour = aiSettings.blockColour

    def prepScore(self):
        #make score into rendered image
        scoreString = str(self.stats)
        self.scoreImage = self.font.render(scoreString,True, self.textColour,
                                           self.aiSettings.bgColour)
        #display score top right of screen
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.right = self.screenRect.right - 20
        self.scoreRect.bottom = 580

    def showScore(self):
        self.screen.blit(self.scoreImage, self.scoreRect)

    def reset(self):
        self.stats = self.aiSettings.stats


class levelTimer():

    def __init__(self, aiSettings, screen):
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.aiSettings = aiSettings

        #make the boarder
        self.boarderWidth = 20
        self.boarderHeight = 80
        self.boarderRect = pygame.Rect(320, 500, self.boarderWidth, self.boarderHeight)
        self.boarderColour = (0,0,0)

        # make the bar
        self.barWidth = 16
        self.barHeight = 76
        self.barY = 502
        self.barColour = (0, 255, 0)
        self.timeLeft = self.aiSettings.timeLeft

        self.bar = "null"

        pygame.display.update()

    def update(self):
        newBarHeight = self.timeLeft * 7.6
        self.barHeight = newBarHeight
        self.barY = 578 - newBarHeight


    def reset(self):
        self.timeLeft = self.aiSettings.timeLeft

    def drawBoarder(self):
        pygame.draw.rect(self.screen, self.boarderColour, self.boarderRect)

    def drawBar(self):
        self.bar = pygame.draw.rect(self.screen, self.barColour, pygame.Rect(
            322, self.barY, self.barWidth, self.barHeight))

