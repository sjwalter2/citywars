from __future__ import division
import random
import member
import generator

firstwordsgang = generator.wordlist("firstwordsgang")
lastwordsgang = generator.wordlist("lastwordsgang")

def firstname():
    return firstwordsgang[random.randint(0,len(firstwordsgang)-1)]

def lastname():
    return lastwordsgang[random.randint(0,len(lastwordsgang)-1)]


def name(input):
    if(input == "gang"):
        return firstname() + " " + lastname()

class gang(object):
        def __init__(self, e):
            self.e = e
            self.name = name("gang")
            self.leader = member.member(self.e,self)
            self.leader.setNotoriety(random.randint(18,30))
            self.members = [self.leader]
            i = 0
            j = random.randint(2,5)
            while i < j:
                self.members.append(member.member(self.e,self))
                i += 1
            self.symbol = random.choice('1234567890!@$%^&*()qwertyuiopasdfghjklzxcvbnm<>?/')
        
        def getName(self):
            return self.name

        def getMembers(self):
            return self.members

        def getLeader(self):
            return self.leader

        def getSymbol(self):
            return self.symbol

        def dies(self,victim):
            for i in self.members:
                if i == victim:
                    self.members.pop(victim)
                    return
            self.e.append(victim + " was supposed to die, but I couldn't find them!")

        def kill(self,killer):
            target = self.members[random.randint(0,len(self.members)-1)]
            if target.getNotoriety() == 0:
                chance = 100
            else:
                chance = killer.getNotoriety()/ (target.getNotoriety() * 2)
            if random.random() < chance:
                self.members.remove(target)
                noteriety = target.getNotoriety()
                killer.setNotoriety(killer.getNotoriety() + target.getNotoriety()//3)
                self.e.append(killer.getName() + "(" + str(killer.getNotoriety()) + ") of " + killer.getGang().getName() + " killed " + target.getName() + "(" + str(target.getNotoriety()) + ") of " + self.name)
                if len(self.members) == 0:
                    return
                if target == self.leader:
                    self.leader = self.members[random.randint(0,len(self.members)-1)]
                    self.e.append(self.leader.getName() + " is now the leader of " + self.name + "!")
            else:
                self.e.append(killer.getName() + " failed to kill " + target.getName() + "!")
