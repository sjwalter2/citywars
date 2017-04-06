import generator
import random

firstwordshero = generator.wordlist("firstwordshero")
lastwordshero = generator.wordlist("lastwordshero")

def firstname():
    return firstwordshero[random.randint(0,len(firstwordshero)-1)]

def lastname():
    return lastwordshero[random.randint(0,len(lastwordshero)-1)]


def name():
    return firstname() + " " + lastname()

class hero(object):
	def __init__(self,e,league):
            self.e = e
            self.name = name()
            self.league = league
            self.setHeat(random.randint(0,100))
            self.setNotoriety(random.randint(0,20))
            self.setHonor(random.randint(90,100))
            self.setInertia(random.randint(0,5))

        def step(self):
            if self.heat > 0:
                self.heat -= 1
            if random.randint(0,15) == 15:
                self.heat += 50
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

        def getLeague(self):
            return self.league
