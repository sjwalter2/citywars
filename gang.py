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

        def kill(self,killer):
            target = self.members[random.randint(0,len(self.members)-1)]
            if target.getNotoriety() == 0:
                chance = 100
            else:
                chance = killer.getNotoriety()/ (target.getNotoriety() * 2)
            if chance == 0:
                chance = 0.01
            if random.random() < chance:
                self.members.remove(target)
                noteriety = target.getNotoriety()
                killer.setNotoriety(killer.getNotoriety() + target.getNotoriety()//3)
                self.e.append(killer.getName() + "(" + str(killer.getNotoriety()) + ") of " + killer.getGroup().getName() + " killed " + target.getName() + "(" + str(target.getNotoriety()) + ") of " + self.name)
                if len(self.members) == 0:
                    return
                if target == self.leader:
                    self.leader = self.members[random.randint(0,len(self.members)-1)]
                    self.e.append(self.leader.getName() + " is now the leader of " + self.name + "!")
            else:
                self.e.append(killer.getName() + " of " + killer.getGroup().getName() + " failed to kill " + target.getName() + " of " + target.getGroup().getName() + "!")
                if killer.getNotoriety() == 0:
                    chance = 100
                else:
                    chance = target.getNotoriety()/(killer.getNotoriety() * 5)
                if chance == 0:
                    chance = 0.01
                if random.random() < chance:
                    self.e.append(killer.getName() + " of " + killer.getGroup().getName() + " was killed by " + target.getName() + " of " + target.getGroup().getName() + " in self-defense!")
                    target.setNotoriety(target.getNotoriety() + killer.getNotoriety()//3)
                    killer.getGroup().dies(killer) == 0
