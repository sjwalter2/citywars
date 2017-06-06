import random
from generator.naming import NameGenerator
from generator.players import MemberGenerator
from model.players import ATTR_TYPE

NEWMEMBERCHANCE = 12 ##the higher this is, the more appeal a gang needs to attract a new member
CHOWNBLOCKNOTORIETY = 10 ##the amount of notoriety gained from taking over a block
NEWMEMBERCOST = 10 ##Amount of appeal spent to gain a new member
NEWHEROCOST = 10 ##Amount of appeal spent to gain a new hero
NEWOFFICERCOST = 15 ##Amount of appeal spent to gain a new officer

class Group:

    def __init__(self, e):
        self.e = e
        self.appeal = 0
        self.nameGenerator = NameGenerator(self.getType())
        self.name = self.nameGenerator.generate()
        self.memberGenerator = MemberGenerator(e, self)
        self.leader = self.memberGenerator.generateLeader()
        self.members = [self.leader]
        for i in range(random.randint(3,4)):
            self.members.append(self.memberGenerator.generate())

    def getName(self):
        return self.name

    def getMembers(self):
        return self.members

    def getLeader(self):
        return self.leader

    def getType(self):
        return ''

    def newMember(self):
        member = self.memberGenerator.generate()
        self.members.append(member)
        self.e.append('{} has joined {}!'.format(member.getName(), self.getName()))
        self.appeal -= self.getNewMemberCost()

    def getNewMemberCost(self):
        return NEWMEMBERCOST

    def dies(self, victim):
        self.members.remove(victim)
        if len(self.members) == 0:
            return
        if victim == self.leader:
            self.leader = self.members[random.randint(0,len(self.members)-1)]
            self.e.append('{} is now the leader of {}!'.format(self.leader.getName(), self.name))

    def step(self):
        for member in self.getMembers():
            if member.step() == 1:
                targetgang = self.e.gangs[random.randint(0,len(self.e.gangs)-1)]
                member.kill(targetgang)


class League(Group):

    TYPE = 'league'

    def __init__(self,e):
        Group.__init__(self,e)

    def getType(self):
        return self.TYPE

    def getNewMemberCost(self):
        return NEWHEROCOST

class Force(Group):

    TYPE = 'force'

    def __init__(self,e):
        Group.__init__(self,e)

    def getType(self):
        return self.TYPE

    def getNewMemberCost(self):
        return NEWOFFICERCOST

class Gang(Group):

    TYPE = 'gang'

    def __init__(self, e, symbol):
        Group.__init__(self,e)
        self.blocks = 0
        self.money = 0
        self.symbol = symbol

    def getType(self):
        return self.TYPE

    def getSymbol(self):
        return self.symbol

    def changeBlockNum(self,i):
        self.blocks += i

    def getBlockNum(self):
        return self.blocks

    def step(self):
        for member in self.getMembers():
            if member.step() == 1:
                ##60% chance to attempt to take a block; 40% chance to attempt to assassinate an opponent
                if random.random() < 0.4:
                    targetgang = self.e.gangs[random.randint(0,len(self.e.gangs)-1)]
                    while targetgang.getName() == self.getName():
                        targetgang = self.e.gangs[random.randint(0,len(self.e.gangs)-1)]
                    member.kill(targetgang)
                else:
                    targetOwner = self.takeBlock(self.e.blocks, member)
                    if type(targetOwner) != type(0):
                        targetOwner.changeBlockNum(-1)
                        if targetOwner.getBlockNum() == 0:
                            self.e.destroyGang(targetOwner)
                            member.getAttributes()[ATTR_TYPE.NOTORIETY].increase(CHOWNBLOCKNOTORIETY)
                    self.changeBlockNum(1)
            if self.appeal > random.randint(0, NEWMEMBERCHANCE):
                self.newMember()

    ##Choose a block, adjacent to an owned block, that this gang does not own
    def chooseBlock(self,blocks):
        ownedblocks = []
        for blockx in blocks:
            for blocky in blockx:
                if type(blocky.getOwner()) != type(0):
                    if blocky.getOwner().getName() == self.name:
                        ownedblocks.append(blocky)
        ## I assert that len(ownedblocks) can be 0, if we are playing a game where a gang lives with no territory. Thus we will return a completely random block
        if len(ownedblocks) == 0:
            targetblocks = []
            for blockx in blocks:
                for blocky in blockx:
                    targetblocks.append(blocky)
            return targetblocks[random.randint(0,len(targetblocks)-1)]
        ## At this point we have a list of owned blocks; now we randomly select from them and find an adjacent unowned block. If all adjacent blocks are owned, pop the block.
        ## If we get to 0 owned blocks, then we own all territory, so we return 0.
        while len(ownedblocks) > 0:
            testblock = ownedblocks[random.randint(0,len(ownedblocks)-1)]
            adjacentblocks = []
            if testblock.getX() != 0:
                targblock = blocks[testblock.getY()][testblock.getX()-1]
                if targblock.getOwner() != self:
                    adjacentblocks.append(targblock)
            if testblock.getX() != len(blocks[0])-1:
                targblock = blocks[testblock.getY()][testblock.getX()+1]
                if targblock.getOwner() != self:
                    adjacentblocks.append(targblock)
            if testblock.getY() != 0:
                targblock = blocks[testblock.getY()-1][testblock.getX()]
                if targblock.getOwner() != self:
                    adjacentblocks.append(targblock)
            if testblock.getY() != len(blocks)-1:
                targblock = blocks[testblock.getY()+1][testblock.getX()]
                if targblock.getOwner() != self:
                    adjacentblocks.append(targblock)
            if len(adjacentblocks) == 0:
                ownedblocks.remove(testblock)
            else:
                return adjacentblocks[random.randint(0,len(adjacentblocks)-1)]
        return 0

    def takeBlock(self,blocks,j):
        target = self.chooseBlock(blocks)
        ## I assert that there can be a gang with no owned blocks, who could then attack anywhere if we are playing that a gang can still exist with 0 territory, or that a gang is fighting against non-territory holders
        if target == 0:
            self.e.append('Alas, {} has found there are no more mountains to conquer!'.format(j.getName()))
        else:
            self.appeal += 1
            targetOwner = target.getOwner()
            target.setOwner(self)
            if type(targetOwner) != type(0):
                j.getAttributes()[ATTR_TYPE.NOTORIETY].increase(10)
                #self.e.append(j.getName() + " of " + self.name + " took over block " + str(target.getCoordinates()) + " from " + targetOwner.getName() + "!")
                return targetOwner
            else:
                j.getAttributes()[ATTR_TYPE.NOTORIETY].increase(5)
                #self.e.append(j.getName() + " of " + self.name + " took over block " + str(target.getCoordinates()) + " that was just sitting there for the taking!")
                return 0


    def addMoney(self, i):
        self.money += i

    def getMoney(self):
        return self.money
