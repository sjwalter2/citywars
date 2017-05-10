import gang
import league
import force
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
enableforce = 1 ##Enable police faction
citysize = 7 ##This-1 becomes the height/width of the city; for now cities are square but the code functions with any rectangle -- note that citysize MUST be at least 2 to avoid errors
##==================================================================================================================================================

##generate league
if enableheroes == 1:
    heroes = league.league(e)
    ##pass league to eventhandler
    e.setHeroes(heroes)

##generate police
if enableforce == 1:
    force = force.force(e)
    ##pass force to eventhandler
    e.setForce(force)

##generate gangs
j = 0
while j < numgangs:
    e.newGang()
    j += 1

##===================================================================================================================================================
##Block generation
blocks = []

##generate blocks
j = 0
while j < citysize:
    y = []
    blocks.append(y)
    i = 0
    while i < citysize:
        blocks[j].append(block.block(e,i,j))
        i += 1
    j += 1

##pass blocks to eventhandler
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
                        #I should note that this causes a couple hundred steps to occur at the end of every hour -- this needs to be fixed, but I need to fix the way I loop anyway
                        #stupid python datetime module
    print count
    count += 1

    ## gangs take turn
    e.stepGangs()
    e.stepHeroes()
    e.stepForce()
    e.printGangs()
    e.printLeagues()
    e.printForce()
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
