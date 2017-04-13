from __future__ import division
import random
import officer
import generator
from group import group

firstwordsforce = generator.wordlist("firstwordsforce")
lastwordsforce = generator.wordlist("lastwordsforce")

def firstname():
    return firstwordsforce[random.randint(0,len(firstwordsforce)-1)]

def lastname():
    return lastwordsforce[random.randint(0,len(lastwordsforce)-1)]

def name():
    return firstname() + " " + lastname()

class force(group):
    def __init__(self,e):
        group.__init__(self,e)
        self.name = self.genName()
        self.leader = officer.officer(self.e,self)
        self.active = 1
        self.members = [self.leader]
        i = 0
        j = random.randint(3,4)
        while i < j:
            self.members.append(officer.officer(self.e,self))
            i += 1

    def getActive(self):
        return self.active

    def setActive(self,state):
        self.active = state

    def newMember(self):
        self.members.append(officer.officer(self.e,self))

    def genName(self):
        self.firstn = firstname()
        self.lastn = lastname()
        return self.firstn + " " + self.lastn
    
    def regenName(self):
        self.firstn = firstname()
        self.name = self.firstn + " " + self.lastn
