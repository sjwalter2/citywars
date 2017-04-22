from __future__ import division
import random
import member
import generator
from group import group

firstwordsgang = generator.wordlist("firstwordsgang")
lastwordsgang = generator.wordlist("lastwordsgang")

def firstname():
    return firstwordsgang[random.randint(0,len(firstwordsgang)-1)]

def lastname():
    return lastwordsgang[random.randint(0,len(lastwordsgang)-1)]


def name():
    return firstname() + " " + lastname()

class gang(group):
        def __init__(self, e,symbol):
            group.__init__(self,e)
            self.name = name()
            self.blocks = 0
            self.money = 0
            self.leader = member.member(self.e,self)
            self.leader.setNotoriety(random.randint(18,30))
            self.members = [self.leader]
            i = 0
            j = random.randint(3,4)
            while i < j:
                self.members.append(member.member(self.e,self))
                i += 1
            self.symbol = symbol
        
        def getSymbol(self):
            return self.symbol

        def changeBlockNum(self,i):
            self.blocks += i

        def getBlockNum(self):
            return self.blocks

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
                self.e.append("Alas, " + j.getName() + " has found there are no more mountains to conquer!")
            else:
                self.setAppeal(self.getAppeal() + 1)
                targetOwner = target.getOwner()
                target.setOwner(self)
                if type(targetOwner) != type(0):
                    j.setNotoriety(j.getNotoriety() + 10)
                    #self.e.append(j.getName() + " of " + self.name + " took over block " + str(target.getCoordinates()) + " from " + targetOwner.getName() + "!")
                    return targetOwner
                else:
                        j.setNotoriety(j.getNotoriety() + 5)
                        #self.e.append(j.getName() + " of " + self.name + " took over block " + str(target.getCoordinates()) + " that was just sitting there for the taking!")
                        return 0

        def newMember(self):
            self.members.append(member.member(self.e,self))

        def addMoney(self, i):
            self.money = self.money + i

        def getMoney(self):
            return self.money
