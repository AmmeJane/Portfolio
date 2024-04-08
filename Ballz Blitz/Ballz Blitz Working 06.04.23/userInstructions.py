import pygame

class userInstructions():
    def __init__(self, aiSettings, screen):
        self.aiSettings = aiSettings
        self.screen = screen
        self.screenRect = screen.get_rect()

        self.image = pygame.image.load("images/instructionsbackground.png")
        #pygame.transform.scale(self.image, (200, 200))
        self.background = self.image
        self.backgroundRect = pygame.Rect(20, 20, 300, 500)

        self.exitButtonRect = pygame.Rect(300, 20, 300, 50)
        self.exitButton = self.screen.blit(
                            pygame.font.SysFont('Arial', 25).render(
                                ("exit"),
                                True, (0, 0, 0)), self.exitButtonRect)

    def makeInstructionsWindow(self):
        self.screen.blit(self.background, self.backgroundRect)
        self.randoInstr()
        self.screen.blit(
            pygame.font.SysFont('Arial', 25).render(
                ("exit"),
                True, (0, 0, 0)), self.exitButtonRect)


    def checkInstructionsExitButton(self, mouseX, mouseY):
        if self.exitButton.collidepoint(mouseX, mouseY) and self.aiSettings.userInstructionsButtonPressed:
            self.aiSettings.userInstructionsButtonPressed = False

    def randoInstr(self):
        # user instructions

        def makeText(text,pos, size):
            self.screen.blit(
                pygame.font.SysFont('Arial', size).render(
                    (text),
                    True, (0, 0, 0)), pos)
        makeText("User Instructions:", pygame.Rect(40, 20, 300, 50), 25)
        makeText("Left and right arrow keys",pygame.Rect(80, 150, 300, 50), 20)
        makeText("to move crosshair.", pygame.Rect(120, 180, 300, 50), 20)
        makeText("Spacebar to shoot fireballs.", pygame.Rect(80, 230, 300, 50), 20)
        makeText("Destroy all blocks before", pygame.Rect(80, 280, 300, 50), 20)
        makeText("you run out of shots.", pygame.Rect(120, 310, 300, 50), 20)

        makeText("You can make money", pygame.Rect(80, 360, 300, 50), 20)
        makeText("every 50 points.", pygame.Rect(120, 390, 300, 50), 20)

        makeText("Press escape key to quit.", pygame.Rect(80, 440, 300, 50), 20)
