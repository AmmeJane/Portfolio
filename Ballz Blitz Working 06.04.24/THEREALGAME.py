#importing libraries
import pygame, random
from pygame.sprite import Group

#importing classes from files
import buttons
from settings import settings
from ship import crosshair as ch
from ship import fireship as fs
from scoreboard import scoreboard as sb
from scoreboard import levelTimer as lt
from store import makeStore as ms
from leaderBoard import leaderBoard as lb
import gameFunctions as gf
from rewards import rewardMenu as rm
from endGame import endGameMenu as eg
from userInstructions import userInstructions as ui

def runGame():
    #starts the game and creates screen object
    pygame.init()
    aiSettings = settings()

    if aiSettings.unlockEverything:
        aiSettings.boughtOptionOne = True
        aiSettings.boughtOptionTwo = True
        aiSettings.boughtOptionThree = True
        aiSettings.boughtOptionFour = True
        aiSettings.boughtOptionFive = True
        aiSettings.boughtOptionSix = True

    #fetches the screen size from settings
    screen = pygame.display.set_mode(
            (aiSettings.screenWidth,
             aiSettings.screenHeight))

    #game title
    pygame.display.set_caption("Ballz Blitz")

    #makes the crosshair
    crosshair = ch(aiSettings, screen)
    fireship = fs(aiSettings, screen)

    #makes objects
    scoreboard = sb(aiSettings, screen)
    timer = lt(aiSettings, screen)
    playButton = buttons.playButton(settings, screen)
    storeButton = buttons.storeButton(settings, screen)
    storeMenu = ms(aiSettings, screen)
    storeMenu.makeStoreWindow()
    leaderBoardButton = buttons.leaderBoardButton(aiSettings, screen)
    leaderboardMenu = lb(aiSettings, screen)
    userInstructionsButton = buttons.gameExplaination(settings, screen)
    userInstructions = ui(aiSettings, screen)
    reward = rm(aiSettings, screen)
    endgame = eg(aiSettings, screen)

    #makes group to put fireballs in
    fireballs = Group()
    blockz = Group()

    # starts the game main loop
    while True:
        # watches for keyboard and mouse events
        gf.checkEvents(aiSettings, screen, crosshair, fireship,
                       fireballs, blockz, playButton, leaderBoardButton,
                       storeButton, storeMenu, leaderboardMenu, timer,
                       reward, userInstructionsButton, userInstructions, endgame)

        if not aiSettings.gameStatus:
            if aiSettings.playButtonPressed:
                if not aiSettings.reward:
                    gf.endOldLevel(fireballs)
                    gf.startNewLevel(aiSettings)
                    timer.reset()
                    aiSettings.gameStatus = True
                else:
                    #rewards user and resets reward to False
                    #reward accepted changed in ai settings
                    gf.endOldLevel(fireballs)
                    if aiSettings.rewardAccepted:
                        aiSettings.reward = False
                        #below will be removed when chests work

            else:
                #code for before or after game
                gf.endGame(fireballs, blockz)
                timer.reset()
                scoreboard.reset()
                aiSettings.overFifty = False
                aiSettings.overHundred = False

        else:
            #updates ship

            crosshair.update()
            fireballs.update(crosshair, screen)
            blockz.update(fireballs)


            for fireball in fireballs:
                if fireball.rect.bottom <= 0:
                    fireballs.remove(fireball)

                for block in blockz:
                    #print(fireball.rect, block.rect)
                    collide = pygame.sprite.collide_rect(fireball, block)
                    block.strength = int(block.strength)
                    if collide:

                        #block has 1 left
                        if block.strength <= 1:

                            #hits block and can destroy
                            if fireball.canCollide:
                                blockz.remove(block)
                                scoreboard.stats += 1

                        #block has more than 1 left
                        elif block.strength > 1:

                            #hits block and can collide
                            if fireball.canCollide and fireball.movable:
                                block.strength -= 1
                                fireball.speedFactory *= -1
                                fireball.movable = False
                                scoreboard.stats += 1

                            #hits block and already not movable
                            elif fireball.canCollide and not fireball.movable:
                                block.strength -= 1
                                scoreboard.stats += 1

                            #hits block and can't collide
                            elif not fireball.canCollide:
                                if fireball.movable:
                                    fireball.speedFactory *= -1
                                    fireball.speedFactorx *= -1

                    block.strength = str(block.strength)



            if not aiSettings.reward:
                if scoreboard.stats >= 50 and not aiSettings.overFifty:
                    aiSettings.reward = True
                    aiSettings.overFifty = True
                    reward.generateChests()
                if scoreboard.stats >= 100 and not aiSettings.overHundred:
                    aiSettings.reward = True
                    aiSettings.overHundred = True
                    reward.generateChests()



            if bool(blockz) == 0:
                aiSettings.gameStatus = False
                aiSettings.level += 1

            if bool(blockz) != 0 and timer.timeLeft <= 0:
                gf.endGame(fireballs, blockz)
                aiSettings.playButtonPressed = False
                # add score to leaderboard txt file
                gf.updateLeaderboardFile(aiSettings.username, aiSettings.level, scoreboard.stats)
                aiSettings.level = 0
                aiSettings.gameOver = True


        #redraws screen during pass through loop and makes recently drawn screen visible
        gf.updateScreen(aiSettings, screen, scoreboard, crosshair,
                        fireship, fireballs, blockz, playButton, leaderBoardButton,
                        storeButton, storeMenu, leaderboardMenu, timer, reward,
                        userInstructionsButton, userInstructions, endgame)

        pygame.event.pump()
    
runGame()
