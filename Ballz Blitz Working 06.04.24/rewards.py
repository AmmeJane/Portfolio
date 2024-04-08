import pygame, random
from pygame.sprite import Sprite
from pygame.sprite import Group

class rewardMenu():
    def __init__(self, aiSettings, screen):
        self.aiSettings = aiSettings
        self.screen = screen
        self.screenRect = screen.get_rect()

        self.background = pygame.image.load("images/rewardsbackground.png")


        self.chests = Group()

    def makeRewardWindow(self):
        self.screen.blit(self.background, pygame.Rect(20, 0, 350, 500))
        for chest in self.chests:
            #place chests
            self.screen.blit(chest.chestImage, chest.rect)


    def generateChests(self):
        x, y = 0, 0
        for i in range(1,4):
            if i == 1:
                x, y = 70, 185
            elif i == 2:
                x, y = 100, 345
            elif i == 3:
                x, y = 60, 500
            newChest = chest(x, y)
            self.chests.add(newChest)
            print(x,y)

    def checkChest(self, mouseX, mouseY):
        for chest in self.chests:
            if chest.rect.collidepoint(mouseX, mouseY) and self.aiSettings.reward:
                self.aiSettings.currency += chest.rewardAmount
                print(chest.rewardAmount)
                self.aiSettings.rewardAccepted = True

class chest(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.chestImage = pygame.image.load("images/chest.png")
        self.chestImage = pygame.transform.scale(self.chestImage, (100, 100))
        self.rewardAmount = random.choice([25, 50, 100, 250])
        self.rect = pygame.Rect(x, y, 80, 80)

