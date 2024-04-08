import pygame, random
from pygame.sprite import Group

class endGameMenu():
    def __init__(self, aiSettings, screen):
        self.aiSettings = aiSettings
        self.screen = screen
        self.screenRect = screen.get_rect()

        self.background = pygame.image.load("images/gameoverbackground.png")

        # button rects
        self.playAgainButtonRect = pygame.Rect(95, 560, 300, 50)
        self.menuButtonRect = pygame.Rect(255, 560, 300, 50)

        # exit button
        self.playAgainButton = self.screen.blit(
            pygame.font.SysFont('Arial', 25).render(
                ("Again"),
                True, (0, 0, 0)), self.playAgainButtonRect)
        # sort button
        self.menuButton = self.screen.blit(
            pygame.font.SysFont('Arial', 25).render(
                ("Menu"),
                True, (0, 0, 0)), self.menuButtonRect)

        self.levelText = "You got to level " + str(self.aiSettings.level)
        self.scoreText = "Your score is " + str(self.aiSettings.stats)


    def makeEndgameWindow(self):
        #backgroud
        self.screen.blit(self.background, pygame.Rect(20, 0, 350, 500))

        #text
        self.screen.blit(
            pygame.font.SysFont('Arial', 25).render(
                (self.levelText ),
                True, (0, 0, 0)), pygame.Rect(80, 350, 300, 500))
        self.screen.blit(
            pygame.font.SysFont('Arial', 25).render(
                (self.scoreText),
                True, (0, 0, 0)), pygame.Rect(80, 400, 300, 500))

        #buttons
        self.screen.blit(
            pygame.font.SysFont('Arial', 25).render(
                ("Again"),
                True, (0, 0, 0)), self.playAgainButtonRect)
        self.screen.blit(
            pygame.font.SysFont('Arial', 25).render(
                ("Menu"),
                True, (0, 0, 0)), self.menuButtonRect)

    def checkEndGameExitButton(self, mouseX, mouseY):
        if self.playAgainButton.collidepoint(mouseX, mouseY):
            self.aiSettings.gameOver = False
            self.aiSettings.playButtonPressed = True

        if self.menuButton.collidepoint(mouseX, mouseY):
            self.aiSettings.gameOver = False