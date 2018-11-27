#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      OLIVER
#
# Created:     14-11-2018
# Copyright:   (c) OLIVER 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame
import random
import math
pygame.init()

#Only works with 4 choices atm
def DanishQ(choices = 4):
    f = open("questions\danish_wordclass.txt","r")
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
    g = open("questions\danish_wordclass_a.txt","r")
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
    f = open("questions\geography_capitals.txt","r")
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

input()
