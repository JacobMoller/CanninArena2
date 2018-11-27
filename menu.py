#################################
#          Authors:             #
#     Jacob Møller Jensen       #
#    Oliver Thejl Eriksen       #
#   Rasmus Damgaard-Iversen     #
#################################
import pygame
import pygame.freetype
import time
import random
pygame.init()
pygame.font.init()

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

#Define tunnel succes
tunneldone = 0
removecount = 0

#Setup Screen Display
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('CanninArena 2')
clock = pygame.time.Clock()

#Load Background
bgImg = pygame.image.load('Art/background/arena_bg.png')
bgImg = pygame.transform.scale(bgImg, (gameWidth, gameHeight))

#Load player graphics and size
playerWidth = 64
playerImg = pygame.image.load('Art/cannin/Skin/cannin_red.png')
playerImg = pygame.transform.scale(playerImg, (playerWidth, playerWidth))

tunnel_height = 200
tunnelImg = pygame.image.load('Art/background/tunnel_bg.png')
tunnelImg = pygame.transform.scale(tunnelImg, (gameWidth, tunnel_height))


#Load Carrots
carrotOneImg = pygame.image.load('Art/carrot/carrot_black_32x32.png')
carrotOneImg = pygame.transform.scale(carrotOneImg, (40, 40))
carrotOneDoneImg = pygame.image.load('Art/carrot/carrot_32x32.png')
carrotOneDoneImg = pygame.transform.scale(carrotOneDoneImg, (40, 40))
carrotTwoImg = pygame.image.load('Art/carrot/carrot_black_32x32.png')
carrotTwoImg = pygame.transform.scale(carrotTwoImg, (40, 40))
carrotTwoDoneImg = pygame.image.load('Art/carrot/carrot_32x32.png')
carrotTwoDoneImg = pygame.transform.scale(carrotTwoDoneImg, (40, 40))
carrotThreeImg = pygame.image.load('Art/carrot/carrot_black_32x32.png')
carrotThreeImg = pygame.transform.scale(carrotThreeImg, (40, 40))
carrotThreeDoneImg = pygame.image.load('Art/carrot/carrot_32x32.png')
carrotThreeDoneImg = pygame.transform.scale(carrotThreeDoneImg, (40, 40))
topGoalLineImg = pygame.image.load('Art/background/goalline.png')
topGoalLineImg = pygame.transform.scale(topGoalLineImg, (gameWidth-(150), 40))
topGoalLineCanninImg = pygame.image.load('Art/cannin/Skin/cannin_default.png')
topGoalLineCanninImg = pygame.transform.scale(topGoalLineCanninImg, (20, 20))

def player(x,y, bg_movement):
    gameDisplay.fill(black)
    gameDisplay.blit(bgImg,(((displayWidth/2)-(gameWidth/2)),bg_movement))
    gameDisplay.blit(playerImg,(x,y))
    

def element(change_movement):
    gameDisplay.blit(tunnelImg,(((displayWidth/2)-(gameWidth/2)),change_movement))
    gameDisplay.blit(topGoalLineImg,((((displayWidth/2)-(gameWidth/2))+140),10))
    gameDisplay.blit(topGoalLineCanninImg,((((displayWidth/2)-(gameWidth/2))+140),30))
    gameDisplay.blit(carrotOneImg,((((displayWidth/2)-(gameWidth/2))+10),10))
    if tunneldone == 1:
        gameDisplay.blit(carrotOneDoneImg,((((displayWidth/2)-(gameWidth/2))+10),10))
    gameDisplay.blit(carrotTwoImg,((((displayWidth/2)-(gameWidth/2))+50),10))
    if tunneldone == 2:
        gameDisplay.blit(carrotOneDoneImg,((((displayWidth/2)-(gameWidth/2))+10),10))
        gameDisplay.blit(carrotTwoDoneImg,((((displayWidth/2)-(gameWidth/2))+50),10))
    gameDisplay.blit(carrotThreeImg,((((displayWidth/2)-(gameWidth/2))+90),10))
    if tunneldone == 3:
        #Level succes
        gameDisplay.blit(carrotOneDoneImg,((((displayWidth/2)-(gameWidth/2))+10),10))
        gameDisplay.blit(carrotTwoDoneImg,((((displayWidth/2)-(gameWidth/2))+50),10))
        gameDisplay.blit(carrotThreeDoneImg,((((displayWidth/2)-(gameWidth/2))+90),10))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('arial.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((displayWidth/2),(gameHeight/2))
    gameDisplay.blit(TextSurf, TextRect)
    
def crash():
    message_display('You Crashed')


def tunneltext_objects(text, font):
    tunneltextSurface = font.render(text, True, black)
    return tunneltextSurface, tunneltextSurface.get_rect()

def tunnelmessage_display(text, movement, textnumber):
    if textnumber == 1:
        xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*17)
        ycoordinate = movement+(displayHeight/100*5)
        if len(text) > 5:
            textSize = 15
            xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*19)
        elif len(text) > 12:
            textSize = 10
        else:
            textSize = 20
    if textnumber == 2:
        xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*38)
        ycoordinate = movement+(displayHeight/100*5)
        if len(text) > 5:
            textSize = 15
            xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*40)
        elif len(text) > 12:
            textSize = 10
        else:
            textSize = 20
    if textnumber == 3:
        xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*60)
        ycoordinate = movement+(displayHeight/100*5)
        if len(text) > 5:
            textSize = 15
            xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*62)
        elif len(text) > 12:
            textSize = 10
        else:
            textSize = 20
    if textnumber == 4:
        xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*76)
        ycoordinate = movement+(displayHeight/100*5)
        if len(text) > 5:
            textSize = 15
            xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*78)
        elif len(text) > 12:
            textSize = 10
        else:
            textSize = 20
    if textnumber == 5:
        xcoordinate = (displayWidth/2)
        ycoordinate = movement+(displayHeight/100*15)
        if len(text) < 10 and len(text) < 24:
            textSize = 35
            xcoordinate = ((displayWidth/2)-(gameWidth/2))
        elif len(text) < 25:
            textSize = 20
        else:
            textSize = 15
    tunnelLargeText = pygame.font.Font('arial.ttf',textSize)
    tunnelTextSurf, tunnelTextRect = text_objects(text, tunnelLargeText)
    tunnelTextRect.center = (xcoordinate,ycoordinate)
    gameDisplay.blit(tunnelTextSurf, tunnelTextRect)

def game_loop():
    x = (displayWidth * 0.50 - (playerWidth/2))
    y = (gameHeight * 0.85)
    change_movement = random.randint(-250, 0) #SKAL ÆNDRES TIL -1500,0
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
            print((displayWidth/2)-(gameWidth/2)+(gameWidth/100*(326/3000*100)))
            if x+(playerWidth/2) > (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(326/3000*100)) and x+(playerWidth/2) < (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(897/3000*100)):
                print("0")
                global tunneldone
                tunneldone += 1
            elif x+(playerWidth/2) > (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(998/3000*100)) and x+(playerWidth/2) < (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(1513/3000*100)):
                print("1")
            elif x+(playerWidth/2) > (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(1582/3000*100)) and x+(playerWidth/2) < (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(2053/3000*100)):
                print("2")
            elif x+(playerWidth/2) > (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(2150/3000*100)) and x+(playerWidth/2) < (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(2622/3000*100)):
                print("3")
                crash()
            else:
                #DIE
                print("dead")
        #Updates player and game screen
        change_movement += 5
        #print(change_movement)
        bg_movement += 0
        player(x,y, bg_movement)
        element(change_movement)
        if tunneldone == 1:
            message_display("Din første gulerod! :)")
            removecount +=1
            remove_message(removecount)
        elif tunneldone == 3:
            message_display("Godt arbejde!")
        tunnelmessage_display("Danmark", change_movement, 1)
        tunnelmessage_display("Sverige", change_movement, 2)
        tunnelmessage_display("Norge", change_movement, 3)
        tunnelmessage_display("Tyskland", change_movement, 4)
        tunnelmessage_display("København er hovedstaden i", change_movement, 5)
        pygame.display.update()
        clock.tick(10)
game_loop()
pygame.quit()
quit()
