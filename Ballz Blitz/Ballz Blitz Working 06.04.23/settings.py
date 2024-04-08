import random
from blocks import block

class settings():
    #stores all settings for Ballz
  
    def __init__(self):
        #intialises game settings
        
        #screen settings
        self.screenWidth = 400
        self.screenHeight = 600
        self.bgColour = (150,150,150)
        #ship settings
        self.crosshairSpeedFactor = 0.2

        #crosshair settings
        self.crosshairHeight = 250

        #fireball settings
        self.fireballSpeedFactor = 0.5
        self.fireballWidth = 3
        self.fireballHeight = 4
        self.fireballHitEdge = False

        #block settings
        self.blockWidth = 40
        self.blockHeight = 30
        self.blockColour = (50,50,50)
        self.blockSpeedFactor = 1

        #score settings
        self.stats = 0
        self.level = 1
        self.gameStatus = False
        self.playButtonPressed = False
        self.died = False

        self.timeLeft = float(10)

        #store settings
        self.storeButtonPressed = False

        self.reward = False
        self.rewardAccepted = False
        self.overFifty = False
        self.overHundred = False

        #leaderboard settings
        self.leaderBoardButtonPressed = False
        self.sortByPoints = True

        #user instructions settings
        self.userInstructionsButtonPressed = False

        #endgame settings
        self.gameOver = False

        #user settings
        #unlockEverything sets all user settings to true
        self.unlockEverything = False
        #ability to use store options
        self.boughtOptionOne = False
        self.boughtOptionTwo = False
        self.boughtOptionThree = False
        self.boughtOptionFour = False
        self.boughtOptionFive = False
        self.boughtOptionSix = False
        #money amount
        self.currency = 50
        #username
        self.username = "AmmeJane"

    def randomiseColours(self):
        self.bgColour = (random.randint(1, 255), \
                         random.randint(1, 255), \
                         random.randint(1, 255))
        self.blockColour = (random.randint(1, 255),
                            random.randint(1, 255),
                            random.randint(1, 255))
        while self.bgColour == self.blockColour:
            self.blockColour = (random.randint(1, 255),
                                random.randint(1, 255),
                                random.randint(1, 255))

