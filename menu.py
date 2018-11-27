#################################
#          Authors:             #
#     Jacob Møller Jensen       #
#    Oliver Thejl Eriksen       #
#   Rasmus Damgaard-Iversen     #
#################################
import pygame
import pygame.freetype
import time
import math
import random
import math
import platform
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

#Define question variables
textQ = ""
choicesQ = []
answerQ = 0

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

def message_display(text, count):
    if count < 30:
        largeText = pygame.font.Font('arial.ttf',50)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((displayWidth/2),(gameHeight/2))
        gameDisplay.blit(TextSurf, TextRect) 
def crash():
    message_display('You Crashed')


def tunneltext_objects(text, font):
    tunneltextSurface = font.render(text, True, black)
    return tunneltextSurface, tunneltextSurface.get_rect()

def openMenu():
    gameDisplay.fill(red)
    print("Menu open")
    pygame.display.update()

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
    generateGate = True
    level = 1
    global textQ
    global choicesQ
    global answerQ

    tunnelCheck = False

    gameExit = False

    while not gameExit:
        if (generateGate == True):
            textQ, choicesQ, answerQ = DanishQ()
            generateGate = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.K_ESCAPE:
                menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    x_change += -15
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x_change += 15
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    x_change += 15
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x_change += -15

        if x > (displayWidth * 0.5 + gameWidth * 0.5 - playerWidth):
            x = (displayWidth * 0.5 + gameWidth * 0.5  - playerWidth)
        elif x < (displayWidth * 0.5 - gameWidth * 0.5):
            x = (displayWidth * 0.5 - gameWidth * 0.5)
        else:
            x += x_change


        if y < change_movement+tunnel_height and tunnelCheck == False:
            tunnelCheck = True
            tunnelChosen = None
            print((displayWidth/2)-(gameWidth/2)+(gameWidth/100*(326/3000*100)))
            if x+(playerWidth/2) > (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(326/3000*100)) and x+(playerWidth/2) < (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(897/3000*100)):
                tunnelChosen = 0
            elif x+(playerWidth/2) > (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(998/3000*100)) and x+(playerWidth/2) < (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(1513/3000*100)):
                tunnelChosen = 1
            elif x+(playerWidth/2) > (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(1582/3000*100)) and x+(playerWidth/2) < (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(2053/3000*100)):
                tunnelChosen = 2
            elif x+(playerWidth/2) > (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(2150/3000*100)) and x+(playerWidth/2) < (displayWidth/2)-(gameWidth/2)+(gameWidth/100*(2622/3000*100)):
                tunnelChosen = 3
            print("Gate: ", tunnelChosen)
            global tunneldone
            if(tunnelChosen == answerQ):
                tunneldone += 1
            else:
                print("Chose wrong gate: Call crash")
                crash()

        #Updates player and game screen
        change_movement += 5
        print(change_movement)
        #int(math.sqrt(math.pow((-500),2)))/100
        bg_movement += 0
        player(x,y, bg_movement)
        element(change_movement)
        if tunneldone == 1:
            global removecount
            removecount +=1
            message_display("Din første gulerod! :)", removecount)
            #removecount +=1
            #remove_message(removecount)
        elif tunneldone == 3:
            message_display("Godt arbejde!")
        tunnelmessage_display(choicesQ[0], change_movement, 1)
        tunnelmessage_display(choicesQ[1], change_movement, 2)
        tunnelmessage_display(choicesQ[2], change_movement, 3)
        tunnelmessage_display(choicesQ[3], change_movement, 4)
        tunnelmessage_display(textQ, change_movement, 5)
        pygame.display.update()
        clock.tick(10)

#Only works with 4 choices atm
def DanishQ(choices = 4):
    print(platform.system())
    if platform.system() == "Windows":
        f = open("questions\danish_wordclass.txt","r")
    else:
        f = open("questions/danish_wordclass.txt","r")
    qList = [] #Makes an empty array
    for line in f: #Splits each line into a value in our array
        #Insert each line as value and strips new line
        qList.append(line.rstrip())
    #Select a question/answer pair from the list
    index = random.randint(0, len(qList)-1)
    #Split the line into question and answer seperately
    q = qList[index].split(",")[0]
    a = qList[index].split(",")[1]

    #Almost same proces for the list of answers
    if platform.system() == "Windows":
        g = open("questions\danish_wordclass_a.txt","r")
    else:
        g = open("questions/danish_wordclass_a.txt","r")
    aList = []
    for line in g:
        aList.append(line.rstrip())
    random.shuffle(aList)
    c = []
    for i in range(0,choices):
        c.append(aList[i])
    t = "Hvilken ordklasse er " + q + "?"
    for i in range(choices):
        if (a==c[i]):
            a = i
    return(t, c, a)
    #print(t) #The text of the question (e.g. "Hvilken ordklasse er Stol?")
    #print(a) #The number of the correct answer (e.g "3")
    #print(c) #Array of choices (e.g "Adjektiv","Verbum","Substantiv","Præposition")

#Works with any number of choices
def GeographyQ(choices = 4):
    if platform.system() == "Windows":
        f = open("questions\geography_capitals.txt","r")
    else:
        f = open("questions/geography_capitals.txt","r")
    
    qList = [] #Makes an empty array
    for line in f: #Splits each line into a value in our array
        #Insert each line as value and strips new line
        qList.append(line.rstrip())
    #Select a question/answer pair from the list
    index = random.randint(0, len(qList)-1)
    #Split the line into question and answer seperately
    q = qList[index].split(",")[0]
    a = qList[index].split(",")[1]
    c = [a]
    while(len(c)<choices):
        tempIndex = random.randint(0, len(qList)-1)
        if(tempIndex != index):
            c.append(qList[tempIndex].split(",")[1])
    random.shuffle(c)
    t = "Hvad er hovedstaden i " + q + "?"
    for i in range(choices):
        if (a==c[i]):
            a = i
    return(t, c, a)

#Works only with 4 choices
def MathQ():
    temp1 = random.randint(0,30)
    temp2 = random.randint(0,4-math.ceil(temp1/10))
    if (temp2 == 1):
        temp2 = 6
        if(temp1 > 15):
            temp2 = 3
    print(temp1 , "   " ,temp2)
    a = temp1 * temp2
    t = str(temp1) + " * " + str(temp2) + " = ?"
    c = []
    c.append(a)
    c.append(random.randint(1, abs(a-1)))
    c.append(random.randint(a+2, (a+1)*2+temp1+2))
    c.append(temp1+temp2)
    if(c[3]==1):
        c[3] = c[2]*3
    random.shuffle(c)
    for i in range(4):
        if (a==c[i]):
            a = i
    return(t, c, a)

game_loop()
pygame.quit()
quit()
