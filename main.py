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

j = 0
while j < 5:
    gangs.append(gang.gang(e))
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
                    targetblocks = []
                    for blockx in blocks:
                        for blocky in blockx:
                            if blocky.getOwner() != gang:
                                targetblocks.append(blocky)
                    ## I assert that len(targetblocks) could be 0 if we are playing that a gang can still exist with 0 territory, or that a gang is fighting against non-territory holders
                    if len(targetblocks) == 0:
                        e.append("Alas, " + j.getName() + " has found there are no more mountains to conquer!")
                    else:
                        target = targetblocks[random.randint(0,len(targetblocks)-1)]
                        targetOwner = target.getOwner()
                        if type(targetOwner) != type(0):
                            j.setNotoriety(j.getNotoriety() + 10)
                            e.append(j.getName() + " of " + gang.getName() + " took over block " + str(target.getCoordinates()) + " from " + targetOwner.getName() + "!")
                            targetOwner.changeBlockNum(-1)
                            if targetOwner.getBlockNum() == 0:
                                destroyGang(targetOwner)
                                j.setNotoriety(j.getNotoriety() + 30)
                        else:
                            j.setNotoriety(j.getNotoriety() + 5)
                            e.append(j.getName() + " of " + gang.getName() + " took over block " + str(target.getCoordinates()) + " that was just sitting there for the taking!")
                        gang.changeBlockNum(1)
                        target.setOwner(gang)
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
    while i < 5:
        blocks[j].append(block.block(e,i,j))
        newowner = gangs[random.randint(0,len(gangs)-1)]
        blocks[j][i].setOwner(newowner)
        newowner.changeBlockNum(1)
        i += 1
    j += 1

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
