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

developerMode = False

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
removecrashcount = 0
levelcompletedcount = 0
controlhelp = 0
gameLevel = 1
gameActive = False
houseActive = False
pauseGame = False
carrotsTotal = 0
levelReached = 1

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
#Load hHouse background
houseImg = pygame.image.load('Art/house/bg.png')
houseImg = pygame.transform.scale(houseImg, (displayWidth, displayHeight))

#Load player graphics and size
playerWidth = 64
playerImg = pygame.image.load('Art/cannin/Skin/cannin_default.png')
playerImg = pygame.transform.scale(playerImg, (playerWidth, playerWidth))

tunnel_height = 200
tunnelImg = pygame.image.load('Art/background/tunnel_bg.png')
tunnelImg = pygame.transform.scale(tunnelImg, (gameWidth, tunnel_height))

#Load Carrots
carrotOneImg = pygame.image.load('Art/carrot/carrot_black_32x32.png')
carrotOneImg = pygame.transform.scale(carrotOneImg, (30, 30))
carrotOneDoneImg = pygame.image.load('Art/carrot/carrot_golden_32x32.png')
carrotOneDoneImg = pygame.transform.scale(carrotOneDoneImg, (30, 30))
carrotTwoImg = pygame.image.load('Art/carrot/carrot_black_32x32.png')
carrotTwoImg = pygame.transform.scale(carrotTwoImg, (30, 30))
carrotTwoDoneImg = pygame.image.load('Art/carrot/carrot_golden_32x32.png')
carrotTwoDoneImg = pygame.transform.scale(carrotTwoDoneImg, (30, 30))
carrotThreeImg = pygame.image.load('Art/carrot/carrot_black_32x32.png')
carrotThreeImg = pygame.transform.scale(carrotThreeImg, (30, 30))
carrotThreeDoneImg = pygame.image.load('Art/carrot/carrot_golden_32x32.png')
carrotThreeDoneImg = pygame.transform.scale(carrotThreeDoneImg, (30, 30))
topGoalLineImg = pygame.image.load('Art/background/goalline.png')
topGoalLineImg = pygame.transform.scale(topGoalLineImg, (gameWidth-20, 40))
topGoalLineCanninImg = pygame.image.load('Art/cannin/Skin/cannin_default.png')
topGoalLineCanninImg = pygame.transform.scale(topGoalLineCanninImg, (20, 20))
controlsHelpImg = pygame.image.load('Art/background/controls.png')
controlsHelpImg = pygame.transform.scale(controlsHelpImg, (gameWidth, 250))
menuBackground = pygame.image.load('Art/background/newmenu.png')
menuBackground = pygame.transform.scale(menuBackground, (displayWidth, displayHeight))
carrot = pygame.image.load('Art/carrot/carrot_32x32.png')
carrot = pygame.transform.scale(carrot, (64,64))

#Load Skins
skinDefault = pygame.image.load('Art/cannin/skin/cannin_default.png')
skinGold = pygame.image.load('Art/cannin/skin/cannin_gold.png')
skinOrange = pygame.image.load('Art/cannin/skin/cannin_orange.png')
skinRed = pygame.image.load('Art/cannin/skin/cannin_red.png')

#Load Arrows
arrowUp = pygame.image.load('Art/background/control_arrow_up.png')
arrowUp = pygame.transform.scale(arrowUp, (65,65))
arrowDown = pygame.image.load('Art/background/control_arrow_down.png')
arrowDown = pygame.transform.scale(arrowDown, (65,65))

def player(x,y, bg_movement):
    gameDisplay.fill(black)
    gameDisplay.blit(bgImg,(((displayWidth/2)-(gameWidth/2)),bg_movement))
    gameDisplay.blit(playerImg,(x,y))
    if (controlhelp < 40):
        gameDisplay.blit(controlsHelpImg,(((displayWidth/2)-(gameWidth/2)),gameHeight/100*50))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text, count):
    if count < 30:
        largeText = pygame.font.Font('arial.ttf',50)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((displayWidth/2),(gameHeight/2))
        gameDisplay.blit(TextSurf, TextRect)


def element(change_movement, progress):
    gameDisplay.blit(tunnelImg,(((displayWidth/2)-(gameWidth/2)),change_movement))
    gameDisplay.blit(topGoalLineImg,((((displayWidth/2)-(gameWidth/2))+10),10))
    gameDisplay.blit(topGoalLineCanninImg,((((displayWidth/2)-(gameWidth/2))+10 + progress),30))
    gameDisplay.blit(carrotOneImg,((((displayWidth/2)-(gameWidth/2))+(gameWidth/100*28)),10))
    if tunneldone == 1:
        gameDisplay.blit(carrotOneDoneImg,((((displayWidth/2)-(gameWidth/2))+(gameWidth/100*28)),10))
    gameDisplay.blit(carrotTwoImg,((((displayWidth/2)-(gameWidth/2))+(gameWidth/100*60)),10))
    if tunneldone == 2:
        gameDisplay.blit(carrotOneDoneImg,((((displayWidth/2)-(gameWidth/2))+(gameWidth/100*28)),10))
        gameDisplay.blit(carrotTwoDoneImg,((((displayWidth/2)-(gameWidth/2))+(gameWidth/100*60)),10))
    gameDisplay.blit(carrotThreeImg,((((displayWidth/2)-(gameWidth/2))+(gameWidth/100*92)),10))
    if tunneldone == 3:
        #Level succes
        gameDisplay.blit(carrotOneDoneImg,((((displayWidth/2)-(gameWidth/2))+(gameWidth/100*28)),10))
        gameDisplay.blit(carrotTwoDoneImg,((((displayWidth/2)-(gameWidth/2))+(gameWidth/100*60)),10))
        gameDisplay.blit(carrotThreeDoneImg,((((displayWidth/2)-(gameWidth/2))+(gameWidth/100*92)),10))

def crash():
    message_display('Du døde', 1)

def pause():
    message_display('Paused', 1)

def tunneltext_objects(text, font):
    tunneltextSurface = font.render(text, True, black)
    return tunneltextSurface, tunneltextSurface.get_rect()

def tunnelmessage_display(text, movement, textnumber):
    if textnumber == 1:
        xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*17)
        ycoordinate = movement+(displayHeight/100*5)
        if len(text) > 5:
            textSize = 15
            xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*22)
        elif len(text) > 12:
            textSize = 10
            xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*18)
        else:
            textSize = 20
            xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*20)
    if textnumber == 2:
        xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*38)
        ycoordinate = movement+(displayHeight/100*5)
        if len(text) > 5:
            textSize = 15
            xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*42)
        elif len(text) > 12:
            textSize = 10
            xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*40)
        else:
            textSize = 20
            xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*40)
    if textnumber == 3:
        xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*60)
        ycoordinate = movement+(displayHeight/100*5)
        if len(text) > 5:
            textSize = 15
            xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*62)
        elif len(text) > 12:
            textSize = 10
            xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*60)
        else:
            textSize = 20
            xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*57)
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
            xcoordinate = ((displayWidth/2)-(gameWidth/2))+(gameWidth/100*77)
    if textnumber == 5:
        xcoordinate = (displayWidth/2)
        ycoordinate = movement+(displayHeight/100*15)
        if len(text) < 10 and len(text) < 24:
            textSize = 35
            xcoordinate = (displayWidth/2)
        elif len(text) < 25:
            textSize = 20
        else:
            textSize = 15
    tunnelLargeText = pygame.font.Font('arial.ttf',textSize)
    tunnelTextSurf, tunnelTextRect = text_objects(text, tunnelLargeText)
    tunnelTextRect.center = (xcoordinate,ycoordinate)
    gameDisplay.blit(tunnelTextSurf, tunnelTextRect)

def houseLevel():
    x = (displayWidth/100) * 80
    y = (displayHeight/100) * 65
    global playerImg
    global houseActive
    global carrotsTotal
    houseActive = True
    playerImg = pygame.transform.scale(playerImg, (128, 128))
    isSelecting = False
    selectedSkin = playerImg
    indexSkin = 0
    skinArray = [skinDefault, skinGold, skinOrange, skinRed]
    priceArray = [0, 50, 25, 9]
    ownedArray = [True, False, False, False]

    while houseActive:
        gameDisplay.fill(black)
        gameDisplay.blit(houseImg,(0, 0))
        gameDisplay.blit(playerImg, (x,y))
        gameDisplay.blit(carrot, ((displayWidth/100)*2,(displayHeight/100)*2))
        print ("Carrots: ", carrotsTotal) #TODO: FIX

        #Handle inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if(x >= 0):
                        x += -40
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x += 40
                if event.key == pygame.K_UP and isSelecting == True:
                    if(indexSkin < len(skinArray)-1):
                        indexSkin += 1
                    else:
                        indexSkin = 0
                    selectedSkin = skinArray[indexSkin]
                if event.key == pygame.K_DOWN and isSelecting == True:
                    if(indexSkin > 0):
                        indexSkin -= 1
                    else:
                        indexSkin = len(skinArray)-1
                    selectedSkin = skinArray[indexSkin]
                if event.key == pygame.K_RETURN and isSelecting == True:
                    if ownedArray[indexSkin] == True:
                        playerImg = pygame.transform.scale(selectedSkin, (128, 128))
                    elif priceArray[indexSkin] <= carrotsTotal:
                        carrotsTotal -= priceArray[indexSkin]
                        ownedArray[indexSkin] = True
                        playerImg = pygame.transform.scale(selectedSkin, (128, 128))
                    else:
                        print("You dont have enough carrots for this outfit", carrotsTotal)
                        message_display("You dont have enough carrots for this outfit", 1)
        if(x <= 0):
            x = 0
        if(x > (displayWidth/100)*90):
            print("Exit house")
            houseActive = False
        if(x < (displayWidth/100)*25):
            isSelecting = True
            tempSkin = pygame.transform.scale(selectedSkin,(128,128))
            gameDisplay.blit(tempSkin, ((displayWidth/100)*10,(displayHeight/100)*30))
            gameDisplay.blit(arrowUp, ((displayWidth/100)*12,(displayHeight/100)*15))
            gameDisplay.blit(arrowDown, ((displayWidth/100)*12,(displayHeight/100)*55))
        else:
            isSelecting = False
            selectedSkin = playerImg


        pygame.display.update()
        clock.tick(10)
    openMenu()

def openMenu():
    global gameActive
    global gameLevel
    global levelReached
    global developerMode
    global carrotsTotal
    levelSelected = 0
    #gameActive = True #SKAL FJERNES NÅR MENU SKAL FIKSES
    while not gameActive:
        gameDisplay.fill(black)
        gameDisplay.blit(menuBackground,(0, 0))
        gameDisplay.blit(playerImg, (55*(displayWidth/768)+(197*levelSelected)*(displayWidth/768),displayHeight*0.56))
        gameDisplay.blit(carrot, ((displayWidth/100)*2,(displayHeight/100)*2))
        print ("Carrots: ", carrotsTotal) #TODO: FIX
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    developerMode = True
                    carrotsTotal = 200
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if levelSelected>0:
                        levelSelected -= 1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if levelSelected < 4 and levelSelected<levelReached:
                        levelSelected += 1
                if event.key == pygame.K_RETURN:
                    gameLevel = levelSelected
                    gameActive = True
        if (developerMode == True):
            levelReached = 3
        pygame.display.update()
        clock.tick(10)
    if (levelSelected == 0):
        print("Enter house")
        houseLevel()
    else:
        game_loop()

def game_loop():
    print("play game")
    x = (displayWidth * 0.50 - (playerWidth/2))
    y = (gameHeight * 0.85)
    change_movement = -200 - (gameHeight - y)
    progressTick = 0
    bg_movement = 0
    generateGate = True
    level = 1
    gateCount = 0
    global textQ
    global choicesQ
    global answerQ
    global gameLevel
    global carrotsTotal
    global levelReached
    global gameLevel
    global carrot

    tunnelCheck = False

    gameExit = False
    hasCrashed = False

    while not gameExit:
        global controlhelp
        global pauseGame
        gameDisplay.blit(carrot, ((displayWidth/100)*2,(displayHeight/100)*2))
        print ("Carrots: ", carrotsTotal) #TODO: FIX
        controlhelp += 1
        if(progressTick<gameWidth-40 and pauseGame == False and hasCrashed == False):
            progressTick += ((gameHeight*3)/5)/(gameWidth)
        #Do once
        if (generateGate == True):
            global gameLevel
            if (gameLevel == 1):
                textQ, choicesQ, answerQ = DanishQ()
            elif (gameLevel == 2):
                textQ, choicesQ, answerQ = GeographyQ()
            elif (gameLevel == 3):
                textQ, choicesQ, answerQ = MathQ()
            generateGate = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and pauseGame == False or event.key == pygame.K_LEFT and pauseGame == False:
                    if(x > displayWidth/2 - gameWidth/2):
                        x += -15
                if event.key == pygame.K_d and pauseGame == False or event.key == pygame.K_RIGHT and pauseGame == False:
                    if(x < displayWidth/2 + gameWidth/2 - playerWidth):
                        x += 15
                if event.key == pygame.K_p:
                    if (pauseGame == True):
                        pauseGame = False
                    else:
                        pauseGame = True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_m:
                    pauseGame = True
                    openMenu()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and pauseGame == False or event.key == pygame.K_LEFT and pauseGame == False:
                    if(x > displayWidth/2 + gameWidth/2 - playerWidth):
                        x += 15
                if event.key == pygame.K_d and pauseGame == False or event.key == pygame.K_RIGHT and pauseGame == False:
                    if(x < displayWidth/2 - gameWidth/2):
                        x += -15
        if x > (displayWidth * 0.5 + gameWidth * 0.5 - playerWidth):
            x = (displayWidth * 0.5 + gameWidth * 0.5  - playerWidth)
        elif x < (displayWidth * 0.5 - gameWidth * 0.5):
            x = (displayWidth * 0.5 - gameWidth * 0.5)


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
                carrotsTotal += 1
                print("Du har gennemført: ", tunneldone)
            else:
                print("Chose wrong gate: Call crash")
                hasCrashed = True
        if(tunnelCheck == True and hasCrashed == False):
            gateCount += 1

        #Updates player and game screen
        if (hasCrashed == False and pauseGame == False):
            change_movement += 5

        if (pauseGame == False):
            player(x,y, bg_movement)
            element(change_movement, progressTick)
        if tunneldone == 1 and gameLevel == 1:
            global removecount
            removecount +=1
            message_display("Din første gulerod! :)", removecount)
        elif tunneldone == 3:
            global levelcompletedcount
            levelcompletedcount +=1
            levelReached = gameLevel+1
            message_display("Level fuldført!", levelcompletedcount)

        if (pauseGame == False):
            tunnelmessage_display(choicesQ[0], change_movement, 1)
            tunnelmessage_display(choicesQ[1], change_movement, 2)
            tunnelmessage_display(choicesQ[2], change_movement, 3)
            tunnelmessage_display(choicesQ[3], change_movement, 4)
            tunnelmessage_display(textQ, change_movement, 5)
        if(levelcompletedcount > 30):
            global gameActive
            gameActive = False
            levelcompletedcount = 0
            tunneldone = 0

        if (change_movement > displayHeight and tunneldone != 3):
            gateCount = 0
            tunnelCheck = False
            generateGate = True
            change_movement = -200
        if hasCrashed == True:
            crash()
        if pauseGame == True:
            pause()
        if (gameActive == True):
            pygame.display.update()
            clock.tick(10)
        else:
            openMenu()

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
            if(qList[tempIndex].split(",")[1] not in c):
                c.append(qList[tempIndex].split(",")[1])
    random.shuffle(c)
    t = "Hvad er hovedstaden i " + q + "?"
    for i in range(choices):
        if (a==c[i]):
            a = i
    return(t, c, a)

#Works only with 4 choices
def MathQ():
    print("MathQ called")
    temp1 = random.randint(0,30)
    temp2 = random.randint(0,4-math.ceil(temp1/10))
    if (temp2 == 1):
        temp2 = 6
        if(temp1 > 15):
            temp2 = 3
    print(temp1 , "   " ,temp2)
    a = temp1 * temp2
    t = str(temp1) + " * " + str(temp2) + " = ?"
    print(t)
    c = []
    c.append(a)
    c.append(str(random.randint(1, abs(a-1))))
    c.append(str(random.randint(a+2, (a+1)*2+temp1+2)))
    c.append(str(temp1+temp2))
    random.shuffle(c)
    for i in range(4):
        if (a==c[i]):
            a = i
            c[i] = str(c[i])

    return(t, c, a)

openMenu()
