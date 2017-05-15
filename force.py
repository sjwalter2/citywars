from __future__ import division
import random
import officer
from group import group

from naming.generator import NameGenerator

nameGenerator = NameGenerator('force')

class force(group):
    def __init__(self,e):
        group.__init__(self,e)
        self.name = nameGenerator.generate()
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
