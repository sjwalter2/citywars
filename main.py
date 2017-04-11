import gang
import league
import random
from member import member
from hero import hero
from datetime import time, datetime, timedelta
from time import sleep
import os
import block
import eventhandler

if os.name == 'nt':
    clear = 'cls'
else:
    clear = 'clear'

count = 0
e = eventhandler.eventhandler()

##==================================================================================================================================================
##Configurable Vars
enableheroes = 1 ##Enable heroes faction
numgangs = 5 ##Set to number of starting gangs
enablepolice = 1 ##Enable police faction


##===================================================================================================================================================
##League functions

if enableheroes == 1:
    heroes = league.league(e)
    e.setHeroes(heroes)
    def printLeagues():
        if e.heroesactive == 1:
            print heroes.getName() + ", led by " + heroes.getLeader().getName()
            print "Members:"
            for j in heroes.getMembers():
                print j.getName() + ", Not:" + str(j.getNotoriety()) + ", Heat:" + str(j.getHeat()) + ", Honor:" + str(j.getHonor()) + ", Inertia:" + str(j.getInertia())
            print ""
##===================================================================================================================================================
##===================================================================================================================================================
##Gang functions
gangs = [] 
symbols = []
i = 0
mystr = "1234567890!@$%^&*()qwertyuiopasdfghjklzxcvbnm<>?/"
while i < len(mystr):
    symbols.append(mystr[i])
    i += 1
    

j = 0
while j < 5:
    randnum = random.randint(0,len(symbols)-1)
    gangs.append(gang.gang(e,symbols.pop(randnum)))
    j += 1

e.setGangs(gangs)

##===================================================================================================================================================
##===================================================================================================================================================
##Block generation
blocks = []

j = 0
while j < 5:
    y = []
    blocks.append(y)
    i = 0
    while i < 7:
        blocks[j].append(block.block(e,i,j))
        i += 1
    j += 1

for gang in gangs:
    testblock = blocks[random.randint(0,len(blocks)-1)][random.randint(0,len(blocks[0])-1)]
    while type(testblock.getOwner()) != type(0):
        testblock = blocks[random.randint(0,len(blocks)-1)][random.randint(0,len(blocks[0])-1)]
    testblock.setOwner(gang)
    gang.changeBlockNum(1)

e.setBlocks(blocks)

##===================================================================================================================================================
##Main Loop
while(0==0):
    os.system(clear)
    a = datetime.now()
    if a.second < 58:
        endstep = datetime(a.year,a.month,a.day,a.hour,a.minute,a.second+2,a.microsecond,a.tzinfo)
    else:
        if a.minute < 59:
            endstep = datetime(a.year,a.month,a.day,a.hour,a.minute+1,(a.second+2)%60,a.microsecond,a.tzinfo)
        else:
            endstep = a #this happens once every hour. Essentially by saying tihs, I am saying "at the end of this step just go ahead and start the next step because I cannot be assed to keep this going"
                        #stupid python datetime module
    print count
    count += 1

    ## gangs take turn
    e.stepGangs()
    e.printGangs()
    printLeagues()
    ## print businesses
    #i = 0
    #while i < len(blocks):
    #    j = 0
    #    while j < len(blocks[i]):
    #        print blocks[i][j].business.getName() + " " +  str(blocks[i][j].business.getIncome()) + " " + blocks[i][j].getOwner().getName()
    #        j += 1
    #    i += 1

    e.printBlocks()
    e.step()

    while datetime.now() < endstep:
        sleep(0.000001)
