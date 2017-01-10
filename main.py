import gang
import random
from member import member
from datetime import time, datetime, timedelta
from time import sleep
import os
import block

if os.name == 'nt':
    clear = 'cls'
else:
    clear = 'clear'

count = 0


##Gang generation
gangs = [] 

j = 0
while j < 4:
    gangs.append(gang.gang())
    j += 1

##Block generation
blocks = []

j = 0
while j < 5:
    y = []
    blocks.append(y)
    i = 0
    while i < 5:
        blocks[j].append(block.block())
        blocks[j][i].setOwner(gangs[random.randint(0,len(gangs)-1)])
        i += 1
    j += 1

eventsarray = []

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
    for gang in gangs:
        print gang.getSymbol() + " " + gang.getName() + ", Led by " + gang.getLeader().getName()
        print "Members: "
        for j in gang.getMembers():
            print j.getName() + ", Not:" + str(j.getNotoriety()) + ", Heat:" + str(j.getHeat()) + ", Honor:" + str(j.getHonor())
            events = j.step()
            if len(events) > 0:
                for event in events:
                    eventsarray.append(event)
        print ""
    print blocks[0][0].business.getName() + " " +  str(blocks[0][0].business.getIncome()) + " " + blocks[0][0].getOwner().getName()

    i = 0
    while i < len(blocks):
        j = 0
        line = ""
        while j < len(blocks[i]):
            line = line + blocks[i][j].getOwner().getSymbol()
            j += 1
        print line
        i += 1

    i = 0
    while i < len(eventsarray):
        print eventsarray[i]
        i += 1

    while datetime.now() < endstep:
        sleep(0.000001)
