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
