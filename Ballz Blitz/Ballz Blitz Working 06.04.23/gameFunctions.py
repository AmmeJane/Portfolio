import random
import sys, pygame,time

from fireball import fireball as fb
makeFireball = pygame.USEREVENT + 0

import blocks as blo
from blocks import block as bl

makeBlocks = pygame.USEREVENT + 1
makeBlocksEvent = pygame.event.Event(makeBlocks)




def checkEvents(aiSettings, screen, crosshair, fireship,
                fireballs, blockz, playButton, leaderBoardButton,
                storeButton, storeMenu, leaderboardMenu, timer,
                reward, userInstructionsButton, userInstructions, endgame):
    global makeBlocks
        #responds to key presses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #things to happen before game quits

            #exits game
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #checks all buttons
            mouseX, mouseY = pygame.mouse.get_pos()
            checkPlayButton(aiSettings, playButton, mouseX, mouseY)
            checkStoreButton(aiSettings, storeButton, mouseX, mouseY)
            storeMenu.checkStoreButtons(mouseX, mouseY)
            checkLeaderBoardButton(aiSettings, leaderBoardButton, mouseX, mouseY)
            leaderboardMenu.checkLeaderBoardExitButton(mouseX, mouseY)
            reward.checkChest(mouseX, mouseY)
            checkUserInstructionsButton(aiSettings, userInstructionsButton, mouseX, mouseY)
            userInstructions.checkInstructionsExitButton(mouseX, mouseY)
            endgame.checkEndGameExitButton(mouseX, mouseY)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                crosshair.movingRight = True
            if event.key == pygame.K_LEFT:
                crosshair.movingLeft = True
            if event.key == pygame.K_SPACE:
                if timer.timeLeft > 0 and aiSettings.playButtonPressed:
                    pygame.event.set_allowed(None)
                    #creates new fireball and adds it to group
                    pygame.time.set_timer(makeFireball, 10, 1)
                    timer.timeLeft -= 0.5
                else:
                    pygame.event.set_blocked(makeFireball) #hashtag to do fireballs again
                    aiSettings.gameStatus = False
                pygame.event.set_allowed(pygame.QUIT)
                crosshair.movingLeft = False
                crosshair.movingRight = False
            if event.key == pygame.K_ESCAPE:
                #make game end here
                pass


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                crosshair.movingRight = False
            if event.key == pygame.K_LEFT:
                crosshair.movingLeft = False
            if event.key == pygame.K_SPACE:
                pygame.event.set_allowed(makeFireball)
            if event.key == pygame.K_ESCAPE:
                aiSettings.gameStatus = False
                aiSettings.playButtonPressed = False

        elif event.type == makeFireball:
           newFireball = fb(aiSettings, screen, fireship, crosshair)
           fireballs.add(newFireball)

        elif event.type == makeBlocks:

            amountToSpawn = blo.amountOfBlocks

            if aiSettings.level < 10:
                blockType = 1
            elif aiSettings.level >= 10:
                blockType = random.randint(1,2)
            elif aiSettings.level > 20:
                blockType = 2
            elif aiSettings.level > 50:
                blockType = random.randint(1, 3)
            elif aiSettings.level > 75:
                blockType = random.randint(2, 3)

            for i in range(amountToSpawn):
                yaxis, xaxis = blo.getAxis()
                newBlock = bl(aiSettings, screen, fireballs, xaxis, yaxis, blockType)

                blockz.add(newBlock)

#checks collisions and buttons only work if certain conditions are met
def checkPlayButton(aiSettings, playButton, mouseX, mouseY):
    if playButton.rect.collidepoint(mouseX,mouseY)\
            and not aiSettings.gameStatus and not aiSettings.storeButtonPressed\
            and not aiSettings.leaderBoardButtonPressed and not aiSettings.reward\
            and not aiSettings.userInstructionsButtonPressed\
            and not aiSettings.gameOver:
        aiSettings.playButtonPressed = True
def checkStoreButton(aiSettings, storeButton, mouseX, mouseY):
    if storeButton.rect.collidepoint(mouseX, mouseY)\
            and not aiSettings.gameStatus and not aiSettings.leaderBoardButtonPressed\
            and not aiSettings.reward and not aiSettings.userInstructionsButtonPressed\
            and not aiSettings.gameOver:
        aiSettings.storeButtonPressed = True
def checkLeaderBoardButton(aiSettings, leaderBoardButton, mouseX, mouseY):
    if leaderBoardButton.rect.collidepoint(mouseX, mouseY)\
            and not aiSettings.gameStatus and not aiSettings.storeButtonPressed\
            and not aiSettings.reward and not aiSettings.userInstructionsButtonPressed\
            and not aiSettings.gameOver:
        aiSettings.leaderBoardButtonPressed = True
def checkUserInstructionsButton(aiSettings, userInstructionsButton, mouseX, mouseY):
    if userInstructionsButton.rect.collidepoint(mouseX, mouseY)\
            and not aiSettings.gameStatus and not aiSettings.storeButtonPressed\
            and not aiSettings.reward and not aiSettings.leaderBoardButtonPressed\
            and not aiSettings.gameOver:
        aiSettings.userInstructionsButtonPressed = True



def startNewLevel(aiSettings):
    global makeBlocks
    blo.makeAxis(aiSettings)
    pygame.event.post(makeBlocksEvent)


def endOldLevel(fireballs):
    pygame.event.clear()
    for sprite_ in fireballs:
        sprite_.kill()

def endGame(fireballs, blockz):
    pygame.event.clear()
    for fireball in fireballs:
        fireball.kill()
    for block in blockz:
        block.kill()

def updateLeaderboardFile(username, level, score):
    f = open("LeaderboardFile","a")
    l = ("\nUsername:"+username+" Level:"+str(level)+" Score:"+str(score))
    f.write(l)
    f.close()

def updateScreen(aiSettings, screen, scoreboard, crosshair,
                 fireship, fireballs, blockz, playButton, leaderBoardButton,
                 storeButton, storeMenu, leaderboardMenu,  timer, reward,
                 userInstructionsButton, userInstructions, endgame):
    #redraws screen during pass through loop
    screen.fill(aiSettings.bgColour)

    if not aiSettings.playButtonPressed \
            and not aiSettings.storeButtonPressed and not aiSettings.reward\
            and not aiSettings.leaderBoardButtonPressed\
            and not aiSettings.userInstructionsButtonPressed\
            and not aiSettings.gameOver:
        #pregame
        playButton.drawButton()
        storeButton.drawButton()
        leaderBoardButton.drawButton()
        userInstructionsButton.drawButton()


    elif aiSettings.playButtonPressed and aiSettings.gameStatus:
        #during game
        crosshair.blitMe()
        fireship.blitMe()

        scoreboard.prepScore()
        scoreboard.showScore()

        timer.update()
        timer.drawBoarder()
        timer.drawBar()

        screen.blit(pygame.font.SysFont('Arial', 20).render(
            ("Level "+str(aiSettings.level)),
            True, (0, 0, 0)), pygame.Rect(10, 440, 300, 50))

    elif aiSettings.storeButtonPressed:
        # store menu
        storeMenu.makeStoreWindow()

    elif aiSettings.leaderBoardButtonPressed:
        #leaderboard
        leaderboardMenu.makeLeaderboards()

    elif aiSettings.userInstructionsButtonPressed:
        #how to play
        userInstructions.makeInstructionsWindow()

    elif aiSettings.reward:
        #update screen with reward icons
        reward.makeRewardWindow()

    elif aiSettings.gameOver:
        endgame.makeEndgameWindow()


    for fireball in fireballs.sprites():
        #print("fireball")
        fireball.blitMe()
        #print("FIREBALLS")
    for block in blockz.sprites():
        block.drawMe(aiSettings)

    #makes recently drawn screen visible
    pygame.display.flip()

     
