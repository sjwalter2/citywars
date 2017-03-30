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
##Gang generation
gangs = [] 

j = 0
while j < 4:
    gangs.append(gang.gang(e))
    j += 1

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
        blocks[j].append(block.block(e))
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

##===================================================================================================================================================
##Main Loop
while(0==0):
    os.system(clear)
    a = datetime.now()
    if a.second < 59:
        endstep = datetime(a.year,a.month,a.day,a.hour,a.minute,a.second+1,a.microsecond,a.tzinfo)
    else:
        if a.minute < 59:
            endstep = datetime(a.year,a.month,a.day,a.hour,a.minute+1,(a.second+1)%60,a.microsecond,a.tzinfo)
        else:
            endstep = a #this happens once every hour. Essentially by saying tihs, I am saying "at the end of this step just go ahead and start the next step because I cannot be assed to keep this going"
                        #stupid python datetime module
    print count
    count += 1

    ## print gang info
    for gang in gangs:
        print gang.getSymbol() + " " + gang.getName() + ", Led by " + gang.getLeader().getName()
        print "Members: "
        for j in gang.getMembers():
            print j.getName() + ", Not:" + str(j.getNotoriety()) + ", Heat:" + str(j.getHeat()) + ", Honor:" + str(j.getHonor()) + ", Inertia:" + str(j.getInertia())
            if j.step() == 1:
                targetgang = gangs[random.randint(0,len(gangs)-1)]
                while targetgang.getName() == gang.getName():
                    targetgang = gangs[random.randint(0,len(gangs)-1)]
                targetgang.kill(j)
                if len(targetgang.getMembers()) == 0:
                    e.append(targetgang.getName() + " has been disbanded!")
                    gangs.remove(targetgang)
                    wipeBlocks(targetgang)
        print ""

    ## print businesses
    #i = 0
    #while i < len(blocks):
    #    j = 0
    #    while j < len(blocks[i]):
    #        print blocks[i][j].business.getName() + " " +  str(blocks[i][j].business.getIncome()) + " " + blocks[i][j].getOwner().getName()
    #        j += 1
    #    i += 1

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

    e.step()

    while datetime.now() < endstep:
        sleep(0.000001)
