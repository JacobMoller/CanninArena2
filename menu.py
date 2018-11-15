#################################
#          Authors:             #
#     Jacob Møller Jensen       #
#    Oliver Thejl Eriksen       #
#   Rasmus Damgaard-Iversen     #
#################################
import pygame
import time
pygame.init()

infoObject = pygame.display.Info()
displayWidth = infoObject.current_w
displayHeight = int(infoObject.current_h * 0.9)
gameWidth = int(infoObject.current_w * 0.35)
gameHeight = int(infoObject.current_h * 0.9)

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('CanninArena 2')
clock = pygame.time.Clock()

bgImg = pygame.image.load('Art/background/arena_bg.png')
bgImg = pygame.transform.scale(bgImg, (gameWidth, gameHeight))

playerWidth = 100
playerImg = pygame.image.load('Art/cannin/Cannin_32x32.png')
playerImg = pygame.transform.scale(playerImg, (playerWidth, playerWidth))

def player(x,y):
    gameDisplay.fill(black)
    gameDisplay.blit(bgImg,(((displayWidth/2)-(gameWidth/2)),0))
    gameDisplay.blit(playerImg,(x,y))

def textObject(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def messageDisplay(text):
    largeText = pygame.font.Font('Arial.ttf', 115)
    TextSurface, TextRectangle = textObject(text, largeText)
    TextRectangle.center = ((displayWidth/2),(displayHeight/2))
    gameDisplay.blit(TextSurface, TextRectangle)

    pygame.display.update()

    time.sleep(2)
    
    game_loop()

def game_loop():
    x = (displayWidth * 0.50 - (playerWidth/2))
    y = (gameHeight * 0.85)

    x_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change += -15
                if event.key == pygame.K_d:
                    x_change += 15
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    x_change += 15
                if event.key == pygame.K_d:
                    x_change += -15

        if x > (displayWidth * 0.5 + gameWidth * 0.5 - playerWidth):
            x = (displayWidth * 0.5 + gameWidth * 0.5  - playerWidth)
        elif x < (displayWidth * 0.5 - gameWidth * 0.5):
            x = (displayWidth * 0.5 - gameWidth * 0.5)
        else:
            x += x_change

        player(x,y)
        
        pygame.display.update()
        clock.tick(240)

game_loop()
pygame.quit()
quit()
