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

