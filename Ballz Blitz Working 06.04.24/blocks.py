import pygame, random

pygame.font.init()

from pygame.sprite import Sprite

class block(Sprite):

    #to manage blocks spawned from the round starting to the above the crosshair
    def __init__(self, aiSettings, screen, fireballs, xaxis, yaxis, blockType):
        #global locations
        super().__init__()
        self.screen = screen
        self.aiSettings = aiSettings
        self.type = type

        self.alive = True

        #create a block rect at (0,0) then set correct position
        self.rect = pygame.Rect(int(xaxis),int(yaxis), aiSettings.blockWidth,aiSettings.blockHeight)

        #store block position as decimal value
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.speedFactor = aiSettings.blockSpeedFactor
        self.colour = aiSettings.blockColour

        #for block strength based on level number
        # higher the level, higher the total block strength, decided in gf
        if blockType == 1:
            self.strength = random.randint(1, 5)
        elif blockType == 2:
            self.strength = random.randint(1, 10)
        elif blockType == 3:
            self.strength = random.randint(5, 20)

        self.strength = str(self.strength)

        self.font = pygame.font.SysFont('Arial', 25)
        self.textColour = aiSettings.bgColour

        self.spawnTimer = 3000

        pygame.display.update()

    def update(self, fireballs):
        #update rect position
        self.rect.y = self.y
        self.rect.x = self.x

    def drawMe(self, aiSettings):
        #draw block on screen
        pygame.draw.rect(self.screen, self.colour, self.rect)
        self.screen.blit(self.font.render(self.strength, True, (self.textColour)), (self.rect))

def getAxis():
    #find area to place block
    global positions, locations
    foundOne = False
    y = -1
    for i in positions:
        x=-1
        y+= 1
        for j in i:
            x+=1
            if positions[y][x] == 1:
                positions[y][x] = 2
                both = locations[0][y][x]
                both = both.split()
                x1 = both[0]
                y1 = both[1]
                xaxis = x1
                yaxis = y1
                foundOne = True
                return yaxis, xaxis
    y=-1

def makeAxis(aiSettings):
    #makes table and places blocks in them
    global positions, locations, amountOfBlocks
    amountOfBlocks = 0
    #totalBlockStrength = aiSetiings*2
    #grid
    positions = [] # positions the blocks are placed
    locations = [] # compares table to find coordinates to place blocks

    for i in range(3):
        positions.append([0,0,0,0,0,0,0,0,0,0]) #ID


    while amountOfBlocks == 0:
        y = -1
        for i in positions:
            x=-1
            y+= 1
            for j in i:
                x+=1
                #this is the chance of blocks and i want a level system
                #higher the level, higher the total blocks
                totalBlocksAllowed = int(aiSettings.level) * 2
                #higher the level, higher the chance to spawn a block
                if aiSettings.level < 3:
                    chanceFraction = 25
                elif aiSettings.level < 10:
                    chanceFraction = 15
                elif aiSettings.level >= 10:
                    chanceFraction = 10
                elif aiSettings.level > 20:
                    chanceFraction = 8
                elif aiSettings.level > 50:
                    chanceFraction = 5
                elif aiSettings.level > 75:
                    chanceFraction = 2
                chanceNumber = random.randint(1,chanceFraction)
                if chanceNumber == 1 and amountOfBlocks < totalBlocksAllowed:
                    amountOfBlocks += 1
                    positions[y][x] = 1
        y=-1



    #unefficient method
    locations.append([["0 0","40 0","80 0","120 0","160 0","200 0","240 0","280 0","320 0","360 0"],
                      ["0 30","40 30","80 30","120 30","160 30","200 30","240 30","280 30","320 30","360 30"],
                      ["0 60","40 60","80 60","120 60","160 60","200 60","240 60","280 60","320 60","360 60"]]) #xy
    #efficient method
    #grid length is 10 with blocks 40 long and 30 tall

def makeBlock(aiSettings, screen, fireballs, xaxis, yaxis, blockType):
    newBlock = block(aiSettings, screen, fireballs, xaxis, yaxis, blockType)

