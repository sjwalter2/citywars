import random
from naming.generator import NameGenerator

nameGenerator = NameGenerator('hero')

class hero(object):
	def __init__(self,e,league):
            self.e = e
            self.name = nameGenerator.generate()
            self.group = league
            self.setHeat(random.randint(0,100))
            self.setNotoriety(random.randint(0,20))
            self.setHonor(random.randint(90,100))
            self.setInertia(random.randint(0,5))

        def step(self):
            if self.heat > 0:
                self.heat -= 1
            if random.randint(0,10) == 10:
                self.heat += 20
                return 1
            return 0

        def getName(self):
            return self.name

        def getHeat(self):
            return self.heat

        def setHeat(self,i):
            self.heat = i

        def getNotoriety(self):
            return self.notoriety

        def setNotoriety(self,i):
            self.notoriety = i

        def getHonor(self):
            return self.honor

        def setHonor(self,i):
            self.honor = i

        def setInertia(self,i):
            self.Inertia = i

        def getInertia(self):
            return self.Inertia

        def getGroup(self):
            return self.group

        def kill(self, targetgang):
            target = targetgang.getMembers()[random.randint(0,len(targetgang.getMembers())-1)]
            if target.getNotoriety() == 0:
                chance = 100
            else:
                chance = self.notoriety / (target.getNotoriety() * 2)
            if chance == 0:
                chance = 0.01
            if random.random() < chance:
                targetgang.dies(target)
                noteriety = target.getNotoriety()
                self.notoriety = self.notoriety + target.getNotoriety()//3
                self.e.append(self.name + "(" + str(self.notoriety) + ") of " + self.getGroup().getName() + " killed " + target.getName() + "(" + str(target.getNotoriety()) + ") of " + targetgang.getName())
                if len(targetgang.getMembers()) == 0:
                    self.notoriety = self.notoriety + 40
                    return
                if target == targetgang.getLeader():
                    targetgang.setLeader(targetgang.getMembers()[random.randint(0,len(targetgang.getMembers())-1)])
                    self.e.append(targetgang.getLeader().getName() + " is now the leader of " + targetgang.getName() + "!")
            else:
                #self.e.append(self.name + " of " + self.getGroup().getName() + " failed to kill " + target.getName() + " of " + targetgang.getName() + "!")
                if self.notoriety == 0:
                    chance = 100
                else:
                    chance = target.getNotoriety()/(self.notoriety * 5)
                if chance == 0:
                    chance = 0.01
                if random.random() < chance:
                    self.e.append(self.name + " of " + self.getGroup().getName() + " was killed by " + target.getName() + " of " + targetgang.getName() + " in self-defense!")
                    target.setNotoriety(target.getNotoriety() + self.notoriety//3)
                    self.getGroup().dies(self)
                    if len(self.getGroup().getMembers()) == 0:
                        target.setNotoriety(target.getNotoriety() + 30)

