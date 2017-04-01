import gang
import random
from member import member
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
##===================================================================================================================================================
##Gang functions
gangs = [] 

j = 0
while j < 4:
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
                    targetgang.kill(j)
                    if len(targetgang.getMembers()) == 0:
                        e.append(targetgang.getName() + " has been disbanded!")
                        gangs.remove(targetgang)
                        wipeBlocks(targetgang)
                        if len(gangs) == 1:
                            print gangs[0].getName() + " has taken over the city!"
                            printBlocks()
                            exit()
                else:
                    targetblocks = []
                    for blockx in blocks:
                        for blocky in blockx:
                            if blocky.getOwner() != gang:
                                targetblocks.append(blocky)
                    target = targetblocks[random.randint(0,len(targetblocks)-1)]
                    e.append(j.getName() + " of " + gang.getName() + " took over block " + str(target.getCoordinates()) + " from " + target.getOwner().getName() + "!")
                    target.setOwner(gang)


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
        blocks[j][i].setOwner(gangs[random.randint(0,len(gangs)-1)])
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
