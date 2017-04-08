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
        def __init__(self, e):
            group.__init__(self,e)
            self.name = name()
            self.blocks = 0
            self.leader = member.member(self.e,self)
            self.leader.setNotoriety(random.randint(18,30))
            self.members = [self.leader]
            i = 0
            j = random.randint(3,4)
            while i < j:
                self.members.append(member.member(self.e,self))
                i += 1
            self.symbol = random.choice('1234567890!@$%^&*()qwertyuiopasdfghjklzxcvbnm<>?/')
        
        def getSymbol(self):
            return self.symbol

        def changeBlockNum(self,i):
            self.blocks += i

        def getBlockNum(self):
            return self.blocks

        def takeBlock(self,blocks,j):
            targetblocks = []
            for blockx in blocks:
                for blocky in blockx:
                    if type(blocky.getOwner()) == type(0):
                        targetblocks.append(blocky)
                    elif blocky.getOwner().getName() != self.name:
                        targetblocks.append(blocky)
                    ## I assert that len(targetblocks) could be 0 if we are playing that a gang can still exist with 0 territory, or that a gang is fighting against non-territory holders
            if len(targetblocks) == 0:
                self.e.append("Alas, " + j.getName() + " has found there are no more mountains to conquer!")
            else:
                target = targetblocks[random.randint(0,len(targetblocks)-1)]
                targetOwner = target.getOwner()
                target.setOwner(self)
                if type(targetOwner) != type(0):
                    j.setNotoriety(j.getNotoriety() + 10)
                    self.e.append(j.getName() + " of " + self.name + " took over block " + str(target.getCoordinates()) + " from " + targetOwner.getName() + "!")
                    return targetOwner
                else:
                        j.setNotoriety(j.getNotoriety() + 5)
                        self.e.append(j.getName() + " of " + self.name + " took over block " + str(target.getCoordinates()) + " that was just sitting there for the taking!")
                        return 0
