import generator
import random

firstwordsmember = generator.wordlist("firstwordsmember")
lastwordsmember = generator.wordlist("lastwordsmember")

def firstname():
    return firstwordsmember[random.randint(0,len(firstwordsmember)-1)]

def lastname():
    return lastwordsmember[random.randint(0,len(lastwordsmember)-1)]


def name():
    return firstname() + " " + lastname()

class member(object):
	def __init__(self):
            self.name = name()
            self.setHeat(random.randint(0,100))
            self.setNotoriety(random.randint(0,20))
            self.setHonor(random.randint(90,100))

        def step(self):
            eventarray = []
            if self.heat > 0:
                self.heat -= 1
            if random.randint(0,15) == 15:
                eventarray.append(self.name + " did an event")
            return eventarray

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

