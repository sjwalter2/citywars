import random
import generator
import business

firstwordsblock = generator.wordlist("firstwordsblock")
lastwordsblock = generator.wordlist("lastwordsblock")

def firstname():
    return firstwordsblock[random.randint(0,len(firstwordsblock)-1)]

def lastname():
    return lastwordsblock[random.randint(0,len(lastwordsblock)-1)]


def name():
    return firstname() + " " + lastname()

class block(object):
        def __init__(self):
            self.name = name()
            self.owner = 0
            self.business = business.business()

        def getOwner(self):
            return self.owner

        def setOwner(self,input):
            self.owner = input

        def getBusiness(self):
            return self.business
