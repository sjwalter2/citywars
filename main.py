import gang
from member import member
from datetime import time, datetime, timedelta
from time import sleep
import os


if os.name == 'nt':
    clear = 'cls'
else:
    clear = 'clear'

count = 0

gangs = [] 

j = 0
while j < 4:
    gangs.append(gang.gang())
    j += 1

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
        print gang.name + ", Led by " + gang.leader.getName()
        print "Members: "
        for j in gang.members:
            print j.getName() + ", Not:" + str(j.getNotoriety()) + ", Heat:" + str(j.getHeat()) + ", Honor:" + str(j.getHonor())
            j.step()
        print ""
    while datetime.now() < endstep:
        sleep(0.000001)
