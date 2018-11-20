#################################
#          Authors:             #
#     Jacob Møller Jensen       #
#    Oliver Thejl Eriksen       #
#   Rasmus Damgaard-Iversen     #
#################################
import pygame
import time
import random
pygame.init()

#Define screen and game size
infoObject = pygame.display.Info()
displayWidth = infoObject.current_w
displayHeight = int(infoObject.current_h * 0.9)
gameWidth = int(infoObject.current_w * 0.35)
gameHeight = int(infoObject.current_h * 0.9)

#Define colors with rgb
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#Setup Screen Display
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('CanninArena 2')
clock = pygame.time.Clock()

#Load Background
bgImg = pygame.image.load('Art/background/arena_bg.png')
bgImg = pygame.transform.scale(bgImg, (gameWidth, gameHeight))

#Load player graphics and size
playerWidth = 64
playerImg = pygame.image.load('Art/cannin/Cannin_32x32.png')
playerImg = pygame.transform.scale(playerImg, (playerWidth, playerWidth))

tunnel_height = 200
tunnelImg = pygame.image.load('Art/background/tunnel_bg.png')
tunnelImg = pygame.transform.scale(tunnelImg, (gameWidth, tunnel_height))

def player(x,y, bg_movement):
    gameDisplay.fill(black)
    gameDisplay.blit(bgImg,(((displayWidth/2)-(gameWidth/2)),bg_movement))
    gameDisplay.blit(playerImg,(x,y))

def element(change_movement):
    gameDisplay.blit(tunnelImg,(((displayWidth/2)-(gameWidth/2)),change_movement))

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
    change_movement = random.randint(-500, 0)
    print(change_movement)
    bg_movement = 0

    x_change = 0

    tunnelCheck = False
    
    gameExit = False

    while not gameExit:
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.K_ESCAPE:
                menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change += -15
                if event.key == pygame.K_d:
                    x_change += 15
                #if event.key == pygame.K_ESCAPE:
                    #Open Menu
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

        
        if y < change_movement+tunnel_height and tunnelCheck == False:
            tunnelCheck = True
            print("Hej")
            print((displayWidth/2)-(gameWidth/2)+(gameWidth/100*(326/3000*100)))
            if x > (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(326/3000*100)) and x < (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(897/3000*100)):
                print("0")
            elif x > (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(998/3000*100)) and x < (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(1513/3000*100)):
                print("1")
            elif x > (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(1582/3000*100)) and x < (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(2053/3000*100)):
                print("2")
            elif x > (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(2150/3000*100)) and x < (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(2622/3000*100)):
                print("3")
            else:
                #DIE
                print("dead")
        
            
        #Updates player and game screen
        change_movement += 5
        #print(change_movement)
        bg_movement += 0
        player(x,y, bg_movement)
        element(change_movement)
        pygame.display.update()
        clock.tick(120)
game_loop()
pygame.quit()
quit()
