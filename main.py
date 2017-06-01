from time import sleep
import os
import block
import eventhandler
from model.groups import Gang, Force, League

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
    e.setHeroes()

##generate police
if enableforce == 1:
    e.setForce()

##generate gangs
for j in range(numgangs):
    e.newGang()

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
while 1:
    os.system(clear)

    print(count)
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

    sleep(1.5)
