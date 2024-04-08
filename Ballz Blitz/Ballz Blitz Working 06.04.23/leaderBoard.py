import pygame

class leaderBoard():
    def __init__(self, aiSettings, screen):
        self.screen = screen
        self.aiSettings = aiSettings

        #import image for background
        self.image = pygame.image.load("images/leaderboardbackground.png")
        self.image1 = self.image

        #rect
        self.rect = pygame.Rect(20, 20, 300, 500)
        #button rects
        self.titleRect = pygame.Rect(60, 20, 300, 50)
        self.sortButtonRect = pygame.Rect(230, 20, 300, 50)
        self.exitButtonRect = pygame.Rect(300, 20, 300, 50)

        #exit button
        self.exitButton = self.screen.blit(
                            pygame.font.SysFont('Arial', 25).render(
                                ("exit"),
                                True, (0, 0, 0)), self.exitButtonRect)
        # sort button
        self.sortButton = self.screen.blit(
            pygame.font.SysFont('Arial', 25).render(
                ("sort"),
                True, (0, 0, 0)), self.sortButtonRect)

    def makeLeaderboards(self):
        #leaderboard text
        self.screen.blit(
            pygame.font.SysFont('Arial', 25).render(
                ("Leaderboard"),
                True, (0, 0, 0)), self.titleRect)
        #leaderboard text button
        self.screen.blit(
            pygame.font.SysFont('Arial', 25).render(
                ("exit"),
                True, (0, 0, 0)), self.exitButtonRect)
        self.screen.blit(
            pygame.font.SysFont('Arial', 25).render(
                ("sort"),
                True, (0, 0, 0)), self.sortButtonRect)
        #leaderboard board background
        self.screen.blit(self.image, self.rect)

        #get file into list
        f = open("LeaderboardFile", "r")
        listData = f.read()
        theList = listData.split("\n")
        f.close()

        newList = []
        #sorting then printing the list
        for item in theList:
            items = item.split(' ')
            points = str(items[2]).split(":")[0]
            level = str(items[1]).split(":")[0]
            pointsNum = str(items[2]).split(":")[1]
            levelNum = str(items[1]).split(":")[1]
            newList.append(points+" "+ pointsNum+" "+level+" "+levelNum)

        if self.aiSettings.sortByPoints:
            newList.sort(key=lambda x: int(x.split()[1]), reverse = True)
        if not self.aiSettings.sortByPoints:
            newList.sort(key=lambda x: int(x.split()[3]), reverse = True)

        row = 115
        counter = 0
        for i in range(10):
            row += 35
            try:
                leaderboardText = newList[counter]
            except:
                leaderboardText = "Name"
            counter += 1
            if counter != 10:
                tempCounter = ("  "+str(counter))
            else:
                tempCounter = str(counter)
            self.screen.blit(
                pygame.font.SysFont('Arial', 16).render(
                    (str(tempCounter)+") "+leaderboardText),
                    True, (0, 0, 0)), pygame.Rect(110, row, 300, 50))

    def checkLeaderBoardExitButton(self, mouseX, mouseY):
        if self.exitButton.collidepoint(mouseX, mouseY) and self.aiSettings.leaderBoardButtonPressed:
            self.aiSettings.leaderBoardButtonPressed = False
        if self.sortButton.collidepoint(mouseX, mouseY) and self.aiSettings.leaderBoardButtonPressed:
            if not self.aiSettings.sortByPoints:
                self.aiSettings.sortByPoints = True
            elif self.aiSettings.sortByPoints:
                self.aiSettings.sortByPoints = False