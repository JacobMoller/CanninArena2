#################################
#          Authors:             #
#     Jacob Møller Jensen       #
#    Oliver Thejl Eriksen       #
#   Rasmus Damgaard-Iversen     #
#################################
import pygame
import time
pygame.init()

displayWidth = 500
displayHeight = 650

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('CanninArena 2')
clock = pygame.time.Clock()

backgroundImg = pygame.image.load('Art/baggrund/CanninArenaBackground-01.png')
gameDisplay.blit(backgroundImg,(x,y))

playerImg = pygame.image.load('Art/Canin/Cannin32x32.png')
playerImg = pygame.transform.scale(playerImg, (playerWidth, playerWidth))
playerWidth = 100

def player(x,y):
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

    x = (displayWidth * 0.45)
    y = (displayHeight * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change += -4
                if event.key == pygame.K_d:
                    x_change += 4
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    x_change += 4
                if event.key == pygame.K_d:
                    x_change += -4
        if x > displayWidth - playerWidth:
            x = displayWidth - playerWidth
        elif x < 0:
            x = 0
        else:
            x += x_change
        
        gameDisplay.fill(red)
        player(x,y)
    
        
            
        pygame.display.update()
        clock.tick(120)



game_loop()
pygame.quit()
quit()
