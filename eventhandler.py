import random

EVENTS_LENGTH = 10

class eventhandler(object):
        def __init__(self):
            self.eventsqueue = []
            self.heroesactive = 0

        def step(self):
            i = 0
            while i < len(self.eventsqueue):
                print self.eventsqueue[i]
                i += 1
            if len(self.eventsqueue) > EVENTS_LENGTH:
                i = 0
                diff = len(self.eventsqueue) - EVENTS_LENGTH
                tmparray = []
                while i < EVENTS_LENGTH:
                    tmparray.append(self.eventsqueue[i + diff])
                    i += 1
                self.eventsqueue = tmparray

        def setGangs(self,gangs):
            self.gangs = gangs

        def setHeroes(self,heroes):
            self.heroesactive = 1
            self.heroes = heroes

        def setBlocks(self,blocks):
            self.blocks = blocks

        def append(self, event):
            self.eventsqueue.append(event)

        def stepGangs(self):
            for gang in self.gangs:
                for j in gang.getMembers():
                    if j.step() == 1:
                        ##60% chance to attempt to take a block; 40% chance to attempt to assassinate an opponent
                        if random.random() < 0.4:
                            targetgang = self.gangs[random.randint(0,len(self.gangs)-1)]
                            while targetgang.getName() == gang.getName():
                                targetgang = self.gangs[random.randint(0,len(self.gangs)-1)]
                            j.kill(targetgang)
                        else:
                            targetOwner = gang.takeBlock(self.blocks,j)
                            if type(targetOwner) != type(0):
                                targetOwner.changeBlockNum(-1)
                                if targetOwner.getBlockNum() == 0:
                                    self.destroyGang(targetOwner)
                                    j.setNotoriety(j.getNotoriety() + 30)
                            gang.changeBlockNum(1)

            if self.heroesactive == 1:
                for j in self.heroes.getMembers():
                    if j.step() == 1:
                        targetgang = self.gangs[random.randint(0,len(self.gangs)-1)]
                        j.kill(targetgang)
                        if len(targetgang.getMembers()) == 0:
                            self.destroyGang(targetgang)
                        if len(self.heroes.getMembers()) == 0:
                            self.append(self.heroes.getName() + " has been disbanded!")
                            self.heroesactive = 0
                            self.heroes.setActive(0)

        def destroyGang(self,gang):
            self.append(gang.getName() + " has been disbanded!")
            self.gangs.remove(gang)
            self.wipeBlocks(gang)
            if len(self.gangs) == 1:
                print self.gangs[0].getName() + " has taken over the city!"
                self.printBlocks()
                exit()

        def printLeagues(self):
            if self.heroesactive == 1:
                print self.heroes.getName() + ", led by " + self.heroes.getLeader().getName()
                print "Members:"
                for j in self.heroes.getMembers():
                    print j.getName() + ", Not:" + str(j.getNotoriety()) + ", Heat:" + str(j.getHeat()) + ", Honor:" + str(j.getHonor()) + ", Inertia:" + str(j.getInertia())
                print ""


        def printGangs(self):
                for gang in self.gangs:
                    print gang.getSymbol() + " " + gang.getName() + ", Led by " + gang.getLeader().getName()
                    print "Members: "
                    for j in gang.getMembers():
                        print j.getName() + ", Not:" + str(j.getNotoriety()) + ", Heat:" + str(j.getHeat()) + ", Honor:" + str(j.getHonor()) + ", Inertia:" + str(j.getInertia())
                    print ""

        def wipeBlocks(self,gang):
            i = 0
            while i < len(self.blocks):
                j = 0
                while j < len(self.blocks[i]):
                    if self.blocks[i][j].getOwner() == gang:
                        self.blocks[i][j].setOwner(0)
                    j += 1
                i += 1

        def printBlocks(self):
            ## print block map
            i = 0
            while i < len(self.blocks):
                j = 0
                line = ""
                while j < len(self.blocks[i]):
                    if self.blocks[i][j].getOwner() == 0:
                        line = line + '#'
                    else:
                        line = line + self.blocks[i][j].getOwner().getSymbol()
                    j += 1
                print line
                i += 1

