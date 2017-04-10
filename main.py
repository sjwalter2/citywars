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

##===================================================================================================================================================
##League functions

heroes = league.league(e)
def printLeagues():
    if heroes.getActive() == 1:
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
    randnum = random.randint(0,len(symbols))
    gangs.append(gang.gang(e,symbols.pop(randnum)))
    j += 1

def stepGangs():
    for gang in gangs:
        for j in gang.getMembers():
            if j.step() == 1:
                ##60% chance to attempt to take a block; 40% chance to attempt to assassinate an opponent
                if random.random() < 0.4:
                    targetgang = gangs[random.randint(0,len(gangs)-1)]
                    while targetgang.getName() == gang.getName():
                        targetgang = gangs[random.randint(0,len(gangs)-1)]
                    j.kill(targetgang)
                    if len(targetgang.getMembers()) == 0:
                        destroyGang(targetgang)
                    if len(gang.getMembers()) == 0:
                        destroyGang(gang)
                else:
                    targetOwner = gang.takeBlock(blocks,j)
                    if type(targetOwner) != type(0):
                        targetOwner.changeBlockNum(-1)
                        if targetOwner.getBlockNum() == 0:
                            destroyGang(targetOwner)
                            j.setNotoriety(j.getNotoriety() + 30)
                    gang.changeBlockNum(1)

    if heroes.getActive() == 1:
        for j in heroes.getMembers():
            if j.step() == 1:
                targetgang = gangs[random.randint(0,len(gangs)-1)]
                j.kill(targetgang)
                if len(targetgang.getMembers()) == 0:
                    destroyGang(targetgang)
                if len(heroes.getMembers()) == 0:
                    e.append(heroes.getName() + " has been disbanded!")
                    heroes.setActive(0)


def destroyGang(gang):
    e.append(gang.getName() + " has been disbanded!")
    gangs.remove(gang)
    wipeBlocks(gang)
    if len(gangs) == 1:
        print gangs[0].getName() + " has taken over the city!"
        printBlocks()
        exit()

def printGangs():
        for gang in gangs:
            print gang.getSymbol() + " " + gang.getName() + ", Led by " + gang.getLeader().getName()
            print "Members: "
            for j in gang.getMembers():
                print j.getName() + ", Not:" + str(j.getNotoriety()) + ", Heat:" + str(j.getHeat()) + ", Honor:" + str(j.getHonor()) + ", Inertia:" + str(j.getInertia())
            print ""

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



##===================================================================================================================================================
##===================================================================================================================================================
##Block functions
def wipeBlocks(gang):
    i = 0
    while i < len(blocks):
        j = 0
        while j < len(blocks[i]):
            if blocks[i][j].getOwner() == gang:
                blocks[i][j].setOwner(0)
            j += 1
        i += 1

def printBlocks():
    ## print block map
    i = 0
    while i < len(blocks):
        j = 0
        line = ""
        while j < len(blocks[i]):
            if blocks[i][j].getOwner() == 0:
                line = line + '#'
            else:
                line = line + blocks[i][j].getOwner().getSymbol()
            j += 1
        print line
        i += 1


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
    stepGangs()
    printGangs()
    printLeagues()
    ## print businesses
    #i = 0
    #while i < len(blocks):
    #    j = 0
    #    while j < len(blocks[i]):
    #        print blocks[i][j].business.getName() + " " +  str(blocks[i][j].business.getIncome()) + " " + blocks[i][j].getOwner().getName()
    #        j += 1
    #    i += 1

    printBlocks()
    e.step()

    while datetime.now() < endstep:
        sleep(0.000001)
