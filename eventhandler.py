import random
import os
from model.players import ATTR_TYPE
from model.groups import Gang, Force, League

EVENTS_LENGTH = 10
NEWGANGFORMCHANCE = 80 ##the higher this is, the less often new gangs form
NEWMEMBERCHANCE = 12 ##the higher this is, the more appeal a gang needs to attract a new member
CHOWNBLOCKNOTORIETY = 10 ##the amount of notoriety gained from taking over a block
NEWHEROCHANCE = 12 ##the higher this is, the more appeal the heroes need to attract a new hero

class eventhandler:
        def __init__(self):
            self.gameover = 0
            self.readytoplay = 1 ##Use this to determine if the player has accepted their turn
            self.turnindex = 0 ##use this to determine which set of groups' turn it is
            self.gangindex = 0 ##use this to determine whose turn it is within the gangs
            self.gangs = []
            self.groups = []
            self.groups.append(self.gangs)
            ##generate symbols
            self.symbols = []
            i = 0
            mystr = "1234567890!@$%^&*()qwertyuiopasdfghjklzxcvbnm<>?/"
            while i < len(mystr):
                self.symbols.append(mystr[i])
                i += 1
            self.eventsqueue = []
            self.heroesactive = 0

        def step(self):
            i = 0
            while i < len(self.eventsqueue):
                print(self.eventsqueue[i])
                i += 1
            if len(self.eventsqueue) > EVENTS_LENGTH:
                i = 0
                diff = len(self.eventsqueue) - EVENTS_LENGTH
                tmparray = []
                while i < EVENTS_LENGTH:
                    tmparray.append(self.eventsqueue[i + diff])
                    i += 1
                self.eventsqueue = tmparray

        def setHeroes(self):
            self.heroesactive = 1
            self.heroes = League(self)
            self.groups.append(self.heroes)

        def setForce(self):
            self.forceactive = 1
            self.force = Force(self)
            self.groups.append(self.force)

        def setBlocks(self, blocks):
            self.blocks = blocks
            ##give each gang 1 block to start
            for gang in self.gangs:
                testblock = self.blocks[random.randint(0,len(self.blocks)-1)][random.randint(0,len(self.blocks[0])-1)]
                while type(testblock.getOwner()) != type(0):
                    testblock = self.blocks[random.randint(0,len(self.blocks)-1)][random.randint(0,len(self.blocks[0])-1)]
                testblock.setOwner(gang)
                gang.changeBlockNum(1)

        def append(self, event):
            self.eventsqueue.append(event)

        def stepGroups(self):
            if self.turnindex == 0: ##case: it is a gang's turn
                if self.gangindex == len(self.gangs):
                    self.turnindex += 1
                    self.gangindex = 0
                    return
                else:
                    if(self.stepGangs()): ## stepGangs will return 1 if the gang took a step, 0 otherwise
                        self.gangindex += 1
            elif self.turnindex == 1: ## case: it is the heroes' turn
                self.stepHeroes()
                self.turnindex += 1
            elif self.turnindex == 2: ## case: it is the police force's turn
                self.stepForce()
                self.turnindex += 1
            else: ## everyone has taken their turn, time to do some "cleanup"
                for blockrow in self.blocks:
                    for block in blockrow:
                        owner = block.getOwner()
                        if type(owner) != type(0):
                            block.getOwner().addMoney(block.getBusiness().getIncome())
                if random.randint(0,NEWGANGFORMCHANCE) == 0:
                    self.newGang()
                self.turnindex = 0

        def stepGangs(self):
            gang = self.gangs[self.gangindex]
            if gang.isPlayerControlled():
                if self.readytoplay == 1:
                    gang.step()
                    return 1
                else:
                    return 0
            else:
                gang.step()
                return 1

        def newGang(self):
            randnum = random.randint(0,len(self.symbols)-1)
            self.gangs.append(Gang(self,self.symbols.pop(randnum)))
            self.append('{} has formed!'.format(self.gangs[len(self.gangs)-1].getName()))

        def newPlayerGang(self):
            randnum = random.randint(0,len(self.symbols)-1)
            self.gangs.append(Gang(self,self.symbols.pop(randnum)))
            self.append('{} has formed!'.format(self.gangs[len(self.gangs)-1].getName()))
            self.gangs[len(self.gangs)-1].setPlayerControlled(1)

        def stepHeroes(self):
            if self.heroesactive == 1:
                self.heroes.step()
                if len(self.heroes.getMembers()) == 0:
                    ##random chance that the league will be reformed
                    if random.randint(0,1) == 1:
                        self.append('{} has reborn!'.format(self.heroes.getName()))
                        self.heroes = League(self)
                    else:
                        self.append('{} has been disbanded!'.format(self.heroes.getName()))
                        self.heroesactive = 0

                if self.heroes.appeal > random.randint(0, NEWHEROCHANCE):
                    self.heroes.newMember()

        def stepForce(self):
            if self.forceactive == 1:
                self.force.step()

                if len(self.force.getMembers()) == 0:
                    self.append('{} has been reorganized by the mayor!'.format(self.force.getName()))
                    self.force = Force(self)

                if self.force.appeal > random.randint(0,8):
                    self.force.newMember()

        def destroyGang(self, gang):
            self.append('{} has been disbanded!'.format(gang.getName()))
            self.gangs.remove(gang)
            self.wipeBlocks(gang)
            if len(self.gangs) == 1:
                self.gameover = 1
                
        def printMembers(self, members):
            print ('Members:')
            for member in members:
                print ('{}, Not: {}, Heat: {}, Honor: {}, Inertia: {}'.format(member.getName(), \
                    member.getAttributes()[ATTR_TYPE.NOTORIETY].getValue(), member.getAttributes()[ATTR_TYPE.HEAT].getValue(),\
                    member.getAttributes()[ATTR_TYPE.HONOR].getValue(), member.getAttributes()[ATTR_TYPE.INERTIA].getValue()))
            print('')

        def printLeagues(self):
            if self.heroesactive == 1:
                print ('{}, Led by {}'.format(self.heroes.getName(), self.heroes.getLeader().getName()))
                self.printMembers(self.heroes.getMembers())

        def printForce(self):
            if self.forceactive == 1:
                print ('{}, Led by {}'.format(self.force.getName(), self.force.getLeader().getName()))
                self.printMembers(self.force.getMembers())

        def printGangs(self):
            for gang in self.gangs:
                print ('{} {}, Led by {}; ${}'.format(gang.getSymbol(), gang.getName(), gang.getLeader().getName(), gang.getMoney()))
                self.printMembers(gang.getMembers())

        def wipeBlocks(self,gang):
            for i in range(len(self.blocks)):
                for j in range(len(self.blocks[i])):
                    if self.blocks[i][j].getOwner() == gang:
                        self.blocks[i][j].setOwner(0)

        def printBlocks(self):
            ## print block map
            for i in range(len(self.blocks)):
                line = ""
                for j in range(len(self.blocks[i])):
                    if self.blocks[i][j].getOwner() == 0:
                        line = line + '#'
                    else:
                        line = line + self.blocks[i][j].getOwner().getSymbol()
                print (line)
